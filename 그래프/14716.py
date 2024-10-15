from collections import deque

m, n = map(int, input().split())

graph = []
visited = [[0]*n for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [0,1,0,-1,-1,-1,1,1]
dy = [1,0,-1,0,1,-1,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        qx, qy = q.popleft()

        for i in range(8):
            nx, ny = qx + dx[i], qy + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny] != 0:
                continue
            if graph[nx][ny] != 1:
                continue
            q.append((nx,ny))
            visited[nx][ny] = 1
cnt = 0
for x in range(m):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            bfs(x,y)
            cnt += 1
print(cnt)
# for i in range(m):
#     print(visited[i])