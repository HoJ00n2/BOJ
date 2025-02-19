N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

blue, white = 0, 0

def recur(x, y, n):
    color = graph[x][y]

    for i in range(n):
        for j in range(n):
            if color != graph[x + i][y + j]:
                n //= 2
                return (recur(x, y, n) + recur(x + n, y, n) + recur(x, y + n, n) + recur(x + n, y + n, n))
    
    return str(color)

answer = (recur(0, 0, N))

for i in answer:
    if i == "0":
        white += 1
    else :
        blue += 1
print(white)
print(blue)

