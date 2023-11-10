import cv2

cap = cv2.VideoCapture(0)  # 0 olarak değiştirildi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # Genişlik 1280 piksel olarak ayarlandı.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # Yükseklik 720 piksel olarak ayarlandı

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    # Piksel değerlerine göre renk tanıma yapıldı.

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "Undefined"
    if hue_value < 5:
        color = "KIRMIZI"
    elif hue_value < 22:
        color = "Turuncu"
    elif hue_value < 33:
        color = "SARI"
    elif hue_value < 78:
        color = "YEŞİL"
    elif hue_value < 131:
        color = "MAVi"
    elif hue_value < 170:
        color = "MOR"
    else:
        color = "KIRMIZI"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
