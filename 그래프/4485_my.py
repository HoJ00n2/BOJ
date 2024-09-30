# 10분 시작
# 초기 visited를 INF로 설정한 것 까진 좋았는데, 결국 얘도 다익스트라로..
# 왜냐면 일단 모든 노드로 가는 비용을 다 계산해야하기 때문
# 내가 간 곳에 대해서만 계산하면 이후 안 간 곳의 좌표가 더 작은 값이 나온 경우 돌아가는 상황 발생
# bfs는 간선사이의 거리가 1이어야 함 (가중치가 모두 동일해야함)
# 하지만 이것은 다음 칸 중 최소인 곳으로 가야하므로 (가중치가 모두 다름 >> 결국 모든 노드 다 뒤져서 비교) >> 다익스트라

from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    rupee = 0

    q = deque()
    q.append((x,y))
    visited[x][y] = graph[x][y]
    rupee += graph[x][y]

    while q:
        qx, qy = q.popleft()
        min = 1e9
        final_x, final_y = 0, 0
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            # 범주 내 아니라면
            if nx < 0 or ny < 0 or nx >= n or ny >=n:
                continue
            # 방문 했다면
            if visited[nx][ny] != 1e9:
                continue
            # 미리 다음에 갈 값들을 넣어둠
            visited[nx][ny] = visited[qx][qy] + graph[nx][ny]
            
            if visited[nx][ny] < min: # 최소값이 언제인지 저장
                min = visited[nx][ny]
                final_x, final_y = nx, ny

        # 여기서 최소인 곳으로 이동
        rupee += graph[final_x][final_y]
        if final_x == final_y == n-1: # 도착 좌표에 왔다면
            return rupee
        else:
            q.append((final_x, final_y))

while True:
    testcase = 1
    n = int(input())

    graph = []
    visited = [[1e9]*n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    result = bfs(0,0)

    print(f"Problem {testcase}: {result}")
    testcase += 1

