import cv2

# 0
image = cv2.imread("image/image_for_labeling.png", cv2.IMREAD_COLOR)
cv2.imshow("Color", image)
cv2.waitKey(0)

# 가우시안블러를 통해 이미지의 노이즈를 제거하여 흐릿하게 변함
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# BGR 에서 그레이스케일 이미지로 변환
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# 그레이스케일 이미지로부터 케니알고리즘으로 엣지 검출
edge = cv2.Canny(gray, 50, 150)
cv2.imshow("Edge", edge)
cv2.waitKey(0)

# 1
edge = cv2.bitwise_not(edge)
cv2.imshow("Reverse", edge)
cv2.waitKey(0)

# 컨투어 검출하고 그리는 부분 -> 이미지의 엣지가 보강됨(두꺼워짐) 하지 않으면 라벨링이 잘 안 될 수 있음
contours = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edge, contours[0], -1, (0, 0, 0), 1)
cv2.imshow("Contour", edge)
cv2.waitKey(0)

# 2
# 영역에 번호를 부여하기 위한 라벨링
nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(edge)

for i in range(nlabels):
    if i < 2:   # 라벨 0은 엣지, 라벨 1은 배경이므로 라벨링으로부터 제외
        continue

    # 컨투어로부터 넓이, 중심좌표, 영역박스좌표 등을 가져옴
    area = stats[i, cv2.CC_STAT_AREA]
    center_x = int(centroids[i, 0])
    center_y = int(centroids[i, 1])
    left = stats[i, cv2.CC_STAT_LEFT]
    top = stats[i, cv2.CC_STAT_TOP]
    width = stats[i, cv2.CC_STAT_WIDTH]
    height = stats[i, cv2.CC_STAT_HEIGHT]

    # 영역너비가 50보다 크면 영역을 둘러싼 사각형을 그리고 영역 중심에 원을 그린 후 라벨값 출력
    if area > 50:
        cv2.rectangle(image, (left, top), (left + width, top + height), (0, 0, 255), 1)
        cv2.circle(image, (center_x, center_y), 5, (255, 0, 0), 1)
        cv2.putText(image, str(i), (left + 20, top + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("result", image)
cv2.waitKey(0)
