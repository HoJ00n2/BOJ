# 23분 시작 > 못 품 > 어떻게 부모-자식 관계를 정할지 감이 안왔음

from collections import deque
# "어느 쪽이 부모, 자식인지 모르는 연결된 정점 쌍들의 정보가 주어졌을 때, 이를 통해 트리를 구성하여 각 정점들의 부모를 알아내는 문제"
# 1. 링크드리스트로 풀기 2. n x n 그래프로 풀기
# 1번 방식이 좀 더 합리적
n = int(input())
vertices = [[] for _ in range(n+1)]  # 링크드 리스트 선언

# 또 하나 고려해야 할 것은, 두 정점 중 어느 쪽이 부모이고 자식인지 아직은 알 수 없습니다.
# 즉, 두 정점이 indirect하게 연결되어 있다는 의미입니다.
# indirect하게 연결된 두 정점 간의 연결 정보는 서로의 linked list에 둘 다 저장해주어야 합니다.

for _ in range(n-1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

# 따라서 루트인 1과 연결된 정점들은 반드시 부모가 1인 자식 노드들이 됩니다.
# 트리에서 루트를 제외한 모든 노드들은 하나의 부모만을 가집니다.
# 즉, 1의 자식이라고 밝혀진 정점들은 이미 부모가 있기 때문에, 이 정점과 연결된 다른 정점들은 모두 이들의 자식 노드일 수 밖에 없습니다.
# 이런 식으로, 1부터 시작하여 1의 자식인 정점들을 찾아내고 다시 이들의 자식인 정점들을 찾아가는 방식 으로 모든 정점들의 부모-자식 관계를 밝혀낼 수 있습니다.
parent = [0]*(n+1) # 각 노드의 부모를 기록하는 배열

q = deque()
q.append(1) # 1부터 시작해서 탐색 바로 만나는 애들은 1을 부모로 하는 자식임

while q:
    cur = q.popleft()
    # 현재 노드와 연결된 다른 노드로 이동
    for v in vertices[cur]: # dijkstra 느낌나네
        if parent[v] == 0: # 방문 안 했다면
            q.append(v)
            parent[v] = cur

# parent list의 2번째 요소부터 -> str화로한다. 엔터로 구분한다.
print('\n'.join(map(str, parent[2:])))