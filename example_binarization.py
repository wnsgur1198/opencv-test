import cv2


# 사용하지는 않지만 트랙바 생성에 필요한 더미함수
def nothing(x):
    pass


# 원래 생략가능하지만 윈도우창에 트랙바를 추가하기 위함
cv2.namedWindow('Binary')
cv2.createTrackbar('threshold', 'Binary', 0, 255, nothing)
cv2.setTrackbarPos('threshold', 'Binary', 127)  # 트랙바의 초기값 설정

# 컬러이미지 읽어오기
img_color = cv2.imread('red_ball.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Color', img_color)
cv2.waitKey(0)

# 그레이스케일 변환
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', img_gray)
cv2.waitKey(0)

# 트랙바를 조정하여 바로 반영하기 위한 루프
while True:
    low = cv2.getTrackbarPos('threshold', 'Binary')     # 트랙바 값을 임계값으로 설정
    # 이진화하기
    ret, img_binary = cv2.threshold(img_gray, low, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary', img_binary)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
