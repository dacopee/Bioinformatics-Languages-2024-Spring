
import sys
import fileinput
import os
import os.path
from os import path
import argparse


def main():
    parser = argparse.ArgumentParser(description='Hi, Welcome to Dans Gene Parsing Interface')
    parser.add_argument('command', help='Command to execute')
    
    args = parser.parse_args()

    if args.command == 'hello':
        print('Hello, World!')

def get_folder_path():
    folder_path = input("Enter the path to the folder: ")
    # Validate if the provided path is a directory
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a valid folder.")
        exit(1)
    return folder_path

if __name__ == '__main__':
    main()