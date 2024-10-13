# # 3차원 bfs
# from collections import deque

# # 행, 열, 높이
# m, n, h = map(int, input().split())

# graph = []
# visited = [[[-1]*n for _ in range(m)] for _ in range(h)]

# dx = [-1,0,1,0,0,0]
# dy = [0,-1,0,1,0,0]
# dz = [0,0,0,0,-1,1]

# # 1은 익은, 0은 익지 않은, -1은 비어있음
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# def bfs(x,y,z):
#     q = deque()
#     q.append(x,y,z)
#     visited[x][y][z] = 0
#     day = 1

#     while q:
#         qx, qy, qz = q.popleft()
#         for i in range(6):
#             nx, ny, nz = qx + dx[i], qy + dy[i], qz + dz[i]
#             # 범주 내면
#             if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
#                 continue
#             # 방문 했다면
#             if visited[nx][ny][nz] == -1:
#                 continue
#             # 빈칸이라면 넘어가기
#             if graph[nx][ny][nz] == -1:
#                 continue
            
#             q.append((nx,ny,nz))
#             visited[nx][ny][nz] = visited[qx][qy][qz] + 1

#     return day


# 재혁님 답안
from collections import deque

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)] # 3차원 입력
visited = [[[int(1e9)] * n for _ in range(m)] for _ in range(h)] # 여러번 방문을 방지하기 위해 가장 큰 수로 초기화

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

# 얘도 어디부터 시작해야할지 정해야하고
# 방문 처리도 해줘야 함
# 이걸 여러번 수행해줘야 하므로 함수화 시키는게 좋음
def bfs(x,y,z):
    q = deque()
    q.append((x,y,z))
    visited[x][y][z] = 0

    while q:
        qx, qy, qz = q.popleft()

        for i in range(6):
            nx, ny, nz = qx + dx[i], qy + dy[i], qz + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
                continue
            # 이미 방문했었는데, 또 방문하는 것 방지 (각 visited 원소에 익은 날을 넣고 비교하기) >> 아니면 bfs에 파라미터로 count를 같이 넣어줘도 됨
            # 이미 토마토가 익은 날 수가 후순위로 올 날짜(nx,ny,nz)보다 작다
            if visited[nx][ny][nz] <= visited[x][y][z] + 1:
                continue
            # 빈칸이라면 넘어가기
            if graph[nx][ny][nz] == -1:
                continue
            
            visited[nx][ny][nz] = visited[x][y][z] + 1
            q.append((nx,ny,nz))

for i in range(m):
    for j in range(n):
        for k in range(h):
            # 익은 토마토면 > bfs 돌리기
            if graph[i][j][k] == 1:
                bfs(i,j,k)

ans = 0
for i in range(m):
    for j in range(n):
        for k in range(h):
            if visited[i][j][k] == int(1e9): # 방문 아예 안 했는데,
                if not graph[i][j][k]: #익지 않은 토마토 일 때
                    print(-1)
                    exit(0)
            else:
                max(ans, visited)
            