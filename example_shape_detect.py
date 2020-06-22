import cv2 as cv


# 컨투어 영역 내에 텍스트를 출력하는 함수
def setLabel(image, str, contour):
    # 주어진 문자열 외곽을 둘러쌀 수 있는 너비높이 계산
    (text_width, text_height), baseline = cv.getTextSize(str, cv.FONT_HERSHEY_SIMPLEX, 0.7, 1)

    # 컨투어 외곽을 둘러쌀 수 있는 위치너비높이 계산
    x, y, width, height = cv.boundingRect(contour)

    # 컨투어 외곽을 둘러싸는 박스의 정중앙에 텍스트와 텍스트박스 출력
    pt_x = x + int((width - text_width) / 2)
    pt_y = y + int((height + text_height) / 2)
    cv.rectangle(image, (pt_x, pt_y + baseline), (pt_x + text_width, pt_y - text_height), (200, 200, 200), cv.FILLED)
    cv.putText(image, str, (pt_x, pt_y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1, 8)


# 도형 검출에서 컬러는 필요없어서 바로 그레이스케일로
# 해도 되지만 보다 직관적인 이해를 위해 컬러로 함
img_color = cv.imread('image/image_for_shape_test.jpg', cv.IMREAD_COLOR)
cv.imshow('Color', img_color)
cv.waitKey(0)

# 그레이스케일로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', img_gray)
cv.waitKey(0)

# 이진화, 컨투어하는 영역이 흰색이 되고, 배경이 검은색이 되어야 함
ret, img_binary = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
cv.imshow('result', img_binary)
cv.waitKey(0)

# 바이너리 이미지에서 컨투어(경계) 검출
# cv.RETR_EXTERNAL 옵션으로 외곽 컨투어만 검출
# cv.CHAIN_APPROX_SIMPLE 옵션으로 검출되는 컨투어의 구성점 개수를 줄임
contours, hierarchy = cv.findContours(img_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# 검출된 컨투어를 직선으로 근사화
for cnt in contours:
    size = len(cnt)
    print(size)     # 컨투어하기 전 직선 개수

    epsilon = 0.005 * cv.arcLength(cnt, True)
    approx = cv.approxPolyDP(cnt, epsilon, True)
    size = len(approx)
    print(size)     # 컨투어한 후 직선 개수

    cv.line(img_color, tuple(approx[0][0]), tuple(approx[size-1][0]), (0, 255, 0), 3)
    for k in range(size-1):
        cv.line(img_color, tuple(approx[k][0]), tuple(approx[k+1][0]), (0, 255, 0), 3)

    if cv.isContourConvex(approx):  # 오목하게 들어간 도형을 잘못 판단하지 않게 하기 위한 조건문
        # 근사화된 직선 개수를 사용하여 컨투어 내부에 도형 이름 출력
        if size == 3:
            setLabel(img_color, 'triangle', cnt)
        elif size == 4:
            setLabel(img_color, 'rectangle', cnt)
        elif size == 5:
            setLabel(img_color, 'pentagon', cnt)
        elif size == 6:
            setLabel(img_color, 'hexagon', cnt)
        elif size == 8:
            setLabel(img_color, 'octagon', cnt)
        elif size == 10:
            setLabel(img_color, 'decagon', cnt)
        else:
            setLabel(img_color, str(size), cnt)
    else:
        setLabel(img_color, str(size), cnt)

    # 도형 옆에 직선 개수 출력
    # cv.putText(img_color, str(size), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, 8)

cv.imshow('result', img_color)
cv.waitKey(0)
