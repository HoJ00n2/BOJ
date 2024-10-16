# 27분 시작 >> 30분 초과

test = int(input())

def calcul(final):
    # print("final", final)
    num = 0
    result = 0
    oper = 1
    for i in final:
        if i.isdigit():
            num = num*10 + int(i)
        else:
            result += num * oper
            num = 0 # num 초기화
            if i == "+":
                oper = 1 # 덧셈
            else:
                oper = -1 # 뺄셈
    # 나머지 숫자 연산
    result += num * oper
    # print(result)
    if result == 0:
        return True
    else:
        return False

def back(arr, depth):
    global n
    global answer
    arr.append(str(depth))

    if depth == n:
        str_arr = ''.join(arr)
        final = str_arr.replace(" ","") # 공백 붙이기
        if calcul(final):
            # print(str_arr)
            answer.append(str_arr)
        return
    
    for i in ["+", "-", " "]:
        arr.append(i)
        back(arr, depth+1)
        arr.pop() # 숫자 제거
        arr.pop() # 연산자 제거

for _ in range(test):
    n = int(input())
    arr = []
    answer = []
    back(arr, 1)
    
    # 아스키 순으로 정렬
    answer.sort()
    for ans in answer:
        print(ans)

    print()