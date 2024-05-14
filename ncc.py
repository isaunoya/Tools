#!/usr/bin/env python3
import shutil
import subprocess
import sys

def main():
    my_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(int(sys.argv[1])):
        shutil.copy('D:/cp/tools/default.cpp', f'{my_array[i]}.cpp')
        subprocess.run(['subl', f'{my_array[i]}.cpp'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    main()
