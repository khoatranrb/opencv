import numpy as np
import cv2
from matplotlib import pyplot as plt

def mir(X):
    for x in range(X):
        for y in range(512):
            img[y,2*X-x]=img[y,x].copy()

img =(np.zeros((512,512,3),np.uint8))
for i in range(511):
    for j in range(511):
        img[i][j]=[0,0,255]
img=cv2.line(img,(150,400),(256,70),(0,255,255),4)

mir(255)
img=cv2.line(img,(360,400),(80,175),(0,255,255),4)
img=cv2.line(img,(80,175),(430,175),(0,255,255),4)
img=cv2.line(img,(430,175),(150,400),(0,255,255),4)

for x in range(315):
    y1=0
    while(img[x][y1][1]!=255 and y1<510):
        y1+=1
    y2=511
    while(img[x][y2][1]!=255 and y2>0):
        y2 -= 1
    for y in range(y1,y2):
        img[x][y]=[0,255,255]
img2=img.copy()
for y in range(512):
    x1=310
    while(img[x1][y][1]!=255 and x1<510):
        x1+=1
    x2=511
    while(img[x2][y][1]!=255 and x2>315):
        x2 -= 1
    for x in range(x1,x2):
        img[x][y]=[0,255,255]
print("done")


# img=cv2.rectangle(img,(10,10),(40,40),(0,255,0),2)
# img=cv2.circle(img,(256,256),50,(0,0,255),3)
# img=cv2.ellipse(img,(256,256),(50,100),0,0,180,100,-1)
cv2.imshow('result', img),cv2.imshow('result2', img2) ,cv2.waitKey(0)

# cv2.namedWindow("image")
# cv2.imshow(img)
cv2.destroyAllWindows()
