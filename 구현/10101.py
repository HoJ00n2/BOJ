# 좀 더 그럴 듯하게 풀순 없었을까? 생각해보기

angle = []

for _ in range(3):
    angle.append(int(input()))

cnt = 0
angle.sort(reverse=True)
first = angle[0]

if sum(angle) == 180:
    for i in angle[1:]:
        if i == first:
            cnt += 1
    if cnt == 2:
        print("Equilateral")
    elif cnt == 1:
        print("Isosceles")
    elif cnt == 0:
        print("Scalene")
else:
    print("Error")