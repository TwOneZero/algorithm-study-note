#피보나치 2

#재귀

# def f(n):
#   if n == 0:
#     return 0
#   elif n == 1:
#     return 1
#   return f(n-1) + f(n-2)

# print(f(int(input())))

#그냥 반복문
# n = int(input())
# prev = 0
# now = 1
# next_fibo = 0

# for _ in range(n-1):
#   next_fibo = now + prev
#   prev = now
#   now = next_fibo

# print(now)

#메모이제이션

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

def f(n):
  if cache[n] == -1 :
    cache[n] = f(n-1) + f(n-2)
  #구한 적 있으면 바로 반환
  return cache[n]

print(f(int(input())))