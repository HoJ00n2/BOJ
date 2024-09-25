# 51분 시작 01분 종료료

# N, M이 주어졌을 때
# 중복없이 1 ~ N 까지 중 길이 M이 되는 답들을 모두 반환
# 백트래킹인건 알았는데, 어떻게 구현하나 ? 

arr = []
depth = 0 # 몇번이나 재귀했는가?
n, m = map(int, input().split())

def back(depth):
    if depth == m:
        print(*arr)
        return
    # 1 ~ n 사이의 수
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            back(depth+1)
            arr.pop()

back(0)