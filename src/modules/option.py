import matplotlib.pyplot as plt

src='C:/Users/Sely/Documents/work/studyPic/Gasyori100knock/dataset/images/imori_256x256.png'

def disp_pics(imgs, cmaps):
    fig, ax = plt.subplots(1, len(imgs))

    for i in range(len(imgs)):
        img = imgs[i]
        cmap = cmaps[i]
        if(cmap is None):
            ax[i].imshow(img)
        else:
            ax[i].imshow(img, cmap=cmap)
    plt.show()
