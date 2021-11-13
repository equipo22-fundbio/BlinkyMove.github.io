import cv2
import numpy as np
import dlib
from math import hypot

cap = cv2.VideoCapture(0)
board = np.zeros((500, 500), np.uint8)
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r"C:\Users\jear1\PycharmProjects\BlinkyMoveS\shape_predictor_68_face_landmarks.dat")

# Ajustes de teclado
keyboard = np.zeros((400, 1000, 3), np.uint8)
keys_set_1 = {0: "Q", 1: "W", 2: "E", 3: "R", 4: "T", 5: "Y", 6: "U", 7: "I", 8: "O", 9: "P",
              10: "A", 11: "S", 12: "D", 13: "F", 14: "G", 15: "H", 16: "J", 17: "K", 18: "L", 19: ",",
              20: "Z", 21: "X", 22: "C", 23: "V", 24: "B", 25: "N", 26: "M"}

def letter (letter_index, text, letter_light):
    #Teclas
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 100
        y = 0
    elif letter_index == 2:
        x = 200
        y = 0
    elif letter_index == 3:
        x = 300
        y = 0
    elif letter_index == 4:
        x = 400
        y = 0
    elif letter_index == 5:
        x = 500
        y = 0
    elif letter_index == 6:
        x = 600
        y = 0
    elif letter_index == 7:
        x = 700
        y = 0
    elif letter_index == 8:
        x = 800
        y = 0
    elif letter_index == 9:
        x = 900
        y = 0
    elif letter_index == 10:
        x = 0
        y = 100
    elif letter_index == 11:
        x = 100
        y = 100
    elif letter_index == 12:
        x = 200
        y = 100
    elif letter_index == 13:
        x = 300
        y = 100
    elif letter_index == 14:
        x = 400
        y = 100
    elif letter_index == 15:
        x = 500
        y = 100
    elif letter_index == 16:
        x = 600
        y = 100
    elif letter_index == 17:
        x = 700
        y = 100
    elif letter_index == 18:
        x = 800
        y = 100
    elif letter_index == 19:
        x = 900
        y = 100
    elif letter_index == 20:
        x = 0
        y = 200
    elif letter_index == 21:
        x = 100
        y = 200
    elif letter_index == 22:
        x = 200
        y = 200
    elif letter_index == 23:
        x = 300
        y = 200
    elif letter_index == 24:
        x = 400
        y = 200
    elif letter_index == 25:
        x = 500
        y = 200
    elif letter_index == 26:
        x = 600
        y = 200

    width = 100
    height = 100
    th = 3 #thickness
    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (147, 228, 141), -1)
    else:
        cv2.rectangle(keyboard, (x + th, y + th), (x + width - th, y + height - th), (147, 228, 141), th)

    # Ajuste de texto
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 6
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text)/2) + x
    text_y = int((height + height_text)/2) + y
    cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale, (255, 255, 255), font_th)

def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_PLAIN

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[0]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    #hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    #ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

def get_gaze_ratio(eye_points, facial_landmarks):
    right_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                             (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                             (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                             (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                             (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                             (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)], np.int32)
    # cv2.polylines(frame, [right_eye_region], True, (0, 0, 255), 2)

    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(frame, [right_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [right_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    min_x = np.min(right_eye_region[:, 0])
    max_x = np.max(right_eye_region[:, 0])
    min_y = np.min(right_eye_region[:, 1])
    max_y = np.max(right_eye_region[:, 1])

    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 70, 255, cv2.THRESH_BINARY_INV)
    height, width = threshold_eye.shape
    right_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    right_side_white = cv2.countNonZero(right_side_threshold)

    gaze_ratio = right_side_white
    return gaze_ratio

# Contadores
frames = 0
letter_index = 0
blinking_frames = 0
text = ""
keyboard_selected = "left"
last_keyboard_selected = "left"

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    keyboard[:] = (0, 0, 0)
    frames += 1
    new_frame = np.zeros((500, 500, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    active_letter = keys_set_1[letter_index]

    faces = detector(gray)
    for face in faces:
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x,y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        #Detectar parpadeos
        right_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        blinking_ratio = right_eye_ratio

        if blinking_ratio > 5.7:
            #cv2.putText(frame, "", (50, 150), font, 4, (0, 0, 0), thickness=3)
            blinking_frames += 1
            frames -= 1

            if blinking_frames == 5:
                text += active_letter
        else:
            blinking_frames = 0

        #Detección de mirada
        gaze_ratio_right_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio = gaze_ratio_right_eye



        if gaze_ratio <= 40 :
           keyboard_selected == "left"
           last_keyboard_selected = keyboard_selected

        else:
           keyboard_selected = "right"
           last_keyboard_selected = keyboard_selected

    # Letters
    if frames == 15:
        letter_index += 1
        frames = 0
    if letter_index == 15:
        letter_index = 0


    for i in range(27):
        if i == letter_index:
            light = True
        else:
            light = False
        letter(i, keys_set_1[i], light)

    cv2.putText(board, text, (10, 100), font, 4, 0, 3)


    cv2.imshow("Frame", frame)
    cv2.imshow("Keyboard", keyboard)
    cv2.imshow("Board", board)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()