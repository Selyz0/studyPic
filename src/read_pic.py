import argparse
import cv2
import numpy as np

def add_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', 'pic reading file')

    return parser

def is_correct(src, dst):
    im = cv2.imread(src)
    dst_im = cv2.imread(dst)

    return np.array_equal(im, dst_im)

def read():
    parser = add_argparser()
    args = parser.parse_args()

    src = args.arg1

    return

def main():
    read()

if __name__ == '__main__':
    main()