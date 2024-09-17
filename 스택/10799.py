board = input()
result = 0

# ()는 반드시 레이저
# 찰린 막대기의 총 개수
# () 기준으로 아래 몇개의 막대기가 있는지 count
# () 기준으로 앞에 몇 개의 )만나지 않은 (가 있는지만 세면 될 듯

# (((()(()()))(())()))(()())
# 3 + 4 + 4 + 3 + 2 + (5) // 1 + 1 + 1
# (((()(()()))(())())) 의 경우 21이 나와야함
# 3 + 4 + 4 + 3 + 2 + (5) 끝나는 )의 개수

stack = []
for idx, i in enumerate(board):
    if i == ')':
        if board[idx-1] == '(': # 레이저인 경우
            result += len(stack) - 1 # 레이저는 카운트 x
        else: # 막대기의 끝인 경우
            result += 1 # 나머지
        stack.pop()
    else: # (일 때
        stack.append(i)


print(result)

