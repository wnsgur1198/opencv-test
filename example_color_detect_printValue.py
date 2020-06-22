import numpy as np
import cv2

color = [255, 0, 0]
pixel = np.uint8([[color]])

# cvtColor 함수로 BGR을 HSV로 변환
hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
hsv = hsv[0][0]

# 파란색에 대한 BGR과 HSV 값
print("bgr: ", color)
print("hsv: ", hsv)
