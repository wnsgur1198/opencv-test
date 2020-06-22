import cv2
import numpy as np

img_color = cv2.imread("image/turtle.jpg", cv2.IMREAD_COLOR)

height, width, channel = img_color.shape
img_gray = np.zeros((height, width), np.uint8)

for y in range(0, height):      # y좌표 먼저 루프
    for x in range(0, width):   # 그 다음 x좌표 루프
        # 컬러 영상의 경우 픽셀값 읽어오기
        b = img_color.item(y, x, 0)     # 파랑
        g = img_color.item(y, x, 1)     # 초록
        r = img_color.item(y, x, 2)     # 빨강

        gray = (int(b) + int(g) + int(r)) / 3.0     # 그레이스케일 이미지화

        # 그레이스케일의 경우 픽셀값 저장하기
        img_gray.itemset(y, x, gray)

cv2.imshow('bgr', img_color)
cv2.imshow('gray', img_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()
