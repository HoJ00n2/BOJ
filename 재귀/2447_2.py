# 문제를 봤을 때 3분할로 생각하자
# 상단 ***
# 중단 * *
# 하단 ***
# 그리고 이전 패턴의 반복으로 다음 패턴을 채워 넣음
# 예로 9의 패턴을 하기 위해선 3의 패턴결과를 알아야하고, 27의 패턴을 위해선 9의 패턴결과를 알아야함

N = int(input())

# 결과 저장할 N x N 배열 초기화
graph = [[" " for _ in range(N)] for _ in range(N)]

def backtrack(x, y, pattern):
    # 3의 패턴 어떻게 저장 or 출력할까? (재활용을 해야하는데)
    if pattern == 1:
        graph[x][y] = "*"
        return

    new_pattern = pattern // 3

    # 3 x 3 패턴에 대한 별 채우기
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            # 3 x 3 패턴을 start index (x, y)에 채워넣기 
            # 이 때 i=j=1일 때는 패스하므로, 중간패턴이 사라짐
            # 이게 1x1 빈칸, 3x3빈칸, 9x9빈칸이 되는 이유는 new_pattern 때문 (9일 때의 1,1 구하고, 3일 때의 1,1을 구함함)
            backtrack(x + i * new_pattern, y + j * new_pattern, new_pattern)

backtrack(0, 0, N)

for i in range(N):
    print(''.join(graph[i]))