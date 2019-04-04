import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("i.jpg",1)
b,g,r =cv2.split(img)
img2=cv2.merge([r,g,b])
img3=cv2.merge([g,r,b])
plt.subplot(221); plt.imshow(img)
plt.subplot(222);plt.imshow(img2)
plt.subplot(223);plt.imshow(img3)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
