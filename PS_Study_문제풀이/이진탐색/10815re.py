import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
my_card = sorted(list(map(int, input().split())))

M = int(input())
looking_card = list(map(int, input().split()))
ans = []

for q in looking_card:
    l = bisect_left(my_card, q)
    r = bisect_right(my_card, q)
    # 찾는 수가 없으면, l = r  임
    ans.append(1 if r - l else 0)

print(*ans)
# print(' '.join(map(str, ans)))

# lo = 0
# hi = len(my_card) - 1
# mid = (lo + hi) // 2
# def is_found(mid, l):
#     return 1 if mid == l else 0


# def look_up(card):

#
#
# for l in looking_card:
#     while lo <= hi:
#         print(f'lo: {lo}  , mid: {mid}  , hi: {hi}  , ans: {ans}')
#         mid = (lo + hi) // 2
#         if is_found(my_card[mid], l):  # 예산이 가능한 범위라면 -> lo 를 mid 로 늘림
#             nxt_idx = mid
#             ans.append(1)
#             break
#         else:  # 불가능이면 hi 를 mid 로 낮춤
#             hi = mid - 1
#             ans.append(0)
#
# for a in ans:
#     print(a, end=" ")
