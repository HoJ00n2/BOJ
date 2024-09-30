# 초기 visited를 INF로 설정한 것 까진 좋았는데, 결국 얘도 다익스트라로..
# 왜냐면 일단 모든 노드로 가는 비용을 다 계산해야하기 때문
# 내가 간 곳에 대해서만 계산하면 이후 안 간 곳의 좌표가 더 작은 값이 나온 경우 돌아가는 상황 발생
# bfs는 간선사이의 거리가 1이어야 함 (가중치가 모두 동일해야함)
# 하지만 이것은 다음 칸 중 최소인 곳으로 가야하므로 (가중치가 모두 다름 >> 결국 모든 노드 다 뒤져서 비교) >> 다익스트라

import heapq

INF = 1e9
testcase = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# bfs의 탈을 쓴 다익스트라 실행
def bfs(x,y,testcase):
    heap = []
    visited[x][y] = graph[x][y]
    # cost 기준으로 min heap push
    heapq.heappush(heap, (graph[x][y], x, y))

    while heap:
        cost, hx, hy = heapq.heappop(heap)

        for i in range(4):
            nx, ny = hx + dx[i], hy + dy[i]
            # 범주내다.
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 방문이미 했다.
            if visited[nx][ny] != INF:
                continue
            # 다음으로 갈 수 있는 곳의 cost
            new_cost = cost + graph[nx][ny]
            # 갈 수 있는 곳 중 최소 cost로 이동
            if visited[nx][ny] > new_cost:
                visited[nx][ny] = new_cost

                # [n-1][n-1]에 도달했다면,
                if nx == ny == n-1:
                    print(f"Problem {testcase}: {visited[n-1][n-1]}")
                else:
                    heapq.heappush(heap, (new_cost, nx, ny))

while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    visited = [[1e9]*n for _ in range(n)]

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    bfs(0,0, testcase)

    testcase += 1