import sys

# set으로 해도 시간초과 발생 -> 이것은 I/O 단에서 시간초과가 발생하여 sys.stdin.readline으로 불러오기
# Python의 input()은 느리기 때문에, 대량의 데이터를 처리할 때는 sys.stdin.readline()을 사용 O(N) -> O(1)로 I/O 단축
input = sys.stdin.readline  # 🔹 input()을 sys.stdin.readline으로 재정의, 근데 이건 "\n"까지 입력으로 받음

N, M = map(int, input().split())

memo = set()
for _ in range(N):
    memo.add(input().strip())  # 🔹 개행 문자("\n") 제거 후 추가

for _ in range(M):
    user_input = input().strip().split(",")  # 🔹 빠른 입력 처리

    for i in user_input:
        memo.discard(i)  # 🔹 존재하면 삭제 O(1)

    print(len(memo))  # 🔹 남은 키워드 개수 출력
