"""
초음파 센서에 따른 거북이 제어

1. 센서데이터
2. 거북이 제어 

MVP: Minimum Viable Product
최소 기능 제품 
test
"""

import serial
import time

# 전역 변수
connection = None
current_distance = 0
MIN_DISTANCE = 10

def connect_sensor(port='COM3'):
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False

def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting > 0:
        data = connection.readline().decode().strip()
        try:
            distance = float(data)
            
            
            if 2<= distance <=400:
                current_distance = distance
            return distance
        except:
            pass
    return None

def setup_tutle():
# turtle 초기설정
    s = tutle.Screen()
    
    t = turtle.Turtle()
    


def control_tutle(): # 거북이 제어
    #거리 조건에 따른 움직
    #상태 변환
    
    if current_distance < MIN_DISTANCE:
        if is moving:
            print(f"장애물")
            is_moving = False # 정리로 변경 
        
    else:
        if not is_moving:
            print(f"계속 간다")
            is_moving = True #이동으로 변경
            
        turtle.forward(2) 
        

def main():
    
    try:
        control_turtle()
        
    except KeyboardInterrupt:
        
    
    
    if connect_sensor():
        for i in range(10):
            dist = read_distance()
            if dist:
                print(f"거리: {dist}cm")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
