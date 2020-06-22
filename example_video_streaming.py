import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, img_color = cap.read()

    # 처음 영상을 읽어들이는데 실패했을 경우 고려
    if not ret:
        continue

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Color', img_color)
    cv2.imshow('Gray', img_gray)

    # ESC키 누르면 창 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
