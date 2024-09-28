# 8분 시작 > 21분 종료

# 23
# 32 32 > 32 16 16 > 32 16 8 8 > 32 16 8 4 4 > 32 16 8 4 2 2 > 32 16 8 4 2 1 1

# 일단 쪼개고 생각할까 ?
stick = [64] # 처음에 64로 두고 이후 계속 재귀적으로 넣어두기

x = int(input())

# stick이 1로 쪼개질 때 까지 반복
while stick[-1] != 1:
    half = stick[-1]//2

    # 처음에는 2번 삽입
    if len(stick) == 1:
        stick.append(half)
        stick.append(half)
    else:
        stick[-1] = half
        stick.append(half)

result = 0
if x in stick:
    print(1)
    exit(0)
else:
    for i in stick:
        if i > x:
            continue
        x -= i
        result += 1

print(result)