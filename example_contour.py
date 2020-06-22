import cv2 as cv

img_color = cv.imread('image/sample_image_forContour.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)

# 컨투어를 검출하는 함수
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# 컨투어를 그리는 함수, 초록색으로, 두께는 3
cv.drawContours(img_color, contours, 0, (0, 255, 0), 3)

# 컨투어를 그리는 함수, 파란색으로, 두께는 3
cv.drawContours(img_color, contours, 1, (255, 0, 0), 3)

cv.imshow('result', img_color)
cv.waitKey(0)

cv.destroyAllWindows()
