# 45분 시작 >> 07분 종료

t = int(input())

for _ in range(t):
    # 출발지, 도착지
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input()) # 행성개수
    cnt = 0 # 정답 개수
    planet = []
    for i in range(n):
        # 각 행성계의 중점과 반지름 입력
        planet.append(list(map(int ,input().split())))

    # Q1 어떻게 해야 최소의 경계만 통과하고 도착할까?
    # >> 직선은 안 됨
    # Q2 내가 특정 원에 포함되어 있다는걸 어떻게 구분할까?
    # >> 이것만 알 수 있다면 시작점을 포함하는 원 개수 +
    # 도착점을 포함하는 원 개수 합친게 답
    # 원 마다 for문을 돌면서 이 안에 시작점 or 도착점이 있는지 판단?
    # 시작점과 행성 중심거리가 반지름에 포함되는지 판단!

    for i in planet:
        # 시작점, 도착점 모두 행성 내부에 들어 있을 때 >> no count
        if (x1 - i[0])**2 + (y1 - i[1])**2 < i[2]**2 and \
        (x2 - i[0])**2 + (y2 - i[1])**2 < i[2]**2:
            continue
        elif (x1 - i[0])**2 + (y1 - i[1])**2 < i[2]**2 :
            cnt += 1
        elif (x2 - i[0])**2 + (y2 - i[1])**2 < i[2]**2:
            cnt += 1
    
    print(cnt)