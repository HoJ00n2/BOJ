t = int(input())

for _ in range(t):
    n = int(input())
    
    # 날 별 주식가격
    price = list(map(int, input().split())) # 최대길이 100만
    
    # max_idx를 하면 안되는게 max값이 여러 날인 경우가 문제 ex) 9 1 1 9
    # 앞 -> 뒤로 탐색하면 새로운 max찾느라 시간초과 나므로 뒤집자 (미래를 본다 == 뒤집자)
    price.reverse()
    max_price = price[0]
    interest = 0 # 이익
    # 0은 이미 박았으니까 1번째 idx부터 탐색
    for i in range(1, len(price)):
        # max_price보다 작다면 무조건 사기
        if price[i] < max_price:
            interest += max_price - price[i]
        else:
            max_price = price[i]
            
    print(interest)