# 0 ~ 12 번의 노드가 트리로 주어졌을 때 코드로 DFS 구현하기

# 인접행렬로

adj = [[0] * 13 for _ in range(13)]
# 간선이 주어지면?
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1


# ...

# for row in adj:
#   print(row)

def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            print(f'{now} ---> {nxt}')
            dfs(nxt)


dfs(0)
