n = int(input())
my = {}
numb = list(map(int, input().split()))
for i in numb:
    if i in my:
        my[i] += 1
    else:
        my[i] = 1

m = int(input())
search = list(map(int, input().split()))
answer = []
for target in search:
    values = my.get(target) # get : dict의 value를 반환하는 함수, 없다면 None 반환
    if values == None:
        answer.append(0)
    else:
        answer.append(values)

print(*answer)