import sys
sys.setrecursionlimit(10**7)


MOD = 10007
cache = [0] * 1001
n = int(input())

cache[1] = 1
cache[2] = 2

#Top-down
# def f(n) :
#   if cache[n] == 0 :
#     cache[n] = f(n-1) + f(n-2)
#     cache[n] %= MOD


#   return cache[n]

# print(f(n))

#Bottom-up

for i in range(3, 1001):
  cache[i] = cache[i-1] + cache[i-2]
  cache[i] %= MOD

print(cache[n])