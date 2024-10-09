# 23분 시작 > 39분 종료 (입력땜에 생각함)
n = int(input())

queue = []

for _ in range(n):
    # 어떻게 해야 1개도 받고 2개도 받나?
    # 일단 1개만 받고 if에서 판단하자
    command = str(input())
    # 이렇게 받는게 더 좋은 방법!
    # command = input().split()
    # print(command)

    if command[:4] == 'push':
        queue.append(int(command[5:]))
    elif command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
