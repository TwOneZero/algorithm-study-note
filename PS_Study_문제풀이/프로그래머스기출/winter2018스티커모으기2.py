from itertools import combinations


import sys
input = sys.stdin.readline

sticker = list(map(int, input().split()))


print(sticker[0:-1:2])
print(sticker[1::2])
first = sum(sticker[0:-1:2])
second = sum(sticker[1::2])

print(max(first, second))


