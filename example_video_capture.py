import cv2

cap = cv2.VideoCapture(0)

ret, img_color = cap.read()

cv2.imshow('Color', img_color)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
