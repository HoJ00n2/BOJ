N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))

plus, zero, minus = 0, 0, 0

def recur(x, y, scope):
    global plus
    global zero
    global minus

    # 계속 쪼개서 1이 되거나, 모두 같은 덩어리면 개수 카운트하고 반환

    # 같은 덩어리 1개로 취급하기기
    # 영역 내 요소가 동일한가?
    identity = True
    # 영역 내 탐색
    for i in range(scope):
        for j in range(scope):
            if graph[x + i][y + j] != graph[x][y]:
                identity = False
    if identity:
        if graph[x][y] == -1:
            minus += 1
        elif graph[x][y] == 0:
            zero += 1
        else:
            plus += 1
        return

    # 1까지 쪼개졌을 때의 개수 업뎃
    if scope == 1:
        if graph[x][y] == -1:
            minus += 1
        elif graph[x][y] == 0:
            zero += 1
        else:
            plus += 1
        return

        

    # 탐색하면서 전부 같은지 판단, 영역 9로 쪼개기
    new_scope = scope // 3

    for i in range(3):
        for j in range(3):
            recur(x + i * new_scope, y + j * new_scope, new_scope)


recur(0, 0, N)
print(minus)
print(zero)
print(plus)