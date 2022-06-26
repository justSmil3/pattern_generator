import imp
import numpy as np
from random import randint, random
import matplotlib.pyplot as plt
radius = 8

bayer_field = np.zeros((256, 256))

print(bayer_field)

while 0 in bayer_field:
    x = randint(0, 255);
    y = randint(0, 255);
    if (bayer_field[x][y] != 0): 
        continue;
    value = random()
    pcc = 0;
    pccxy = []
    for x2 in range(-radius, radius):
        for y2 in range(-radius, radius):
            x3 = np.clip(x + x2, 0, 255)
            y3 = np.clip(y + y2, 0, 255)
            if bayer_field[x3][y3] == 0:
                pcc += 1
            pccxy.append((x3, y3))
    if pcc >= radius * 0.7:
        for xy in  pccxy:
            bayer_field[xy[0]][xy[1]] = value        
    plt.imsave("tmp.png", bayer_field)