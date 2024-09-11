# 결국 모든 점들에 대한 최소거리 >> 플로이드 워셜 ?

n, m = map(int, input().split())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)] # min 비교를 통해 최소비용이 드는 거리로 이동할거라 INF로 설정

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0 # 자기 자신에 대한 거리는 0으로 초기화

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # 바로가기 vs 거쳐가기의 최소 비교

min_sum = INF
answer = 0
for i in range(1,n+1):
    row_sum = sum(graph[i][1:]) # 행의 합
    if row_sum < min_sum:
        min_sum = row_sum
        answer = i
print(answer)