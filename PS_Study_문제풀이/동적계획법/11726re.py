# 1 X 2 타일 : a (a 는 무조건 2의 배수로 있어야함)
# 2 X 1 타일 : b
# 2 X N -> N 이 홀수일 때 : b 홀수
#          N 이 짝수일 때 : b 짝수
#
# 2  X  5 -> 4a  +  b
#         -> 2a  + 3b

# 마지막 타일이 세로하나 타일  or 가로두개타일 인지
# f(n) : 완성한 타일의 가로길이 가 N 일 때 경우의 수
# f(n) -> f(n-1) X 1
# f(n) -> f(n-2) X 1
# f(n) -> f(n-1) + f(n-2)


cache = [-1] * 1001
cache[0] = 0
cache[1] = 1
cache[2] = 2

MOD = 10_007


# Top-down
def f(n):
    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)
        cache[n] %= MOD
    return cache[n]


print(f(int(input())))

# Bottom-up 반복문
# N = int(input())
# # 미리 다 계산해놓기
# for i in range(2, N + 1):
#     cache[i] = cache[i - 1] + cache[i - 2]
#
# print(cache[N])
