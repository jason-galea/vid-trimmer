# vid-trimmer
This is a quick script to clean up my oversized shadow-play recordings with ffmpeg.
Written in python, and interacting with ffmpeg via python-ffmpeg.

I began writing this script to help automate the trimming and re-encoding of some gameplay recordings that I had accumulated over several years. These recordings were vastly oversized for what they were, with excessive bitrates (30-60mbps for 1080p60fps) and often minutes of irrelevant footage per file.

# Requirements?

- ffmpeg installed (https://www.ffmpeg.org/)
- python3 installed (https://www.python.org/download/releases/3.0/)
- ffmpeg-python library installed (https://github.com/kkroening/ffmpeg-python)

You will also need some video files you want to trim down, with filenames matching the following formatting:
- "[1.33 to 1.41] cool clip #1.mp4"
- "[2.42 to 2.57] cool clip #2 [3.22 to 3.36] cool clip #3.mp4"

Please note that for "cool clip #1" this will explicitly cut from the start of the second at 1:33, to the beginning of the second at 1:41.
The 1:41 timestamp here is more of a stopping point, as the output file will not include the footage found at that second.

# HOW TO USE?

After installing the required programs and formatting your clips with timestamps/names, simply open a terminal in the directory containing your video files and execute the script.
