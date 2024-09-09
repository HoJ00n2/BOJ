# 어떻게 4 2 3 1 의 최소가 19가 될까?
# 4 3 3 3 > 4 3 6 6
# 결국 매 m번 시행 마다 가장 작은 top2를 고르면 되는거 아닌가 ?
# 근데 이거 시간초과 날 것 같은데? m * (card list sort) == 15000 * 1백만

n, m = map(int, input().split()) # 1000, 15000
card = list(map(int, input().split())) # 1백만

# 매 m번 시행마다
for _ in range(m):
    
    # sort 안하고 어떻게 최소 top2를 찾을까?
    # 자체 sort는 퀵소트라 o(n)보다 작으니 안걸릴라나? >> 안 걸림
    card.sort()
    
    summed_card = card[0] + card[1]
    card[0], card[1] = summed_card, summed_card

print(sum(card))