n = int(input())

depth = 0 # 현재 몇 행이냐?
ans = 0 # 경우의 수

v1 = [0]*n # 현재 열에 둘 수 있는가?
v2 = [0]*(2*n-1) # 현재 오른쪽방향 대각선에 둘 수 있는가?
v3 = [0]*(2*n-1) # 현재 왼쪽방향 대각선에 둘 수 있는가?

def back(depth):
    global ans
    if depth == n:
        ans += 1
        return
    
    for j in range(n):
        # 현재 위치에서 열방향 왼쪽 대각선, 오른쪽 대각선 모두 둘 수 있다면
        if v1[j] == v2[depth + j] == v3[depth - j] == 0:
            v1[j] = v2[depth + j] = v3[depth - j] = 1 # 일단 두기
            back(depth+1) # 탐색하기
            v1[j] = v2[depth + j] = v3[depth - j] = 0
            
back(0)

print(ans)