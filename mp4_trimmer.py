#! python3

# test test test new clone test test test 

import sys, getopt, os, re

from funcs import *
from encoder_presets import * 

def main(argv):
    cwd = os.getcwd()
    os.chdir(cwd) # This avoids having to add "cwd" to the start of the filename/new_name(s)
    reg = re.compile(r"\[(?P<timestamp>[^\[]+)\](?P<new_name>[^\[]+)")
    encoder = "h264" # Not needed since h264 is already the default for encode()

    # Receive arguments 
    try:
        opts, args = getopt.getopt(argv, "h", ["help", "h264", "hevc", "vp9", "nvenc"])
    except getopt.GetoptError:
        print("\nInvalid arguments\n")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help() # Prints help then exits
        elif opt == "--h264":
            pass # This is fine, right?
        elif opt == "--hevc":  
            encoder = "hevc"
        elif opt == "--vp9":
            encoder = "vp9"
        elif opt == "--nvenc":
            encoder = "nvenc"    

    print('>> This script will clean up any ".mp4" files in the current directory: "%s"' %(cwd))
    input()

    for filename in os.listdir(cwd):
        for timestamp, new_name in re.findall(reg, filename): # Returns tuple for each clip
            timestamp = timestamp.split(" to ")
            new_name = new_name.strip()
            start_offset = ts_convert(timestamp[0])
            duration = ts_convert(timestamp[1]) - start_offset + 1

            # (USE DIFFERENT BRANCH) Set new_name to chosen format
            if ".mp4" not in new_name: # Accounts for regex matching both "abc" and "abc.mp4" for group "new_name"
                new_name = new_name + ".mp4"
        
            # print('> encode("%s", "%s", %s, %s, "%s")\n' %(encoder, filename, start_offset + 1, duration, new_name))
            encode(encoder, filename, start_offset, duration, new_name)
            
            # exit() # Only encode one file

    input(">> Press any key to exit")
    exit()

if __name__ == "__main__":
   main(sys.argv[1:])