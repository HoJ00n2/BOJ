N = int(input())
file_dict = {}

for _ in range(N):
    file_name = input().split(".")
    if file_name[1] in file_dict:
        file_dict[file_name[1]] += 1
    else:
        file_dict[file_name[1]] = 1

# dict 정렬
# file_dict = sorted(file_dict, key = lambda x : x) # 이렇게 해야 key 기준 오름차순 > 근데 반환은 list임
# file_dict = sorted(file_dict, key = lambda x : file_dict[x]) # 이렇게 하면 value 기준 오름차순
sorted_file_dict = sorted(file_dict.items())  # (key, value) 튜플을 사전순 정렬 > 이렇게 해도 됨

for i in sorted_file_dict:
    print(i[0], i[1])