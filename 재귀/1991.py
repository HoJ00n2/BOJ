# 55분 시작 > 30분 초과

def preorder(node):
    print(node,end="")
    # 왼쪽 자식 존재한다면
    if tree[node][0] != ".":
        preorder(tree[node][0])
    if tree[node][1] != ".":
        preorder(tree[node][1])

def inorder(node):
    if tree[node][0] != ".": 
        inorder(tree[node][0])
    print(node, end="")
    if tree[node][1] != ".":
        inorder(tree[node][1])

def postorder(node):
    if tree[node][0] != ".": 
        postorder(tree[node][0])
    if tree[node][1] != ".":
        postorder(tree[node][1])
    print(node, end="")


n = int(input())

tree = {}
for i in range(n):
    # 항상 A가 루트노드라는 조건이 있음
    root, left, right = map(str, input().split())
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')