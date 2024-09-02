from collections import deque

n = int(input())
m = int(input())

friend = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    friend[a].append(b)
    friend[b].append(a)
    

q = deque()
q.append((1,0)) # x와 cnt 넣기, cnt를 넣어줌으로써 자기 자신과 거리를 비교 (최대 2까지)
visited[1] = 1 # 자기자신은 방문처리
result = 0

while q:
    x, cnt = q.popleft()
    # 친구의 친구는 이미 cnt=1일 때 result +=1 하므로
    # 나와 거리 차이(cnt=2)가 나면 무시한다. 
    if cnt >= 2: 
        continue
    for i in friend[x]:
        if visited[i] == 0:
            visited[i] = 1
            q.append((i, cnt+1))
            result += 1

print(result)
    