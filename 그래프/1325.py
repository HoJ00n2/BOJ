# 30분 초과 문제 제대로 이해해야 할 듯 바로 들어가니 논리가 막힘

# A가 B를 신뢰한다 : B만 해킹하면 A와 엮인애가 보너스!
# 이 때 가장 신뢰의 최상위 레벨을 찾으면 됨
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] # N+1행으로 선언
for i in range(M):
    A, B = map(int, input().split())

    # 내 위가 누군지를 정하면 될 듯? (누가 더 상위의 관계인지)
    graph[B].append(A)

q = deque()
level = [] # 각 노드의 최대 깊이 담음
# 모든 노드를 다 돌아본다.
for i in range(1,N+1):
    cnt = 0 # 전염 개수
    visited = [0] * (N+1) # 방문 행렬 돌 때 마다 초기화

    # 상위의 컴퓨터가 있다면
    if graph[i]:
        visited[i] = 1 # 첫 시작 점도 방문해야함
        cnt += 1 # 첫 시작점도 카운트
        for nxt in graph[i]:
            if not visited[nxt]:
                q.append(nxt) # 큐에 삽입
                visited[nxt] = 1
                cnt+=1
            
        # 큐가 빌 때 까지 탐색
        while q:
            next_node = q.popleft()
            for j in graph[next_node]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = 1
                    cnt += 1
                
    level.append(cnt)

max_cnt = max(level)
for i in range(N):
    if level[i] == max_cnt:
        print(i+1, end=" ")