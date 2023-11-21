import sys
from collections import deque

input = sys.stdin.readline

# 1000 * 1000 정도의 시간 복잡도

n, m = map(int, input().split())

arr = [input() for _ in range(n)]

dp = [[0] * m for _ in range(n)]

# 제일 왼쪽, 위 행과 열은 먼저 채워줌
for i in range(m):
    if arr[0][i] == '1':
        dp[0][i] = 1
for i in range(1, n):
    if arr[i][0] == '1':
        dp[i][0] = 1
    # (1,1) 부터 점화식 적용
    for j in range(1, m):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

ans = 0
for i in range(n):
    ans = max(ans, max(dp[i]))
# j for j in dp[i])
# 넓이 출력
print(ans**2)
