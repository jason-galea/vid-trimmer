#! python3

import sys

def ts_convert(s): # Eg: "2.42" >> 162
    s = str(s).split(".") # Eg: ["2", "42"]
    s = (int(s[0]) * 60) + int(s[1]) # Eg: 162 = (2*60) + 42
    return s

def print_help():
    print()
    print("Options:")
    print("-h   Show help options")
    print("\n")

    sys.exit(2)