from tkinter.tix import MAIN
from unittest import main
import numpy as np

def SHIFT_TO_LSB(w):
    return w & 0x00FF

def SHIFT_TO_MSB(w):
    return (w >> 8) & 0x00FF

a = np.uint(-10000)
b = np.int16(-10000)
print(np.int16(a))
print(np.int16(b))

print(SHIFT_TO_LSB(a))
print(SHIFT_TO_MSB(a))

print(SHIFT_TO_LSB(b))
print(SHIFT_TO_MSB(b))