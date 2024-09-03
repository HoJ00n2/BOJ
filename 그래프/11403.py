# 문제 예시부터 이해가 잘 안가네..
# https://velog.io/@yoopark/baekjoon-11403

# 플로이드 와샬 알고리즘을 이용하는 문제
# 모든 정점을 탐색 할 때 유용
# 주로 DP 형태로 식이 구성되며, 3중 for문으로 짠다.
# 모든 정점간의 최소 거리를 구할 때 사용되며, 음수 가중치일 때도 사용 가능

# 왜 플로이드를 쓰냐?
# 모든 정점 (i,j)에 대해서 i -> j로 가는 경로가 있는지 없는지 구하라고 했기 때문
# 주의할 점은 바로 i->j로 간다는게 아니고 중간을 거쳐서 가더라도 갈수만 있으면 되는 것임!

# 어떻게 플로이드를 적용?
# 입력 그래프를 바탕으로 이어지지 않은 (=0)인 부분을 경로가 없다는 의미로 두기 위해 큰 수로 대체
# 이 후 플로이드 알고리즘을 통해 1~n 번째 정점을 순차적으로 모두 탐색하며 값을 갱신
# 마지막으로 출력 시 큰 수의 값이면 0, 아니면 1로 대체

# 예시에 대한 이해는 직접 노드 연결관계를 그려야지 이해가 가능함

n = int(input())

input_graph = []

# input graph 생성
for _ in range(n):
    row = list(map(int, input().split()))
    input_graph.append(row)

for k in range(n):
    for i in range(n):
        for j in range(n):
            # i에서 k를 거쳐서 j로 갈 수 있다면 (i -> k) = 1 and (k -> j) = 1
            if input_graph[i][k] and input_graph[k][j]:
                input_graph[i][j] = 1 # 도착했으니 연결관계 1로 해주기

for row in input_graph:
    print(*row)
