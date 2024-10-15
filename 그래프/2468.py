# 높이별로 BFS 시작
# 최대한 같은 부분이 반복되는 곳을 함수로 구현하자
from collections import deque
n = int(input())
graph = []
answer = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def BFS(rain):
    cnt = 0
    visited = [[-1]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            # 탐색점이 빗물보다 높고, 방문 안 한 곳이라면
            if graph[x][y] > rain and visited[x][y] == -1:
                # 탐색
                q = deque()
                q.append((x,y))
                visited[x][y] = 1
                cnt += 1
                while q:
                    qx, qy = q.popleft()
                    for i in range(4):
                        nx, ny = qx+dx[i], qy+dy[i]

                        if nx < 0 or ny < 0 or n <= nx or n <= ny:
                            continue
                        if graph[nx][ny] <= rain:
                            continue
                        if visited[nx][ny] != -1:
                            continue
                    
                        visited[nx][ny] = 1
                        q.append((nx,ny))
    return cnt

for rain in range(101):
    result = BFS(rain)

    if result > answer:
        answer = result

print(answer)