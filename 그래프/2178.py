from collections import deque

n, m = map(int, input().split())

graph = list(input() for _ in range(n)) # 띄어쓰기 붙여서 받기 
visited = [[-1]*m for _ in range(n)] # -1이 아니면 방문 한 것

q = deque()
q.append((0,0))
visited[0][0] = 1 # 첫 칸 포함해야 하므로

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while q:
    qx, qy = q.popleft()
    
    for i in range(4):
        nx, ny = qx + dx[i], qy + dy[i]
        # 범주 체크
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽이라면
        if graph[nx][ny] == "0":
            continue
        # 방문 했다면
        if visited[nx][ny] != -1:
            continue
        # 나머지 경우에 대해서
        visited[nx][ny] = visited[qx][qy] + 1 # 해당 좌표에 이동한 칸수 저장
        q.append((nx,ny))
    
print(visited[n-1][m-1])