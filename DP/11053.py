n = int(input())

arr = list(map(int, input().split()))

# 나보다 앞에서 시작한 애들이 나(i) 까지 왔을 때 부분 수열이 가능한 경우의 수가 담김
# = dp[i]  :  arr[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이
# 경우의 수면 자기 자신은 무조건 부분 수열이므로 1로 초기화
dp = [1] * n 

for i in range(len(arr)):
    cnt = 0 # i와 증가하는 부분 수열이 가능한 경우의 수가 담김
    for j in range(i):
        # 나보다 앞쪽에 있는애가 더 작다면,
        # 적어도 j에서 시작한 애는 i와 증가하는 부분수열을 이루는 경우의 수가 됨
        if arr[i] > arr[j]:
            # if 조건을 만족하므로 dp[i]에 들어갈 값은
            # 이전까지 경우의 수를 쌓아왔던 dp[j]에 + 1만 해주면 됨
            # 근데 앞에 있는 여러 j 중 가장 경우의 수가 많은 놈으로 업뎃하면 됨
            # 어짜피 arr[i] > arr[j] 니까
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))