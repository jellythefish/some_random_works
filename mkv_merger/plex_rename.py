#!/usr/bin/python3

# renames videos according to Plex Media Server naming rules

import argparse
from pathlib import Path
import os

def main():
    parser = argparse.ArgumentParser(description='renamer')
    parser.add_argument('new_name', type=str, help='name of a movie/tv show/etc...')
    parser.add_argument('season_number', type=str, help='number of a season')
    parser.add_argument('input_path', type=str, help='path with data')

    args = parser.parse_args()

    input_path = Path(args.input_path)
    video_files = os.listdir(input_path)
    
    video_files = sorted(video_files)
    
    for n, video in enumerate(video_files):
        ext = video.split(".")[-1]
        new_name = "{} s{}e{}.{}".format(args.new_name, str(args.season_number).zfill(2), str(n + 1).zfill(2), ext)
        os.rename(input_path/video, input_path/new_name)


if __name__ == '__main__':
    main()
