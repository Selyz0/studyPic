import sys
sys.path.append('../modules')
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import option

def rgb2gray(im):
    gray = im[:, :, [0]] * 0.2126 + im[:, :, [1]] * 0.7152 + im[:, :, [2]] * 0.0722
    gray = np.clip(gray, 0, 255)
    gray = gray.astype(np.uint8)
    return gray

def binalize(im, thre):
    return (im // thre) * 255

def solve():
    im = np.array(Image.open(option.src))
    gray = rgb2gray(im)
    ans = binalize(gray, 127)
    option.disp_pics(im, ans, cmap='gray')

def main():
    solve()

if __name__ == '__main__':
    main()