# 30분 시작

# 그리디의 문제 같음 + 정렬

# 어떻게 조합해야 최소 길이로 갈까?
# 무조건 고속도로 길이 D로 도착해야함
# 시작점, 도착점, 지름길 길이
# 도착점 - 시작점 (갭이 클수록), 지름길 길이는 작을수록
# 뭔가 회의실 배정처럼 짜여질 것 같음


n, d = map(int, input().split())

info = []

for _ in range(n):
    arr = list(map(int, input().split()))
    # 지름길이 더 긴 경우 넘어가기
    if abs(arr[1] - arr[0]) < arr[2]:
        continue
    info.append(arr)
    
# 정제된 정보 중 무엇을 기준으로 정렬할 것인가?
# 회의실처럼 우선 도착지가 작은순으로 정렬, 같다면 지름길 길이가 작은순으로 정렬?
info = sorted(info, key = lambda x : (-abs(x[1]- x[0] - x[2]), x[1]))
print(info)

result, now = 0, 0
for i in info:
    # 시작위치가 현재보다 앞에있다면 넘어가기 > 앞으로 가는 길중 지름길만 찾을 것이므로
    if i[0] < now:
        continue
    # 도착지가 고속도로 길이를 초과할 경우
    elif i[1] > d:
        continue
    
    # 다음 지름길까지는 직접 가기
    if now < i[0]:
        result += (i[0] - now)
        now = i[0]
    
    now = i[1]
    result += i[2]

# 지름길이 더이상 없는데 아직 고속도로 도착을 못 했다면
if now < d:
    # 지름길 없이 나머지 가기
    result += (d - now)
    
print(result)

# 0 + 100 + 260 + 10 + 15 + 40 + 9
# 360 + 35 + 49 = 84 + 360 = 454