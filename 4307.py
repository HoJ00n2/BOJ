# 29분 시작 

# 개미가 다 떨어질 때 까지 걸리는 최소 시간, 최대 시간
# 2 6 7 (10cm) >> 4초 8초
# 1초에 cm/s 가므로 서로 1cm차이날 때는 그대로 있으면 됨 (6 =>  <= 7) 이라면 다음엔 그냥 (6 7) 유지 (0.5s 에서만나고 0.5s에서 돌아가므로)
# 최소 시간은 아무도 안 부딪히고 바로 가까운 방향으로 가서 떨어지는 시간 (절반길이 기준 +-1 로 따지면 될 듯)
# 최대 시간은 안쪽의 개미가 최대한 많이 부딪히고 나중에 떨어져야 함

t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    ant = []
    for _ in range(n):
        ant.append(int(input()))
    
    min_time, max_time = 0, 0
    ant.sort()
    mid = l//2
    min_value = 10e9
    for i in range(n):
        value = abs(ant[i] - mid)
    idx = value.index(min(value))
    min_time = l - ant[idx]
    
    print(min_time, max_time, end=" ")
    
    