from itertools import combinations

import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

tot = list()
for combi in combinations(nums, 3):
    tot.append(sum(combi))

cnt = len(tot)
ans = 0

for t in tot:
    for i in range(2, t - 1):
        print(f'{t} % {i} = {t % i}')
        if t % i == 0:
            cnt -= 1
            break

print(cnt)
