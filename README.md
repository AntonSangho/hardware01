# 초음파 센서에 따른 거북이 제어

# MVP (Minimum Viable Product): 최소 기능
- 초음파 센서로 장애물을 감지하면 직진하던 거북이가 멈춘다.

# 코드 동작설명
1. serial 라이브러리
2. 센서 연결
- 시리얼 연결
3. 데이터 처리니
- 초음파 센서 데이터를 2에서 400 사이의 값만 받는다.
4. Turtle 설정
- 그래픽 환경을 만든다.
- 거북이를 만든다.
5. 제어로직
- 상태 기반으로 거북이를 움직인다. is_moving 상태 변수
6. 메인 루프
- 반복적으로 움직이도록한다. 