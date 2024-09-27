from collections import deque

n = int(input())

graph = []
visited = [[-1]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 # 방문 처리
    cnt = 1

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue
            
            if visited[nx][ny] != -1:
                continue
            # 위 모든 조건이 아니라면 방문하기
            q.append((nx,ny))
            visited[nx][ny] = 1
            cnt += 1
    return cnt

arr = []
for x in range(n):
    for y in range(n):
        # 1이면서, 방문 안 했다면 탐색하기
        if visited[x][y] == -1 and graph[x][y] == 1:
            result = bfs(x,y)
            arr.append(result)

arr = sorted(arr)
print(len(arr))
for i in arr:
    print(i)

