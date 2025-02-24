# def backtrack(start, comb):
#     # 6개의 숫자를 선택했으면 출력
#     if len(comb) == 6:
#         print(" ".join(map(str, comb)))
#         return # 이전 단계로 회귀

#     # 현재 인덱스부터 끝까지 순회하며 숫자 선택
#     for i in range(start, k):
#         # 이렇게 한 이유는 오름차순으로 구현하기 위함함
#         backtrack(i + 1, comb + [S[i]])

arr = []

def backtrack(depth, start, k, S):
    if depth == 6:
        print(*arr)
        return
    
    # 이렇게 하면 백트래킹은 되는데, 오름차순이 안되고 중복도 들어감 
    # for i in range(k):
    #     arr.append(S[i])
    #     backtrack(depth + 1, k, S)
    #     arr.pop()

    # 위 문제를 해결하기 위해 다음과 같이 변경
    for i in range(start, k):
        arr.append(S[i])
        backtrack(depth + 1, i + 1, k, S)
        arr.pop()

while True:
    user_input = list(map(int, input().split()))
    if user_input[0] == 0:
        break

    k = user_input[0]
    S = user_input[1:]    # 결과 출력
    backtrack(0, 0, k, S)
    print()  # 테스트 케이스 구분을 위한 개행
