# 22분 시작 > 29분 완료
n = int(input())

coord = []
for _ in range(n):
    coord.append(list(map(int, input().split())))

# lambda sort
coord = sorted(coord, key = lambda x: (x[1], x[0]))

for i in range(n):
    print(*coord[i])