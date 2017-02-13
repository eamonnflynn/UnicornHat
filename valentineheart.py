import unicornhat as UH
import sys
import time
import random
import math as math

UH.clear()
UH.brightness(0.5)


freq = 0.125
r = 0
while True:
    for i in range(64):

        r = int(math.sin(freq * i) * 127 + 128)
        #print (r)

        UH.set_pixel(4, 0, r, 0, 0)
        UH.set_pixel(3, 0, r, 0, 0)

        UH.set_pixel(5, 1, r, 0, 0)
        UH.set_pixel(3, 1, r, 0, 0)
        UH.set_pixel(4, 1, r, 0, 0)
        UH.set_pixel(2, 1, r, 0, 0)

        UH.set_pixel(6, 2, r, 0, 0)
        UH.set_pixel(2, 2, r, 0, 0)
        UH.set_pixel(3, 2, r, 0, 0)
        UH.set_pixel(4, 2, r, 0, 0)
        UH.set_pixel(5, 2, r, 0, 0)
        UH.set_pixel(1, 2, r, 0, 0)

        for y in range(3, 7):
            UH.set_pixel(7, y, r, 0, 0)
            UH.set_pixel(2, y, r, 0, 0)
            UH.set_pixel(3, y, r, 0, 0)
            UH.set_pixel(4, y, r, 0, 0)
            UH.set_pixel(5, y, r, 0, 0)
            UH.set_pixel(6, y, r, 0, 0)
            UH.set_pixel(1, y, r, 0, 0)
            UH.set_pixel(0, y, r, 0, 0)

        UH.set_pixel(5, 7, r, 0, 0)
        UH.set_pixel(2, 7, r, 0, 0)
        UH.set_pixel(6, 7, r, 0, 0)
        UH.set_pixel(1, 7, r, 0, 0)

        UH.show()
        time.sleep(0.01)
