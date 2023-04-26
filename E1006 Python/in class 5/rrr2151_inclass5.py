import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


def rgb_ints_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3), dtype=np.uint8)
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 255
            # purple pixels
            # set all 3 color components
            img[x+50, y+50,:] = (0, 0, 128)
            # green pixels
            img[x+100,y+100,green] = 255
    return img

def onechannel(pattern, rgb):
    img = pattern
    color = rgb
    
    if color == 0:
        img[:,:,1], img[:,:,2] = 0, 0 
    elif color == 1:
        img[:,:,0], img[:,:,2] = 0, 0 
    elif color == 2:
        img[:,:,0], img[:,:,1] = 0, 0 

    return img

def permutecolorchannels(img, perm):
    i = img
    icopy = i.copy()
    r,g,b = perm
    # [2,0,1] red>blue, green>red, blue>green
    icopy[:,:,r] = i[:,:,0]
    icopy[:,:,g] = i[:,:,1]
    icopy[:,:,b] = i[:,:,2]
    
    return icopy

def decrypt(image, key):
    img = image
    key = key
    icopy = img.copy()  
    red,green,blue = range(3)
    
    for row in icopy:
        for rgb,k in zip(row,key):
            rgb[red] = rgb[red]^k
            rgb[green] = rgb[green]^k
            rgb[blue] = rgb[blue]^k
      
    return icopy

def main():
    permcolors = plt.imread('permcolors.jpg')
    correctPerm = [1,2,0]
    columbia = permutecolorchannels(permcolors, correctPerm)
    plt.imshow(columbia)
    plt.pause(0.001)
    
    key = np.load('key.npy')
    secret = plt.imread('secret.bmp')
    lights = decrypt(secret,key)
    plt.imshow(lights)
    plt.pause(0.001)
    
if __name__ == "__main__":
    main()
