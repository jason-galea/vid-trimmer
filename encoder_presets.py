#! python3

import ffmpeg

def encode(encoder, filename, start_offset, duration, new_name):
    pass
    

def encode_nvenc(filename, start_offset, duration, new_name): # str, int(s), int(s), str, str
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