# 내일 다시한다.

n = int(input()) # 64,  2^31 == 10*9 

result = []
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 1. 4분 영역으로 쪼갠다. () 쪼갤 때 마다 () 안에 정보가 들어감
# 2. 해당 영역이 모두 같아질 때 까지 쪼갠다. >> 1의 과정 반복

# 어떻게 4분 영역으로 쪼갤까?
# 반복하면서 4분 영역 쪼개는 방법 >> 재귀

# 재귀하는 파라미터로, x,y와 길이 정보 n 을 준다.
# 재귀할 때 마다 영역 내 정보 같은 정보인지 check
# 각 영역을 탐색해야 하므로 4번의 재귀로 표현한다. (왼위, 오위, 왼아래, 오아래)

def check(x, y, n):
    one = 0 # 영역 내 1의 개수
    zero = 0 # 영역 내 0의 개수
    # 해당 영역내의 값이 모두 같은지 아닌지는 모두 여기서 판단
    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] == 0:
                zero += 1
            else:
                one += 1
    
    # 영역이 통일인지 체크
    if one == 0:
        print(0, end='')
    elif zero == 0:
        print(1, end='')
    # 아니라면 한 번더 재귀 탐색
    else:
        print('(', end='')
        n //= 2
        check(x, y, n) # 쪼개진 1사분면
        check(x, y + n, n) # 쪼개진 2사분면
        check(x + n, y, n) # 쪼개진 3사분면
        check(x + n, y + n, n) # 쪼개진 4사분면
        print(')', end='')

check(0,0,n)
        
