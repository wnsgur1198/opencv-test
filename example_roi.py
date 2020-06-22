import cv2

mouse_is_pressing = False   # 마우스 버튼 클릭상태를 체크하기 위한 변수
start_x, start_y = -1, -1   # 버튼의 누른 위치를 저장하기 위한 변수 -> ROI 시작점으로 사용


def mouse_callback(event, x, y, flags, param):
    global start_x, start_y, mouse_is_pressing

    img_result = img_color.copy()   # 결과 영상으로 사용하기 위한 원본 복사

    # 마우스 왼클릭하면 해당 좌표를 ROI 시작점으로 함
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_is_pressing = True
        start_x, start_y = x, y
        cv2.circle(img_result, (x, y), 10, (0, 255, 0), -1)     # 시작점에 초록색 원 출력
        cv2.imshow("img_color", img_result)

    # 버튼을 누른채 이동하면 ROI 시작점부터 현재 커서까지 초록색 사각형 그림
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_is_pressing:
            cv2.rectangle(img_result, (start_x, start_y), (x, y), (0, 255, 0), 3)
            cv2.imshow("img_color", img_result)

    # 버튼에서 손 떼면 해당 좌표를 ROI 끝좌표로 지정
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressing = False
        img_cat = img_color[start_y:y, start_x:x]
        img_cat = cv2.cvtColor(img_cat, cv2.COLOR_BGR2GRAY)
        img_cat = cv2.cvtColor(img_cat, cv2.COLOR_GRAY2BGR)
        img_result[start_y:y, start_x:x] = img_cat
        cv2.imshow("img_color", img_result)
        cv2.imshow("img_cat", img_cat)


img_color = cv2.imread('image/Billiard.jpg', cv2.IMREAD_COLOR)

cv2.imshow("img_color", img_color)
cv2.setMouseCallback('img_color', mouse_callback)   # 마우스이벤트 발생 시 호출될 콜백함수 지정

cv2.waitKey(0)

cv2.destroyAllWindows()
