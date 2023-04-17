import cv2
import numpy as np


img = cv2.imread('./measure/56.5.jpg')

img = img[ :, 0:894]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gaus = cv2.GaussianBlur(gray, (7,7), 1)
# cv2.imwrite('GAUS.jpg', gaus)

sobelx = cv2.Sobel(src=gaus, ddepth=cv2.CV_8U, dx=0, dy=1, ksize=5,delta=0)
sobelx = np.uint8(np.absolute(sobelx))


cv2.imwrite('sobel.jpg', sobelx)

retval, threshold = cv2.threshold(sobelx, 120, 255, cv2.THRESH_BINARY)

kernel = np.ones((1,1), np.uint8)
threshold = cv2.erode(threshold, kernel, iterations=1)
cv2.imwrite('erode.jpg', threshold)
threshold = cv2.dilate(threshold, kernel, iterations=1)

# ret,bi = cv2.threshold(sobelx, 10, 255, cv2.THRESH_BINARY)


# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
# dilation = cv2.dilate(bi, kernel, iterations=1)

cv2.imwrite('dilation.jpg', threshold)

lines = cv2.HoughLinesP(threshold, 1, np.pi / 180, threshold=200, minLineLength=400, maxLineGap=35)
for line in lines:
    x1,y1,x2,y2 = line[0]
    print(line[0])
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)


    
cv2.imwrite('./measure/line-detected/out.jpg', img)
# edges = cv2.Canny(gaus, 5, 100, apertureSize=3)
# cv2.imwrite('canny.jpg', edges)

# lines = cv2.HoughLinesP(sobelx, rho=1.0 ,theta= np.pi/180,threshold= 50, minLineLength=100, maxLineGap=20)

# print(len(lines[0]))

# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)


# cv2.imwrite('out.jpg', img)
