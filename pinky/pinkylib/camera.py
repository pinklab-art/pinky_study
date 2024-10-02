import cv2
from IPython.display import display, clear_output, Image
import time
from picamera2 import Picamera2

import numpy as np
from glob import glob


class Camera:
    def __init__(self):
        self.picam2 = Picamera2()

        self.calibration_matrix = None
        self.dist_coeffs = None

    def start(self, width=640, height=480):
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": "RGB888", "size": (width, height)}))
        self.picam2.start()

    def display_jupyter(self, frame):
        _, buffer = cv2.imencode('.jpg', frame)
        clear_output(wait=True)
        display(Image(data=buffer, width=500))

    def get_frame(self):
        frame = self.picam2.capture_array()
        frame = cv2.rotate(frame, cv2.ROTATE_180)

        return frame

    def play_jupyter(self, play_time=3):
        start_time = time.time()
        while time.time() - start_time < play_time:
            frame = self.capture_frame()
            self.display_jupyter(frame)
    
            time.sleep(0.01)

    def close(self):
        self.picam2.close()

    def calibration_camera(self, img_path, checkerboard_size=(8, 6)):
        obj_points = []  # 3D 좌표 공간의 점들 (체커보드의 코너들)
        img_points = []  # 이미지 평면의 점들 (체커보드의 코너들)
    
        # 코너 검출 기준 설정
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # 3D 체커보드 좌표 초기화
        objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)

        # 이미지 파일 경로들 읽기
        images = glob(img_path + '/*.jpg')
        
        for image in images:
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # 체커보드 코너 찾기
            ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)

            if ret:
                obj_points.append(objp)  # 3D 점 추가
                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)  # 코너 정밀화
                img_points.append(corners2)  # 2D 점 추가

                # 이미지에 체커보드 코너 그리기
                img = cv2.drawChessboardCorners(img, checkerboard_size, corners2, ret)

            self.display_jupyter(img)# 이미지 표시
            cv2.waitKey(500)  # 0.5초 대기

        # 카메라 캘리브레이션 실행
        ret, camera_matrix, distortion_coefficients, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
        
        # 카메라 캘리브레이션 결과 저장
        np.savez("./camera_calibration.npz", camera_matrix=camera_matrix, distortion_coefficients=distortion_coefficients, rvecs=rvecs, tvecs=tvecs)
        
    def set_calibration(self, file_path="camera_calibration.npz"):
        with np.load(file_path) as data:
            self.calibration_matrix = data['camera_matrix']
            self.dist_coeffs = data['distortion_coefficients']

    def detect_aruco(self, frame, aruco_dict_type=cv2.aruco.DICT_5X5_250):
        if self.calibration_matrix is None or self.dist_coeffs is None:
            print("please set calibration file")
            return
        
        output_frame, pose = self.pose_estimation(frame, aruco_dict_type, self.calibration_matrix, self.dist_coeffs)

        self.display_jupyter(output_frame)

        if pose is None:
            return print("not detect aruco")

        return pose

    def pose_estimation(self, frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.aruco_dict = cv2.aruco.Dictionary_get(aruco_dict_type)
        parameters = cv2.aruco.DetectorParameters_create()

        corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, cv2.aruco_dict, parameters=parameters)

        if ids is not None:
            for i in range(len(ids)): # markerLength = 0.2 
                # Estimate pose of each marker and return the values rvec and tvec---(different from those of camera coefficients)
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[i], 0.02, matrix_coefficients,
                                                                        distortion_coefficients)
                print(f"rotation vector: {rvec}")
                print(f"translation vector: {tvec}\n")
                
                x, y, z = tvec[0][0] * 100 # cm로 변환
                text = f"id: {ids[i][0]} x: {x:.2f}, y: {y:.2f}, z: {z:.2f}"
                cv2.putText(frame, text, (int(corners[i][0][0][0]), int(corners[i][0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                
                # Draw a square around the markers
                cv2.aruco.drawDetectedMarkers(frame, corners)

                pose = [x, y, z]

        else:
            return frame, None
        
        return frame, pose