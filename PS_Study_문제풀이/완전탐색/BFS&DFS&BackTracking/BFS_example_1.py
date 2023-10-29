from collections import deque

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1
adj[3][7] = adj[3][8] = 1


def bfs():
    dq = deque()
    # 시작 노드
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                print(f'{now} -> {nxt}')
                dq.append(nxt)

bfs()
