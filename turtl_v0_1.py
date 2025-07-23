import serial
import time
import turtle

# 전역 변수
connection = None
current_distance = 0
turtle_obj = None
is_moving = True
MIN_DISTANCE = 10  # 최소 거리 (cm)

def connect_sensor(port='COM3'):
    """센서 연결"""
    global connection
    try:
        connection = serial.Serial(port, 9600)
        time.sleep(2)
        print("센서 연결 성공")
        return True
    except Exception as e:
        print(f"센서 연결 실패: {e}")
        return False

def read_distance():
    """거리 측정값 읽기"""
    global connection, current_distance
    if connection and connection.in_waiting > 0:
        try:
            data = connection.readline().decode().strip()
            distance = float(data)
            # 유효한 거리값만 사용 (2-400cm)
            if 2 <= distance <= 400:
                current_distance = distance
                return distance
        except (ValueError, UnicodeDecodeError):
            pass
    return None

def setup_turtle():
    """Turtle 초기 설정"""
    global turtle_obj
    
    # 화면 설정
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.title("HC-SR04 Turtle Controller (MVP)")
    
    # Turtle 객체 생성
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.color("black")
    turtle_obj.speed(3)  # 적당한 속도로 설정
    
    print("Turtle 설정 완료")

def control_turtle():
    """거리에 따른 Turtle 제어"""
    global turtle_obj, is_moving, current_distance
    
    if current_distance < MIN_DISTANCE:
        # 최소 거리보다 가까우면 멈춤
        if is_moving:
            print(f"장애물 감지! 거리: {current_distance:.1f}cm - 정지")
            is_moving = False
    else:
        # 최소 거리보다 멀면 전진
        if not is_moving:
            print(f"경로 확보! 거리: {current_distance:.1f}cm - 이동 재개")
            is_moving = True
        
        # 직선으로 전진
        turtle_obj.forward(2)  # 작은 단위로 이동

def main():
    """메인 실행 함수"""
    print("=== HC-SR04 Turtle Controller MVP ===")
    print("기능: 직선 이동, 장애물 감지 시 정지")
    print("종료: Ctrl+C")
    
    # 센서 연결
    if not connect_sensor():
        print("센서 연결에 실패했습니다.")
        return
    
    # Turtle 설정
    setup_turtle()
    
    try:
        print("시스템 시작 - Turtle이 직선으로 이동합니다.")
        
        while True:
            # 거리 측정
            distance = read_distance()
            
            if distance is not None:
                # Turtle 제어
                control_turtle()
            
            # 짧은 딜레이
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        # 정리
        if connection:
            connection.close()
        turtle.bye()

if __name__ == "__main__":
    main()