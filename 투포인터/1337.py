# 풀긴했는데, 뭔가 때려맞춘 느낌
# 완벽한 정립은 안됨

n = int(input()) # 50

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

result = []
for i in arr:
    count = 0
    for j in range(1,5):
        if i + j in arr:
            count += 1
    result.append(count)

print(4 - max(result))