# 시작점을 어떻게 설정할 것이냐?
# 각 단지의 수
# 각각의 덩어리를 어떻게 구분할 것이냐?

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[-1]*n for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    cnt = 1 # bfs 걸린 것 자체가 방문된 것이므로 1로 시작

    while q:
        qx, qy = q.popleft()
        # 4방향 탐색
        for i in range(4):
            # 다음 점이 어디임? 
            nx, ny = qx + dx[i], qy + dy[i]
            # 범주 내냐?
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 이미 방문 했다면?
            if visited[nx][ny]:
                continue
            # 집이 아니라면?
            # 집이 없는 경우가 0이므로 not으로 치환 가능 0만 False 이므로
            if not graph[nx][ny]:
                continue
            # 위 if에 다 안걸리고 온 애들은 큐에 넣어도 되는 애들
            visited[nx][ny] = 0
            q.append((nx,ny))
            cnt += 1
    
    return cnt

# bfs를 어디서 시작해야 하냐? 얼마나 돌아야 하냐?
ans = []
danji = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            ans.append(bfs(x,y))
            danji += 1
ans.sort()
print(danji)
print(*sorted(ans), sep="\n") # 꿀팁 (배열을 정렬하고 원소 단위마다 엔터로 끊어서 출력), for문으로 할 때 보다 시간을 빠르게 할 수 있음

# 파이써닉 출력 예제 비교 2 (후자가 시간을 좀 더 아낄 수 있음)
# l = [0, 1, 1, 1,1,1,1,1,1,1, ... 1]
# for i in l:
#     print(i)
# print("\n".join(list(map(str, l))))
