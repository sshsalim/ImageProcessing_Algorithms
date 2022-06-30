import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def line_distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

if __name__ == "__main__":
    img = cv2.imread('sample_image.png', 0)
    h,w = img.shape

    # only changed the values here  x and y
    centerRight = [0, int(h/2)]
    centerLeft = [int(w/2), 0]

    # -- Extract the line...
    # Make a line with "num" points...
    x0, y0 = centerLeft[0], centerLeft[1]  # These are in _pixel_ coordinates!!
    x1, y1 = centerRight[0], centerRight[1]

    # scale the length of the line
    x1 = centerRight[0]
    x2 = centerLeft[0]
    y1 = centerRight[1]
    y2 = centerLeft[1]

    num = line_distance(x1, y1, x2, y2)
    num = int(num)
    x, y = np.linspace(x0, x1, num), np.linspace(y0, y1, num)

    # Extract the values along the line
    zi = img[y.astype(int), x.astype(int)]

    # -- Plot...
    fig, axes = plt.subplots(nrows=2, figsize=(7, 7))
    axes[0].imshow(img, cmap = 'gray')
    axes[0].plot([x0, x1], [y0, y1], 'ro-')
    axes[0].axis('image')
    axes[0].set_xlabel('X')
    axes[1].set_xlabel('Distance along the evaluation line')
    axes[1].set_ylabel('Gray value of the pixel')
    axes[1].plot(zi)
    #plt.show()
    plt.savefig("plot_sample_image.png")
