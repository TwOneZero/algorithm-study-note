# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 정점의 개수 N과 간선의 개수 M
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2))

# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력

# 연결 요소의 개수

# 풀이 전략
# 간선의 최대 수가 N^2 에 가까우므로 -> 인접 행렬을 쓴다.
# dfs or bfs 로 풀기
# 노드(정점) 수와 같은 check 배열로
# 탐색이 종료되고 새 탐색 시마다 check 될 때마다 연결 요소 개수 +1 해줌
import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x - 1, map(int, sys.stdin.readline().split()))
    # 무방향이므로 다 저장
    adj[a][b] = adj[b][a] = 1

# for row in adj:
#     print(row)
ans = 0  # 연결 요소 개수
chk = [False] * N  # 체크 배열


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)
