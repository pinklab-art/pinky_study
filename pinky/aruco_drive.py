import numpy as np
import cv2
import time
from picamera2 import Picamera2
from pinkylib import Pinky
from ultralytics import YOLO
APPLE = 0
model = YOLO("best.pt")
print("load model")
aruco_dict_type = cv2.aruco.DICT_5X5_250 # 아루코마커 타입설정
markerLength = 0.035 #(m)
target_id_list = [8, 7, 11, 9]
target_id_index = 0
apple_ids = [7]
turn_right_ids = [8, 11]
end_id = 9
pose = {
    8 : [-3.6, 15],
    7 : [4.7, 25],
    11 : [-1, 15],
    9 : [3.5, 13]
}
with np.load('camera_calibration.npz') as data:
    calibration_matrix = data['camera_matrix']
    dist_coeffs = data['distortion_coefficients']
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'RGB888', "size": (640, 480)}))
picam2.start()
pinky = Pinky()
pinky.start_motor()
pinky.enable_motor()
def find_aruco():
    pinky.turn_right(30, 30)
    time.sleep(0.2)
    pinky.stop()
    time.sleep(1)
def turn_right():
    pinky.turn_right(30, 30)
    time.sleep(0.5)
    pinky.stop()
def turn_180():
    pinky.turn_right(30, 30)
    time.sleep(1)
    pinky.stop()
def find_apple(img):
    global APPLE
    pinky.stop()
    result = model(img, verbose=False)
    clss = result[0].boxes.cls.numpy()
    for i in clss:
        if i == 0:
            APPLE += 1
while True:
    L, R = 0, 0
    frame = picam2.capture_array()
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    target_id = target_id_list[target_id_index]
    target_x, target_z = pose[target_id]
    print(f"target id is {target_id}")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
    parameters = cv2.aruco.DetectorParameters_create()
    # 아루코 인식
    corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, cv2.aruco_dict, parameters=parameters)
    if ids is not None and target_id in ids:
        i = np.where(ids == target_id)[0][0]
        rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], markerLength, calibration_matrix,
                                                                dist_coeffs)
        aruco_x, aruco_y, aruco_z = tvec[0][0] * 100 # cm로 변환
        text = f"id: {ids[i][0]} x: {aruco_x:.2f}, y: {aruco_y:.2f}, z: {aruco_z:.2f}"
        print(text)
        if target_z > aruco_z and target_x < aruco_x + 0.3 and target_x > aruco_x - 0.3:
            print("stop")
            if target_id in turn_right_ids:
                print("trun right")
                turn_right()
            elif target_id  in apple_ids:
                print("detect apple")
                find_apple(frame)
                print(f"현재 인식한 사과 {APPLE} 개")
                print("turn 180")
                turn_180()
            elif target_id == end_id:
                print("fin")
                pinky.stop()
                break
            target_id_index += 1
        else:
            if target_z < aruco_z:
                L, R = 25, 25
            if target_x > aruco_x + 0.3:
                L = 30
            elif target_x < aruco_x - 0.3:
                R = 30
    else:
        print("find aruco")
        find_aruco()
    pinky.move(L, R)
    #cv2.imshow('Estimated Pose', frame)
    if cv2.waitKey(1) == ord('q'):
        break
print(f"인식된 사과 총 {APPLE} 개")
picam2.close()
pinky.stop_motor()
pinky.clean()
#cv2.destroyAllWindows()
