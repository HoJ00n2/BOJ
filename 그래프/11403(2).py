# 20분 시작 > 43분 종료
# 가중치가 없는 방향그래프 

n = int(input())
INF = 1e9
dist = [[INF]*n for _ in range(n)] # 모든 거리 INF로 초기화

# 자기 자신에 대한 거리는 초기화 필요 x
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             dist[i][j] = 0

# 입력
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            dist[i][j] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            # 바로 갈순 없지만(=dist[i][j]), 거쳐 갈 수는 있는 경우(=dist[i][k] + dist[k][j]) ==>> i => j로 가는 경로가 있다! 
            if dist[i][j] > (dist[i][k] + dist[k][j]):
                dist[i][j] = 1

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            dist[i][j] = 0

for i in range(n):
    print(*dist[i])
