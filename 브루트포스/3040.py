# 숫자 9개가 들어 왔을 때, 7개만 택해서 100이 되도록 하려면 ?
# 우선 입력의 총합을 구하고, 총합 - 100의 값이 나오는 애들이 2개 거기 있다면 그걸 빼면 되지 않을까?


numb = []

for _ in range(9):
    numb.append(int(input()))

total = sum(numb)
diff = total - 100

a,b = 0, 0
switch = False
# diff가 나오는 2개 찾기
for i in range(8):
    for j in range(i+1,len(numb)):
        if numb[i] + numb[j] == diff:
            a,b = numb[i], numb[j]
            switch = True
    if switch: # 2중 for문 탈출하는 방법??
        break

for i in numb:
    if i != a and i != b:
        print(i)