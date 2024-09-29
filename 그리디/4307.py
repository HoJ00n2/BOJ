test = int(input())

for _ in range(test):
    l, n = map(int, input().split())
    ant = []
    for _ in range(n):
        ant.append(int(input()))
    
    # 개미 크기 정렬
    ant.sort()
    # 최소 시간, 최대 시간 초기화
    min_time, max_time = 0, 0

    # 최소 시간은 각자 가까운 방향으로 떨어질때, 가장 중간에 가까운 애가 떨어지는 시간
    mid = l / 2 # 판단하기 위한 길이의 평균값
    arr = [] # 중간값과의 거리 담는 배열
    for i in range(n):
        new_input = abs(ant[i] - mid)
        arr.append(new_input)

    a = min(l - (min(arr) + mid), abs(0 - (mid - min(arr))))
    min_time = int(a)

    # 최대 시간은 가장 멀리 있는애가 반대로 도착하는 시간
    max_time = max(l - ant[0], abs(0 - ant[-1])) 
    print(min_time, max_time)