# 4분 시작
# 입력의 예시를 보니 배수 관계가 아니어도 됨 >> dp로 풀어야?

# 우선 예제가 어떻게 해당 정답이 되는지 도출해보기 (패턴을 도출하지 못함)

# dp 배열로 푼다는 가정하에
# 각 dp배열에는 각 값을 만들 수 있는 경우의 수가 담겨있다고 하면 될 듯?


t = int(input())

for _ in range(t):
    n = int(input())
    # 알아서 오름차순으로 입력
    coins = list(map(int, input().split()))

    m = int(input())

    dp = [0]*(m+1) # 각 값을 만들 수 있는 경우의 수가 담김 
    dp[0] = 1 # 0원을 만들 수 있는 경우는 무조건 1가지 (모든 동전을 안 쓸 때)
    for coin in coins:
        for money in range(coin, m+1): # 시작 동전부터 세도 상관없음 (어짜피 이전은 카운트 못하므로)
            if money >= coin: #  금액이 동전의 가치보다 크거나 같다면 (자기 자신도 포함)
                dp[money] += dp[money - coin]

    # n가지 동전으로 m을 만드는 모든 방법의 수
    print(dp[m])