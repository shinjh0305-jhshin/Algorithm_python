import sys
Input = sys.stdin.readline
tc = int(Input())
nodes = 0
graph = []


def initialize():
    global graph, nodes
    nodes = int(Input())
    graph = [-1] * (nodes + 1)
    for _ in range(nodes - 1):
        x, y = map(int, Input().split())
        graph[y] = x


def operate():
    x, y = map(int, Input().split())

    # x가 root로 가기 전까지 거쳐가는 노드들을 전부 기록
    visited_x = set()
    while x != -1:
        visited_x.add(x)
        x = graph[x]

    # y를 root로 보내면서 확인
    while y not in visited_x:
        y = graph[y]
    print(y)


for _ in range(tc):
    initialize()
    operate()