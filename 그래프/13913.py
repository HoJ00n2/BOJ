# 48분 시작
# 최적의 길로 가는 경로를 어떻게 저장할까?
# 각 걸어온 경로를 저장하는 변수를 만들자 > history

from collections import deque

n, k = map(int, input().split())
INF = int(1e9)
visited = [[INF, 0] for _ in range(100001)]
time = 0

q = deque()
q.append((n, time))
visited[n][0] = time
result = [k]
while q:
    cur, t = q.popleft()
    # 찾았다면 (가장 빨리 k에 도착한 경우에만 해당)
    if cur == k:
        # 내가 갔던 경로들 역추적
        while cur > 0:
            # cur 이전에 어디서 왔는지 담겨있음
            cur = visited[cur][1]
            result.append(cur)  
        
    for nxt in [cur*2, cur+1, cur-1]:
        if nxt < 0 or nxt > 100000:
            continue            
        if visited[nxt][0] > t+1:
            q.append((nxt, t+1))
            visited[nxt][0] = t+1
            visited[nxt][1] = cur

    
print(visited[k][0])
# result에는 맨 마지막 0 담겨있어서 얘 뺴고, 역순으로 출력
# print(*result[::-1]) # *result[:-1:-1] 으로 하면 왜 안나오지? (탐색 순서가 우선순위인가?)
result = result[:-1]
print(*result[::-1])