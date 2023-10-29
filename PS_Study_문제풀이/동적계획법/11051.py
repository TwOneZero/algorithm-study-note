# import sys
# sys.setrecursionlimit(10 ** 7)

MOD = 10007

N, K = map(int, input().split())

#메모이제이션
cache = [[0] * 1001 for _ in range(1001)]

#Top-down
# def bino(n, k):
#   if cache[n][k]:
#     return cache[n][k]
#   if k == 0 or k == n :
#     cache[n][k] = 1
#   else :
#     cache[n][k] = bino(n-1,k-1) + bino(n-1, k)
#     cache[n][k] %= MOD
#   return cache[n][k]

# print(bino(N,K))


#Bottom-up
for n in range(N + 1):
  cache[n][0] = cache[n][n] = 1
  for k in range(1, n):
    cache[n][k] = cache[n-1][k-1] + cache[n-1][k]
    cache[n][k] %= MOD

print(cache[N][K])