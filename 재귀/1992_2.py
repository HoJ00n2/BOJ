N = int(input())

# 그래프 초기화
graph = [list(map(int, input().strip())) for _ in range(N)]

# 재귀적 탐색
def recur(x, y, boundary):
    cur = graph[x][y]

    # 현재 영역이 모두 같은 숫자인지 확인
    for i in range(boundary):
        for j in range(boundary):
            if graph[x + i][y + j] != cur:
                # 다른 숫자가 발견되면 사분할
                boundary //= 2
                # ()만 따로 반환하지말고, ()와 내부 숫자들을 한번에 반환하는 것이 좋음!
                return "(" + recur(x, y, boundary) + recur(x, y + boundary, boundary) + \
                           recur(x + boundary, y, boundary) + recur(x + boundary, y + boundary, boundary) + ")"

    # 모든 숫자가 같다면 하나의 숫자로 반환
    return str(cur)

# 정답 출력
print(recur(0, 0, N))
