import sys
sys.path.append('../modules')
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import option

def rgb2hsv(img):
    _img = img.copy().astype(np.float32) / 255
    v_min = _img.min(axis=2)
    v_max = _img.max(axis=2)
    v_min_args = _img.argmin(axis=2)
    hsv = np.zeros_like(_img, dtype=np.float32)
    r, g, b = _img[..., 0], _img[..., 1], _img[..., 2]

    diff = np.maximum(v_max-v_min, 1e-10)
    ind = (v_min_args == 0)
    hsv[..., 0][ind] = 60 * (b-g)[ind] / diff[ind] + 180
    ind = (v_min_args == 1)
    hsv[..., 0][ind] = 60 * (r-b)[ind] / diff[ind] + 300
    ind = (v_min_args == 2)
    hsv[..., 0][ind] = 60 * (g-r)[ind] / diff[ind] + 60
    ind = (v_max == v_min)
    hsv[..., 0][ind] = 0

    hsv[..., 1] = (v_max-v_min)/v_max*100
    hsv[..., 2] = v_max*100

    return hsv

def hsv2rgb(hsv):
    _hsv = hsv.copy().astype(np.float32)
    H, S, V = _hsv[..., 0], _hsv[..., 1] / 100, _hsv[..., 2] / 100
    C = V*S
    H_ = H / 60
    X = C*(1-np.abs((H_%2) - 1))
    Z = np.zeros_like(X)

    rgb = np.zeros_like(_hsv)
    values = np.array([[C, X, Z], [X, C, Z], [Z, C, X], [Z, X, C], [X, Z, C], [C, Z, X]])

    for i in range(6):
        ind = (H_.astype(int) == i)
        for z in range(3):
            rgb[..., z][ind] = (V-C)[ind] + values[i, z][ind]

    return (rgb*255).astype(np.uint8)

def solve():
    im = np.array(Image.open(option.src))
    hsv = rgb2hsv(im)
    hsv[..., 0] = (hsv[..., 0] + 180) % 360
    ans = hsv2rgb(hsv)

    option.disp_pics([im, hsv.astype(np.uint8), ans], [None, 'hsv', None])
    return

def main():
    solve()

if __name__ == '__main__':
    main()