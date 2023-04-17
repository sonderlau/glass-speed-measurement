import cv2
import numpy as np  

CHECKBOARD = (6, 9)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

obj_points = []
img_points = []

objp = np.zeros((1, CHECKBOARD[0] * CHECKBOARD[1], 3), np.float32)
objp[0, :, :2] = np.mgrid[0:CHECKBOARD[0], 0:CHECKBOARD[1]].T.reshape(-1, 2)

prev_img_shape = None

img = cv2.imread('./chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,corners = cv2.findChessboardCorners(gray, CHECKBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK +cv2.CALIB_CB_NORMALIZE_IMAGE)

if ret == True:
    obj_points.append(objp)
    corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)
    img_points.append(corners2)
    img = cv2.drawChessboardCorners(img, CHECKBOARD, corners2, ret)
    
cv2.imwrite('ch.jpg', img)


h,w = img.shape[:2]

ret, mtx , dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

test = cv2.imread('./test_measurement.jpg')

dist = cv2.undistort(test, mtx, dist, None, newcameramtx)

cv2.imwrite('calibrated.jpg', dist)