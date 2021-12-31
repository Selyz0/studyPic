import sys
sys.path.append('../modules')
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import option

def rgb2gray(im):
    gray = im[:, :, [0]] * 0.2126 + im[:, :, [1]] * 0.7152 + im[:, :, [2]] * 0.0722
    gray = np.clip(gray, 0, 255)
    gray = gray.astype(np.uint8)
    return gray

def binalize(im, thre):
    return (im > thre) * 255

def calc_thre_otsu(gray):
    max_v = -1
    max_th = 0
    M = gray.mean()
    for th in range(1, 255):
        w_0 = (gray <= th).sum().astype(np.float32)
        w_1 = (gray > th).sum().astype(np.float32)
        if(w_0 == 0 or w_1 == 0):
            continue
        M_0 = gray[gray <= th].mean()
        M_1 = gray[gray > th].mean()
        v_b = w_0*w_1*((M_0-M_1)**2)/((w_0+w_1)**2)

        if(max_v < v_b):
            max_v = v_b
            max_th = th

    return max_th

def ans():
    im = np.array(Image.open(option.src))
    gray = rgb2gray(im)
    th, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print(th)

def solve():
    im = np.array(Image.open(option.src))
    gray = rgb2gray(im)
    thre = calc_thre_otsu(gray)
    print(thre)
    ans = binalize(gray, thre)
    option.disp_pics([im, gray, ans], [None, 'gray', 'gray'])

def main():
    solve()

if __name__ == '__main__':
    main()