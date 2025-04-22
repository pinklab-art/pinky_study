# 1. calibration
## pinky 폴더 내에 calib_img 폴더 생성
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image11.png)

<br>

## 정확한 측정을 위해 평평한 곳에 체커보드 붙이기
- 8X6, 25mm 체커보드 사용
- [체커보드 다운로드 링크](https://raw.githubusercontent.com/MarkHedleyJones/markhedleyjones.github.io/master/media/calibration-checkerboard-collection/Checkerboard-A4-25mm-8x6.pdf)
- 아루코마커로 정확한 위치를 얻으려면 카메라 캘리브레이션이 필수

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image12.png)

<br>

## 체커보드 사이즈 확인법 - 사각형 사이의 점들의 개수(가로X세로 = 8 X 6) 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image13.png)

<br>

## 정사각형의 너비 측정 - 25mm
- 따라서 우리는 8X6, 25mm 체커보드 사용

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image14.png)

<br>

## pinky 폴더 내에 capture 파일 생성 - 캘리브레이션을 위해 촬영할 파일

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image15.png)

<br>

## 필요한 모듈 import 및 카메라 설정
- jupyter notebook 셀에서 계속 작성
 
<pre>from pinkylib import Camera # 카메라 모듈 불러오기
import cv2 # OpenCV 모듈 불러오기

cam = Camera() # Camera 객체 생성
cam.start() # 카메라 시작

file_number = 1 # 파일 번호 초기화</pre>

<br>

## 캡쳐 코드 작성(c 입력 시 캡쳐, q 입력 시 종료)
- jupyter notebook 셀에서 계속 작성

<pre>while True:
    cmd = input("c is capture")
    if cmd == "c":
        frame = cam.get_frame()
        cv2.imwrite(f"./calib_img/{file_number}.jpg", frame) # 사진 저장
        print(f"Saved {file_number}.jpg")
        cam.display_jupyter(frame) # jupyter notebook에서 사진 확인
        file_number += 1
    
    if cmd == "q":  # q 키를 누르면 종료
        break

cam.close() # 카메라 닫기</pre>

<br>

## 촬영 요령 - 체커보드 전체가 나오는 사진을 조금씩 이동하며 10장 정도 촬영하기 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image18.png)

<br>

## calib_img 폴더 안에 잘 저장되었는지 확인
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image19.png)

<br>

## capture.ipynb로 다시 돌아와서 캘리브레이션 함수 실행 
- jupyter notebook 셀에서 작성

<pre>cam.calibration_camera("./calib_img")</pre>

<br>

## pinky 폴더 내에 캘리브레이션 파일 생겼는지 확인
- 생성되지 않았다면 사진촬영부터 다시 실행

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image21.png)

<br>

## 테스트 하기 전 마커 크기 확인
- 마커는 5X5이고, 마커의 너비도 측정하자(36mm)
- 항상 마커를 자를 때는 조금 여유를 두고 검정 박스가 잘리지 않도록 자르자
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image23.png)

<br>
