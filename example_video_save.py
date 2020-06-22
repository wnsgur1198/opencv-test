import cv2

cap = cv2.VideoCapture(0)

# 코덱 설정
fourcc = cv2.VideoWriter_fourcc(+'XVID')
# 영상저장을 위한 변수 생성, 프레임수는 보통 30으로 함(1초에30장읽는다는뜻)
writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

while True:
    ret, img_color = cap.read()

    if not ret:
        continue

    cv2.imshow('Color', img_color)

    # 영상 저장
    writer.write(img_color)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
writer.release()    # 자원 반환
cv2.destroyAllWindows()
