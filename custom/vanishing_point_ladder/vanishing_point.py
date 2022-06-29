# Coding interview 1
# Vanishing point

import numpy as np
import cv2

def vanishingPoint(line1, line2):

    # coordinates from tuple
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    # Ax + By = C (for both lines)
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

if __name__ == '__main__':

    # read image
    img = cv2.imread("ladder.png", 1)
    cv2.imshow('img', img)
    cv2.waitKey(2000)

    # mask with threshold
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(img, 5, 255, cv2.THRESH_BINARY_INV)
    mask = np.asarray(mask)
    cv2.imshow('mask', mask)
    cv2.waitKey(2000)

    # find cordinates of all points in the masked line
    allPointsInLine = cv2.findNonZero(mask)
    allPointsInLine = np.asarray(allPointsInLine)

    x_values = []
    y_values = []

    for idx in range(0, len(allPointsInLine)):

        new = allPointsInLine[idx]
        for i in new:
            x_values.append(i[0])
            y_values.append(i[1])

    # max and min y and x values
    x_max = max(x_values)
    y_max = max(y_values)

    x_min = min(x_values)
    y_min = min(y_values)

    topPoints_x = []
    bottomPoints_x = []

    for idx in range(0, len(allPointsInLine)):

        new = allPointsInLine[idx]

        for i in new:
            if i[1] <= y_min + 5:
                topPoints_x.append(i[0])

            if i[1] >= y_max + 5:
                bottomPoints_x.append(i[0])

    # 4 points
    # Top left (x1, y1)
    P1 = (min(topPoints_x), y_min)

    # Top right (x2, y2)
    P2 = (max(topPoints_x), y_min)

    # Bottom right (x3, y3)
    P3 = (x_max, y_max)

    # Bottom left (x4, y4)
    P4 = (x_min, y_max)

    print(f"\nFour points are: {P1}, {P2}, {P3} and {P4}" )

    # coordinates as tuples
    A = P1
    B = P2
    C = P3
    D = P4

    [px, py] = vanishingPoint((A,D), (B, C))
    print(f"\nVanishing point (X, Y) : {px, py}")
