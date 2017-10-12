#!/usr/bin/env python

import sys

if sys.version_info < (3, 6, 0):
    sys.stderr.write("You need python 3.6 or later to run this script\n")
    sys.exit(1)

import os
import argparse
import warnings
import pydub as pb

utility_description = '''
aurd "Aurora" SmArT is a CLI utility for converting supported audio
files.
'''
 
def trim_album():
    f = args.src_dir
    src = pb.AudioSegment.from_mp3(f)
    pass

args = None

def retrieve_args():
    parser = argparse.ArgumentParser(description=utility_description)

    parser.add_argument("-v", "--verbose", help="verbose output",
                        action="store_true")
    parser.add_argument('src_dir', help="source directory")
    parser.add_argument('dst_dir', help="general destination directory")
    rg = parser.parse_args()
    rg.src_dir = os.path.abspath(rg.src_dir)    # Takes care of the trailing slash, too
    rg.dst_dir = os.path.abspath(rg.dst_dir)
    
    print(f'src: "{rg.src_dir}"')
    print(f'dst: "{rg.dst_dir}"')
    return rg

    if not os.path.isdir(rg.src_dir):
        print('Source directory "{}" is not there.'.format(rg.src_dir))
        sys.exit()
    if not os.path.isdir(rg.dst_dir):
        print('Destination path "{}" is not there.'.format(rg.dst_dir))
        sys.exit()

    return rg


def main():
    global args

    try:
        warnings.resetwarnings()
        warnings.simplefilter('ignore')

        args = retrieve_args()
        trim_album()
    except KeyboardInterrupt as e:
        sys.exit(e)


if __name__ == '__main__':
    main()
