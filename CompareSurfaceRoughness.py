import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./DataImage/wood_texture1.png')
cv2.imshow('temp',img)
cv2.waitKey()
cv2.destroyAllWindows()