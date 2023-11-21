import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
INF = 987654321
graph = [[] for _ in range(N)]

for i in range(M):
    s, f = map(lambda x: x - 1, map(int, input().split()))
    graph[s].append(f)
    graph[f].append(s)

kevin = []


def bfs(start, end):
    check = [False] * N
    check[start] = True

    dq = deque()
    dq.append((start, 0))
    while dq:
        now, dist = dq.popleft()
        if now == end:
            return dist
        # 현재까지의 관계 수
        nd = dist + 1
        for nxt in graph[now]:
            if not check[nxt]:
                check[nxt] = True
                dq.append((nxt, nd))


def get_kevin(start):
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)
    return tot


for i in range(N):
    kevin.append(get_kevin(i))

print(f'kevin: {kevin}')

ans = (-1, INF)
for i, v in enumerate(kevin):
    if ans[1] > v:
        ans = (i, v)

print(ans)
