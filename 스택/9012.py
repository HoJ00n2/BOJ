# 18분

t = int(input())

for _ in range(t):
    test_input = list(map(str, input().rstrip()))

    stack = list()

    while test_input:
        value = test_input.pop(0)
        if value ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(value)
        else:
            stack.append(value)
            
    if stack:
        print('NO')
    else:
        print('YES')