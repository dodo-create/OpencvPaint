import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Color Palette
colors = [(255, 0, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255), (0, 0, 0)]
color_names = ["Purple", "Green", "Blue", "Red", "Black"]
color_index = 0
current_color = colors[color_index]

# Create canvas
canvas = np.ones((720, 1280, 3), dtype=np.uint8) * 255
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Track shape drawing
prev_x, prev_y = 0, 0
frame_counter = 0

def draw_palette(img):
    for i, color in enumerate(colors):
        x = 20 + i * 100
        y = 20
        cv2.rectangle(img, (x, y), (x + 80, y + 80), color, -1)
        # Always use black text for all labels, including black paint
        text_color = (0, 0, 0)
        cv2.putText(img, color_names[i], (x, y + 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    text_color, 2)

def fingers_up(lm_list):
    up = []
    tip_ids = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
    for i in range(1, 5):  # Ignore thumb
        if lm_list[tip_ids[i]][2] < lm_list[tip_ids[i] - 2][2]:
            up.append(1)
        else:
            up.append(0)
    return sum(up)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img = frame.copy()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    pip_frame = frame.copy()

    index_x, index_y = 0, 0
    frame_counter += 1

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            lm_list = []
            h, w, _ = img.shape
            for id, lm in enumerate(hand_landmark.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            mp_draw.draw_landmarks(pip_frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            index_x, index_y = lm_list[8][1], lm_list[8][2]

            fingers = fingers_up(lm_list)

            # 1 finger: show cursor only (handled above)
            if fingers == 2:
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = index_x, index_y
                cv2.line(canvas, (prev_x, prev_y), (index_x, index_y), current_color, 5)
                prev_x, prev_y = index_x, index_y
            else:
                prev_x, prev_y = 0, 0

            # 3 fingers: change color
            if fingers == 3 and frame_counter % 20 == 0:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]

            # 4 or 5 fingers: erase
            if fingers == 4 or fingers == 5:
                cv2.circle(canvas, (index_x, index_y), 30, (255, 255, 255), -1)

    # Overlay canvas
    mask = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv_mask = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY_INV)
    inv_mask = cv2.cvtColor(inv_mask, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, inv_mask)
    # Ensure canvas is fully opaque (no alpha blending)
    img = cv2.bitwise_or(img, canvas)

    # Draw the black cursor above the canvas if a hand is detected
    if result.multi_hand_landmarks:
        # Use the last detected hand's index finger tip
        cv2.circle(img, (index_x, index_y), 14, (0, 0, 0), -1)

    # Draw UI elements
    draw_palette(img)
    pip_resized = cv2.resize(pip_frame, (150, 150))
    img[10:160, 1110:1260] = pip_resized  # 1280 - 150 - 20 (for margin)

    cv2.putText(img, f"Mode: {color_names[color_index]}", (1000, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (120, 0, 120), 2)
    cv2.putText(img, "1=Cursor 2=Draw 3=Color 4/5=Erase C=Clear", (10, 700), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (120, 0, 120), 2)

    cv2.imshow("HandPaint 🖌️", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('c') or key == ord('C'):
        canvas[:] = 255

cap.release()
cv2.destroyAllWindows()
