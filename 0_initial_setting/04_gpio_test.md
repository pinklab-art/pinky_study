# 4. 로봇 정상동작 테스트 - GPIO test
## 로봇의 pinky_test 폴더 안에서 New->Python3 파일 생성
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image29.png)

<br>

## Untitled를 클릭하면 이름 수정 가능
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image30.png)

<br>

## buzzer를 울리는 파일 코드를 두 개 작성한 후, 화면을 동시에 띄우고 순서대로 실행해보자!
- 파일 이름은 buzzer1, buzzer2로 수정
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image31.png)

<br>

## 두 번째 실행한 코드에서는 GPIO가 사용중이라는 에러가 발생한다
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image32.png)

<br>

## 이유는 무엇일까? 다시 Jupyter 파일 목록 부분으로 돌아오자
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image33.png)

<br>

## Running 에서 실행중인 커널 확인
- 여러개가 열려있을 것이다!
- 하드웨어 자원은 하나의 커널만 접근 가능한데 한 번에 여러 개의 커널에서 접근하려고 했기에 발생한 에러!

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image34.png)

<br>

## Shut Down All을 클릭해서 모든 커널을 닫아주기
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image35.png)

<br>

## 다시 buzzer2로 돌아오면 Kernel Unknown이 보인다

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image36.png)

<br>

## 코드를 실행해주면 Select Kernel이 뜨는데 Select 클릭

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image37.png)

<br>

## 다시 buzzer2 코드를 실행하면 하나의 커널만 접근하기 때문에 잘 실행이 된다
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image38.png)

<br>

## pinky.clean()을 코드 마지막에 넣고 다시 순서대로 실행해보자
- clean()은 GPIO 자원 해제하는 함수이기 때문에 커널 종료 없이 연속으로 실행 가능하도록 해준다

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image39.png)

<br>

## 카메라도 close() 없이 연속 실행해보면 에러가 난다. 

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image40.png)
![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image41.png)

<br>

## 이번에도 Shut Down All로 커널 종료

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image42.png)

<br>

## close() 코드를 추가하여 하드웨어 자원을 종료시키고 camera 코드를 연속 실행하면 에러 없이 동작 가능

![image](https://github.com/pinklab-art/pinky_study/blob/main/picture/initial_setting/02_03/image43.png)

<br>

## 결론
### 부저 또는 카메라와 같이 하드웨어 자원을 사용한 후에는 clean(), close()와 같은 닫아주는 함수를 반드시 실행하자.
