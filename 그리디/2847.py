n = int(input())

result = 0
point = []

for _ in range(n):
    p = int(input())
    point.append(p)
    
# 어짜피 최종기준은 맨 마지막 level이므로 역탐색을 하면 될 듯?
temp = point[-1] # 비교기준
for i in range(len(point)-2, -1, -1):
    if temp > point[i]: # 다음 레벨 클리어 점수가 현재 레벨 클리어 점수보다 높을 때 >> 조정 필요 x
        temp = point[i] # 여기도 바꿔줘야 다음 for loop에도 기준이 바뀜
        continue
    else: # 현재 레벨 클리어 점수가 다음 레벨 클리어 점수보다 높을 때 >> 조정 필요
        result += (point[i] - temp + 1) # 조정 횟수만큼 정답 count, 같은 경우에도 빼야하므로 최소 + 1 보장
        point[i] = temp - 1 # 조정된 점수는 최소만 바꿔줌
        temp = point[i] # 비교기준 바꾸기
    
print(result)