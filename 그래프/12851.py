from collections import deque

n, k = map(int, input().split())

INF = int(1e9)
visited = [INF]*100001

# 최소 거리 출력은 같으나, 도달하는 방법 수가 추가 됨
q = deque()
way, time = [], 0
q.append((n, time))
visited[n] = time

while q:
    cur, t = q.popleft()

    for nxt in [cur*2, cur+1, cur-1]:
        if nxt < 0 or nxt > 100000:
            continue
        if visited[nxt] >= t+1:
            if nxt == cur*2:
                visited[nxt] = t+1
                q.appendleft((nxt, t+1))
            else:
                visited[nxt] = t+1
                q.append((nxt, t+1))
        # 동생을 찾았다면,
        if nxt == k:
            # 우선 찾았을 때의 시간 모두 담아둠
            way.append(t+1)
print(visited[k])
cnt = 0
# 반례 n==k일 때,  n이 1에서 시작할 때
if n != k:
    for i in way:
        if i == visited[k]:
            cnt += 1
    print(cnt)
else:
    print(cnt+1)