import sys

sys.setrecursionlimit(10 ** 6)


# 1. 인접행렬담기
# 2. check 배열을 만들어서 방문하지 않은 노드를 만나면 탐색시작 and count  + 1

# dfs 로 풀어보자
def dfs(now):
    for nxt in range(N):
        # 방문 체크
        if adj[now][nxt] and not is_visit[nxt]:
            is_visit[nxt] = True
            dfs(nxt)


# 정점 , 간선
N, M = map(int, input().split())
# 인접 행렬 초기화
adj = [[0] * N for _ in range(N)]

# 방문체크 배열 초기화
is_visit = [False] * N
# 연결 요소 개수
count = 0

for _ in range(M):
    u, v = map(lambda x: x - 1, map(int, sys.stdin.readline().split()))
    # 무방향 그래프
    adj[u][v] = adj[v][u] = 1

for i in range(N):
    if not is_visit[i]:
        count += 1
        is_visit[i] = True
        dfs(i)

print(count)
