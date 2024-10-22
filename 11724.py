# 45분 시작
# 결국 모든 노드를 이었을때, 안 끊어진 연결관계가 총 몇개냔 뜻
# 다 이어졌다면 1
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
group = 1
for i in range(1,n+1):
    # 방문 안했고, 다음노드가 있다면
    if graph[i] and visited[i] == 0:
        q.append(i)
        visited[i] = group
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if visited[nxt] != 0:
                    continue
                q.append(nxt)
                visited[nxt] = group
        group += 1
print(max(visited))
    
