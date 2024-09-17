# 이건 볼 때마다 어떻게 풀어야할지 감이 안 옴 >> 정확히는 내가 생각한게 어떻게 증명이 될까? >> 이건 np hard 유형
# 이런 유형은 항상 풀이도 일정 : 예로 시간이 나오고 들어갈 수 있는 최대 회의 개수 묻는 유형
# 어떻게 푸냐면.. 끝나는 시간 기준으로 오름차순을 하고 
# 확정된 회의의 끝나는 시간에 바로 가까운 시작 시간의 회의 시간을 넣는 방식으로


# 회의 시간이 주어졌을 때, 회의 실 1개에서 할 수 있는 최대 회의 개수
# 시간을 2^31 -1 로 준 이유 ?? >> int형으로 하라고 명시하는 것 (다른 언어인 경우..)

n = int(input()) # 회의 개수 10만 > 2중 for문은 가능 x >> n^2이 10^9가 되는지 안되는지 체크하기

meeting = 0
time_table = []
confirmed_start = [] # 확정된 회의 시간 담는 배열

for _ in range(n):
    start_time, end_time = map(int, input().split())
    time_table.append((start_time,end_time))
    

# 오래 걸리는 회의를 무조건 거르냐? >> 변수가 있을 듯함

# 안 겹치는 회의를 먼저 넣냐? >> 어짜피 안 겹치므로 영향 x
# 일단 안 겹치는 회의를 먼저 넣어보자 >> 넣었다면 시간표에서 빼버리기
time_table = sorted(time_table) # 아마 (a,b) a가 오름 차순인 대로 정렬

for i in range(n-1):
    # 시간이 겹친 다면 pass
    if time_table[i][1] > time_table[i+1][0]:
        pass
    else:
        meeting += 1 # 회의에 넣기
        confirmed_start.append(time_table[i][0]) # 이후 비교에 사용 위함
        del time_table[i] # 회의에 넣었으므로 시간표에서 튜플 삭제

# 마지막 요소에 대해서 check
if time_table[-2][1] <= time_table[-1][0]:
    meeting += 1
    confirmed_start.append(time_table[-1][0])
    del time_table[-1]

print(time_table)
# 일단 안 겹치는 회의는 넣었고, 나머지에선 어떻게 판단할까?
# 일단 너무 긴 회의부터 삭제하고, 삭제 했을 때 안겹치는 회의를 넣는다?

# 사실 예제도 4개가 될 답은 다양하게 존재하는데
# (1,4), (5,7), (8,11), (12,14)로 한 것은 얘네가 가장 각각의 회의 시간도 적기 때문
# 그러므로 많은 시간 걸리는 애들을 거르는게 좋을 듯?

for i in time_table:
    for j in confirmed_start:
        if i[1] > j:
            del i