import time
from pinkylib import Pinky

pinky = Pinky()

pinky.enable_motor()
pinky.start_motor()

try:
    while True:
        left_ir, center_ir, right_ir = pinky.read_ir()
        
        # 검은색 선이 인식될경우 0 흰색이 인식될경우 1
        print(left_ir, center_ir, right_ir)
        # 직진 100 101
        if left_ir == 1 and center_ir == 0 and right_ir == 0:   
            pinky.move(30, 30)
        elif left_ir == 1 and center_ir == 0 and right_ir == 1:
            pinky.move(30, 30)
    
        # 왼쪽으로 회전 000 001 011
        elif left_ir == 0 and center_ir == 0 and right_ir == 0:
            pinky.move(30, 40)
        elif left_ir == 0 and center_ir == 0 and right_ir == 1:
            pinky.move(30, 40)
        elif left_ir == 0 and center_ir == 1 and right_ir == 1:
            pinky.move(30, 40)
        
        # 오른쪽으로 회전 110
        elif left_ir == 1 and center_ir == 1 and right_ir == 0:   
            pinky.move(40, 30)

        # 검은색 선이없을 경우 정지 111
        else:
            pinky.move(0, 0)   
        time.sleep(0.1)

except KeyboardInterrupt:
    pinky.move(0, 0)
    pinky.clean()