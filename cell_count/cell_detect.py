import cv2
import numpy as np

# window sliders
cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
cv2.createTrackbar('max_size', 'hsv', 600, 1000, lambda x: 0)
cv2.createTrackbar('min_size', 'hsv', 0, 1000, lambda x: 0)
cv2.createTrackbar('min_area', 'hsv', 100, 1000, lambda x: 0)
cv2.createTrackbar('min_sat', 'hsv', 150, 255, lambda x: 0)

img = cv2.imread('imgs/test.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def get_cell_contours(image, min_p, max_p, min_a, min_sat):
    lower_hsv = np.array([0, min_sat, 0])
    higher_hsv = np.array([180, 255, 255])
    mask_hsv = cv2.inRange(image, lower_hsv, higher_hsv)
    all_contours, hierarchy = cv2.findContours(mask_hsv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return [i for i in all_contours
            if min_p < cv2.arcLength(i, True) < max_p
            and min_a < cv2.contourArea(i)]


cells = 0
while True:
    # Update values and contours accordingly
    c_min_perimeter = cv2.getTrackbarPos('min_size', 'hsv')
    c_max_perimeter = cv2.getTrackbarPos('max_size', 'hsv')
    c_min_area = cv2.getTrackbarPos('min_area', 'hsv')
    min_sat = cv2.getTrackbarPos('min_sat', 'hsv')

    conts = get_cell_contours(hsv, c_min_perimeter, c_max_perimeter, c_min_area, min_sat)
    if len(conts) != cells:
        cells = len(conts)
        print("New cell number:", cells)

    im2 = img.copy()
    cv2.drawContours(im2, conts, -1, (0, 0, 255), thickness=2)
    cv2.imshow("hsv", im2)

    k = cv2.waitKey(100)
    if k == 27:
        break
