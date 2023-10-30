# 메모이제이션 없이
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n - 1) + f(n - 2)
# print(f(int(input())))

cache = [-1] * 91
cache[0] = 0
cache[1] = 1

# Top-down
# def f(n):
#     if cache[n] == -1:
#         cache[n] = f(n - 1) + f(n - 2)
#     return cache[n]
#
#
# print(f(int(input())))


# Bottom-up 반복문
N = int(input())
# 미리 다 계산해놓기
for i in range(2, N + 1):
    cache[i] = cache[i - 1] + cache[i - 2]

print(cache[N])
