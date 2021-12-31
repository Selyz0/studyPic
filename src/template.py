import sys
sys.path.append('../modules')
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import option

def solve():
    im = np.array(Image.open(option.src))
    # SOLVE PROBLEM TO IM

def main():
    solve()

if __name__ == '__main__':
    main()