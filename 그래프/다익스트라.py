import heapq
import sys
input = sys.stdin.readline().rstrip
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF]*(n+1)

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) # 출발지, 도착지, cost
    graph[a].append((b,c)) # a에서 b로가는 비용이 c

def dijkstra(start):
    q = []
    # 시작 노드 자신에 대한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start)) # 큐 list에 (cost, 시작점)을 넣고 우선순위큐로 만듦
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위큐 q의 맨 앞부분 pop
        # 이미 처리된 노드라면 pass
        if distance[now] < dist: # 우선순위큐 방식으로 처리하므로 distance에 있는 각 노드 최단거리는 이미 갱신된거라 이후는 방문된것
            continue
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]: # i는 now와 인접한 노드정보 (인접 노드, cost)
            cost = dist + i[1] # dist는 현재 노드까지의 최단거리, i[1]은 현재노드에서 인접노드까지의 거리
            # 최소 비교 (새로 갱신된 거리 vs 기존 최단거리)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# start에서 다른 점으로 가는 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

print(f"dijkstra distance: {distance}")