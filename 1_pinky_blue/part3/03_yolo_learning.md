# 3. Yolo 학습하기
## 원하는 물체를 딥러닝 학습하기 위해 사진을 찍어 데이터 모으기(20장 이상)
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image30.png)

<br>

## 라벨링하는 도구인 labelImg
- [라벨링 프로그램 다운로드 링크](https://github.com/HumanSignal/labelImg/releases/tag/v1.8.1)
- OS에 맞게 다운로드
- 경로에 한글이 있으면 안되므로 c:(cdrive)에 다운로드
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image31.png)

<br>

## 다운로드 받은 파일에서 압축을 풀고 data 폴더에서 predefined_classes 열기

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image32.png)

<br>

## 사과 색 구분을 위해 red, green을 입력해주자 (저장 필수)
- 사과가 아닌 다른 것을 학습한다면 이름을 바꿔주자

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image33.png)

<br>

## PC에서 APPLE이라는 폴더를 만들고 다음과 같이 구성
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image34.png)

<br>

## 그리고 train과 val의 images 폴더 안에 사진을 나누어 넣기
- train과 val의 사진 개수를 8:2비율로 나누기

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image35.png)

<br>

## 이제 압축을 푼 폴더에서 labelImg 더블 클릭해 실행
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image36.png)

<br>

## Open Dir 클릭
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image37.png)

<br>

## train 폴더의 images 를 열면
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image38.png)

<br>

## train 폴더안의 이미지들이 생기고 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image39.png)

<br>

## Change Save Dir를 눌러
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image40.png)

<br>

## train폴더의 labels로 설정해 라벨링한 데이터 저장 위치 지정하기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image41.png)

<br>

## PascalVOC 부분을 클릭해서
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image42.png)

<br>

## YOLO로 바꾸기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image43.png)

<br>

## 그리고 이제 라벨링 시작
- w키를 누르고 드래그하고 클래스를(red, green) 지정해 라벨링하기
- a 와 d 키로 다음 사진으로 이동하기
- 한 이미지마다 라벨링을 다하면 스페이스바 또는 ctrl+s로 라벨링 데이터 꼭 저장하기
- 이렇게 val에 있는 이미지도 완료하기

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image44.png)

<br>

## 라벨링이 다 되었으면 google drive 업로드 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image45.png)

<br>

## train, val 각 폴더의 labels 폴더 안을 확인해보자
- labels 폴더 안의 파일은 확장자가 txt이어야 한다
  
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image46.png)

<br>

## 확장자가 gdoc라면 아래 사진을 따라하고 다시 apple 폴더 업로드
- 구글 드라이브 톱니바퀴-> 설정 클릭
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image47.png)
- 아래로 내리다가 나오는 업로드 옵션이 체크되어 있다면 체크 해제해주기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image48.png)

<br>

## 그리고 drive에서 Colab열기 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image49.png)

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image50.png)

<br>

## GPU를 사용하기 위해 런타임 유형 변경 클릭
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image51.png)

<br>

## T4 GPU로 설정 후 저장
- GPU 연결될 때까지 대기

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image52.png)

<br>

## google Drive 마운트 하기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image53.png)

<br>

## 잘 마운트 되었는지 확인
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image54.png)

<br>

## 그리고 gpu 설정 되었는지 확인
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image55.png)

<br>

## colab에 yolo 설치하기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image56.png)

<br>

## 오른쪽 클릭으로 data.yaml 파일 추가
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image57.png)

<br>

## data.yaml 파일 더블클릭해서 오픈하고 다음 내용 추가 (저장 필수)
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image58.png)

<br>

## data.yaml파일의 train과 val의 경로는 오른쪽클릭 경로 복사로 수정하기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image59.png)

<br>

## 다음 코드를 colab에서 실행해 학습 시작하기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image60.png)

<br>

## 학습된 결과 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image61.png)

<br>

## 학습한 모델의 위치는 여기에
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image62.png)

<br>

## 학습된 결과 새로 사진을 찍어서 드라이브에 업로드하고 모델 검증 하기
- 코드안의 model_path와 image_path의 경로는 경로 복사해서 수정하기
- 
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image63.png)

<br>

## 결과
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image64.png)

<br>

## 검증이 되었으면 오른쪽 클릭해서 모델 다운로드
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image65.png)

<br>

## 드래그앤드랍으로 다운받은 파일 pinky 폴더 안에 넣기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image66.png)

<br>

##  yolo_test 새로운 파일 생성 후 검증해보기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/pinky_blue/image67.png)

<br>
