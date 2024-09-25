# 31분 시작 > 39분 종료

# 서로 다른 N개의 합이 S
# N이 최대가 되도록 하는 프로그램
# N이 최대가 되려면 결국 작은 값 부터 누적하다가 해당 값을 초과해버리면 거기서 종료
# 위의 방식보단 s - total과 cnt랑 비교해야함 (예제의 경우를 생각하면 누적으로 가면 안 됨)

# 1,19 2,18 3,17, 4,16, 5,15, 6,14, 6,13 8,12 9,11 10

s = int(input())

cnt = 1
total = 0

while True:
    total += cnt
    diff = s - total
    if cnt >= diff:
        print(cnt)
        break
    
    cnt += 1

