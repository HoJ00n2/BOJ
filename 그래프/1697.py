# 39분 시작 >> fail

# 1차원 BFS의 기본적인 문제
# 1차원의 BFS [0 ~ 10만]
# 1칸 앞,뒤 x2 지점을 탐색 >> 여기에서 bfs 써야겠다는 것을 느껴야
# 현재 x => [x-1, x+1, x*2] 가 동시에 같은 가중치를 가지므로
# bfs 라는 것을 느끼는게 1번째 포인트

# x*2를 어떻게 처리해야 하는가 설정하는게 2번째 포인트 (특이치)
# 다른 것에 비해 크게 왔다갔다 하는 값
# 이런 경우 queue에 가장 먼저 특이치를 삽입하는게 특징 (이런 애가 원하는 조건을 달성할 가능성이 높기 때문) by appendleft
# visited에서 방문 쳌 & 거리 -> 최소 값이 담기려면 어떤 값과 비교해도 최소가 담기도록 하는 큰 값을 미리 초기화 (INF)
# 범주 내 check, (방문 여부 check by visited[i] >= visited[x+1 or x-1 or x*2]

from collections import deque

n, k = map(int, input().split())

INF = int(1e9) # int 안 하면 실수 오차 생길 수 있음
visited = [INF] * 100001

if n < k:
    time = 0
    q = deque()
    q.append((n, time))
    visited[n] = time

    while q:
        cur, t = q.popleft()

        for nxt in [cur*2, cur-1, cur+1]:
            # 범주 내라면
            if 0 > nxt or nxt > 100000:
                continue
            # 방문했냐 & 더 최소로 갈 수 있냐?
            if visited[nxt] > t+1:
                if nxt == cur*2:
                    q.appendleft((nxt, t+1))
                    visited[nxt] = t+1
                else:
                    q.append((nxt, t+1))
                    visited[nxt] = t+1

    print(visited[k])

elif n == k:
    print(0)
else:
    print(abs(n-k))