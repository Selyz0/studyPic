import sys
sys.path.append('../modules')
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import option

def rgb2bgr(img):
    return img[:, :, ::-1]

def solve():
    im = np.array(Image.open(option.src))
    ans = rgb2bgr(im)
    option.disp_pics(im, ans)

def main():
    solve()

if __name__ == '__main__':
    main()