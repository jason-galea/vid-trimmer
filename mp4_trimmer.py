#! python3

# Consider this filename:
#       "[2.42 to 2.57] car moon jump [3.22 to 3.36] another cool clip.mp4"
# This will explicitly cut from the start of the second at 2:42, to the beginning of the second at 2:57.
# The actual content of the second at 2:57 is not included.

import os
import re
import ffmpeg

def encode_mp4(filename, start_offset, duration, new_name): # str, int(seconds), int(seconds), str
    (
        ffmpeg.input(filename, **{
            'vsync':0 # Never allow duplicate frames
            , 'hwaccel':'cuvid', 'c:v':'h264_cuvid' # Allow hwaccel with h264_cuvid decoder
        })
        .output(new_name, **{
            'c:v':'hevc_nvenc' # HEVC/H265 encoder
            , 'ss':start_offset + 1, 't':duration # Trim start & restrict duration (AKA. trim end)
            , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            , 'video_bitrate':'8M', 'audio_bitrate':'192K' # Bitrate settings (Audio still fluctuates, ehh)
        })
        .overwrite_output() # Same as "-y"
        .run()
    )

def ts_convert(s): # Eg: "2.42" >> 162
    s = str(s).split(".") # Eg: ["2", "42"]
    s = (int(s[0]) * 60) + int(s[1]) # Eg: 162 = (2*60) + 42
    return s

cwd = os.getcwd()
os.chdir(cwd) # This avoids having to add "cwd" to the start of the filename/new_name(s)
reg = re.compile(r"^\[(?P<timestamp>[^\[]+)\](?P<new_name>[^\[]+)")

print('>> This script will clean up any ".mp4" files in the current directory: "%s"' %(cwd))
input()

for filename in os.listdir(cwd):
    for timestamp, new_name in re.findall(reg, filename): # Returns tuple for each clip
        timestamp = timestamp.split(" to ")
        new_name = new_name.strip()
        start_offset = ts_convert(timestamp[0])
        duration = ts_convert(timestamp[1]) - start_offset
        if ".mp4" not in new_name: # Accounts for regex matching both "abc" and "abc.mp4" for group "new_name"
            new_name = new_name + ".mp4"
        # print('> encode_mp4("%s", %s, %s, "%s")\n' %(filename, start_offset, duration, new_name,)) # "encode"
        encode_mp4(filename, start_offset, duration, new_name)
        # exit()

input("\n>> Press any key to exit")
exit()