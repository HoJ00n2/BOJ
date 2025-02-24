def backtrack(start, end, result, lotto):
    if len(result) == 6:
        print(*result, end="\n")
        return
    
    # 여기서 오름차순과 중복허용 안하면서 저장되도록 하려면?
    # for i in lotto:
    #     result.append(i)
    #     backtrack(result, lotto)
    #     result.pop()

    for i in range(start, end):
        result.append(lotto[i])
        # 시작 index를 넣어주어 해결!
        # backtrack 호출 할 때 마다 시작 index를 늘림
        # 이미 입력 자체가 오름차순이므로 뒤의 index부터 시작하면 자연스레 result에 오름차순으로 값 저장
        backtrack(i + 1, end, result, lotto) 
        result.pop()


while True:
    user_input = list(map(int, input().split()))

    test_case = user_input[0]
    lotto = user_input[1:]

    if test_case == 0:
        break
    
    result = []

    backtrack(0, test_case, result, lotto)
    print()