def recur(cantore, start, end):
    if end - start == 1:
        return
    
    # 3등분 된 덩어리
    new_length = (end - start) // 3
    # 중간 왼쪽
    mid_start = start + new_length
    # 중간 오른쪽
    mid_end = mid_start + new_length

    for i in range(mid_start, mid_end):
        cantore[i] = " " # list slicing은 저장 안되고 새로운 배열이 생성됨! (주의)
    
    # 중간 왼쪽 재귀 탐색
    recur(cantore, start, mid_start)
    # 중간 오른쪽 재귀 탐색
    recur(cantore, mid_end, end)

        

while True:
    N = int(input())
    result = ["-"] * (3**N)
    recur(result, 0, 3**N)
    print("".join(result))