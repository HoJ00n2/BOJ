# 16분 시작 > 32분 종료

# 1 ~ N까지 중복없이 M개를 고른 수열
# 고른 수열은 오름차순
# 중복 불가

n, m = map(int, input().split())

depth = 0
arr = []

def back(depth):
    if depth == m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        # arr가 비어있을 때
        if len(arr) == 0: 
            arr.append(i)
            back(depth+1)
            arr.pop()
        else: # arr가 뭐라도 있을 때
            if i not in arr and arr[-1] < i: # arr 요소와 중복이 아니며 오름차순인 것만 뒤에 넣는다.
                arr.append(i)
                back(depth+1)
                arr.pop() # 이후 요소에 대한 pop
                
    
back(depth)