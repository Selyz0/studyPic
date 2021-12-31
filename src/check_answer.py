import argparse
import cv2
import numpy as np

def add_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', 'test pic file')
    parser.add_argument('arg2', 'answer pic file')

    return parser

def is_correct(src, dst):
    im = cv2.imread(src)
    dst_im = cv2.imread(dst)

    return np.array_equal(im, dst_im)

def main():
    parser = add_argparser()
    args = parser.parse_args()

    src = args.arg1
    dst = args.arg2

    ans = 'Correct!' if is_correct(src, dst) else 'NOT Correct!'
    print(ans)

    return

if __name__ == '__main__':
    main()