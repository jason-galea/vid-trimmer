#! python3

import ffmpeg

def encode(encoder, filename, start_offset, duration, new_name):
    if encoder == "hevc":
        encode_hevc(filename, start_offset, duration, new_name)
    elif encoder == "vp9":
        encode_vp9(filename, start_offset, duration, new_name)
    elif encoder == "nvenc":
        encode_nvenc(filename, start_offset, duration, new_name)
    else:
        encode_h264(filename, start_offset, duration, new_name)

def encode_hevc(filename, start_offset, duration, new_name): # str, int(s), int(s), str, str
    (
        ffmpeg.input(filename, **{
            'vsync':0 # Never allow duplicate frames
        })
        .output(new_name, **{
            'c:v':'hevc'
            , 'ss':start_offset, 't':duration # Trim start & restrict duration
            , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            # , 'video_bitrate':'8M'
            , 'audio_bitrate':'192K'
        })
        .overwrite_output() # Same as "-y"
        .run()
    )

def encode_vp9(filename, start_offset, duration, new_name): # str, int(s), int(s), str, str
    (
        ffmpeg.input(filename, **{
            'vsync':0 # Never allow duplicate frames
        })
        .output(new_name, **{
            'c:v':'libvpx-vp9' # Google VP9 Encoder
            , 'ss':start_offset, 't':duration # Trim start & restrict duration
            , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            # , 'video_bitrate':'8M'
            , 'audio_bitrate':'192K'
        })
        .overwrite_output() # Same as "-y"
        .run()
    )

def encode_h264(filename, start_offset, duration, new_name): # str, int(s), int(s), str, str
    (
        ffmpeg.input(filename, **{
            'vsync':0 # Never allow duplicate frames
        })
        .output(new_name, **{
            'c:v':'libx264' # Boring old H264
            , 'ss':start_offset, 't':duration # Trim start & restrict duration
            , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            # , 'video_bitrate':'8M'
            , 'audio_bitrate':'192K'
        })
        .overwrite_output() # Same as "-y"
        .run()
    )

def encode_nvenc(filename, start_offset, duration, new_name): # str, int(s), int(s), str, str
    (
        ffmpeg.input(filename, **{
            'vsync':0 # Never allow duplicate frames
            , 'hwaccel':'cuvid', 'c:v':'h264_cuvid' # Allow hwaccel with h264_cuvid decoder
        })
        .output(new_name, **{
            'c:v':'hevc_nvenc' # NVENC accelerated HEVC encoder
            , 'ss':start_offset, 't':duration # Trim start & restrict duration
            , 'rc:v':'vbr_hq', 'cq:v':19, 'preset':'slow' # Quality settings
            , 'video_bitrate':'8M'
            , 'audio_bitrate':'192K'
        })
        .overwrite_output() # Same as "-y"
        .run()
    )