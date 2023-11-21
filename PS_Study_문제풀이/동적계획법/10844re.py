# f(1) = 9
# + 8
# f(2) = 17
# + 16
# f(3) = 17 * 2 - 1 = 33
# + 32
# f(4) = 33 * 2 - 1 = 65
# a1 = 8
# a2 = 16
# a3 = 32

# f(n) = f(n-1) + 2a(n-1)

cache = [0] * 101
cache[0] = 0
cache[1] = 9
cache[2] = 17
cache[3] = 33

MOD = 1_000_000_000


# Top-down
def f(n):
    if cache[n] == 0:
        cache[n] = cache[n - 1] + (8 * 2 ** (n - 1)) + 1
        cache[n] %= MOD
    return cache[n]


print(f(int(input())))
