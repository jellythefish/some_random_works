#!/usr/bin/python3

import argparse
from pathlib import Path
import os
import logging
import subprocess
import sys
from dataclasses import dataclass

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

SOUND_FOLDER_NAME = "RUS Sound"
SUBS_FOLDER_NAME = "RUS Subs"
VIDEO_FOLDER_NAME = "Videos"
BINARY_PATH = Path("C:\Program Files\MKVToolNix\mkvmerge.exe")


@dataclass 
class FileName:
    sound: str
    sub: str
    video: str


def merge(input_path, input, output_path):
    cmd = [
        BINARY_PATH, "--output", output_path/input.video, "-A", 
        input_path/VIDEO_FOLDER_NAME/input.video, 
        input_path/SOUND_FOLDER_NAME/input.sound, 
        input_path/SUBS_FOLDER_NAME/input.sub
    ]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for c in iter(lambda: process.stdout.read(1), b''): 
        sys.stdout.buffer.write(c)


def main():
    parser = argparse.ArgumentParser(description='MKVMerger')
    parser.add_argument('input_path', type=str, help='path with needed folders')
    parser.add_argument('output_path', type=str, help='path to merged mkvs')

    args = parser.parse_args()

    input_path, output_path = Path(args.input_path), Path(args.output_path)

    input_folders = os.listdir(input_path)
    assert SOUND_FOLDER_NAME in input_folders
    assert SUBS_FOLDER_NAME in input_folders
    assert VIDEO_FOLDER_NAME in input_folders

    sound_files = os.listdir(input_path/SOUND_FOLDER_NAME)
    sub_files = os.listdir(input_path/SUBS_FOLDER_NAME)
    video_files = os.listdir(input_path/VIDEO_FOLDER_NAME)

    assert len(sound_files) == len(sub_files) == len(video_files)

    sound_files = sorted([elem for elem in sound_files])
    sub_files = sorted([elem for elem in sub_files])
    video_files = sorted([elem for elem in video_files])

    if not os.path.exists(output_path):
        logging.info("Output directory {} does not exist, creating...".format(output_path))
        os.makedirs(output_path)

    inputs = [
        FileName(sound, sub, video) 
            for sound, sub, video in zip(sound_files, sub_files, video_files)
    ]
    for idx, input in enumerate(inputs):
        merge(input_path, input, output_path)
        logging.info("{} out of {} is completed".format(idx + 1, len(inputs)))


if __name__ == '__main__':
    main()
