# 27분 시작 > 34분 종료
# +1, -1은 가중치가 같음 (1초), 근데 텔레포트만 0초로 가중치가 다름
# 이렇게 다 맞는데 1개만 가중치가 다른 경우 bfs를 쓸건데 텔레포트에 대해서만 appenleft 하여 빠르게 삽입

from collections import deque

n, k = map(int, input().split())

INF = int(1e9)
visited = [INF]*100001

q = deque()
time = 0
q.append((n, time))
visited[n] = time

while q:
    cur, t = q.popleft()
    
    for nxt in [cur*2, cur+1, cur-1]:
        if nxt < 0 or nxt > 100000:
            continue
        if nxt == cur*2:
            if visited[nxt] > t:
                q.appendleft((nxt,t))
                visited[nxt] = t
        else:
            if visited[nxt] > t+1:
                q.append((nxt, t+1))
                visited[nxt] = t+1

print(visited[k])
                              
