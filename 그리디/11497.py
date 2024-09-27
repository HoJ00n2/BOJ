# 그리디 + 정렬 (그리디문제는 주로 다른 유형들과 혼합되어 나온다)
t = int(input())

for _ in range(t):
    n = int(input())
    height = sorted(list(map(int, input().split())))

    # 트리 구조처럼 만들면 최소 차이가 나지 않을까..
    # 내림차순으로 루트의 자식들을 구성하면?
    # 피라미드 처럼 좌,우 양방향에서 가운데로 갈수록 큰 값으로 만들 수가 있나? >> 가능 함! (방법 숙지하기)
    #print(height) # [10, 10, 11, 11, 12, 12, 13]
    #print(height[::2]) # 짝수 인덱스만 (0,2,4 ...) 오름차순으로 뽑아오기 : [10, 11, 12, 13]
    #print(height[1::2][::-1]) # 홀수 인덱스만 (1,3,5 ...) 내림차순으로 뽑아오기 : [12, 11, 10]
    
    # 이렇게 2개를 더해주면 피라미드 형식으로 리스트를 만들 수 있다!
    pyramid = height[::2] + height[1::2][::-1]

    # 피라미드 구조에서 인접 최대값 반환
    max_diff = max(abs(pyramid[i] - pyramid[i-1]) for i in range(n))
    
    print(max_diff)
    