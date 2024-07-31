# n, s = map(int, input().split())
#
# arr = list(map(int, input().split()))
#
# cnt = 0
# for i in range(len(arr)):
#     tot = 0
#     print(f'===START===')
#     for a in arr[i:]:
#         tot += a
#         print(f'tot-{tot}-s')
#         if tot == s:
#             cnt += 1
#             break
#     print(f'===END===')
# print(cnt)


from itertools import combinations

N, S = map(int, (input().split()))

cnt = 0
arr = list(map(int, input().split()))

for i in range(1, N+1):
    data = combinations(arr, i)
    for d in list(data):
        if sum(d) == S:
            cnt += 1

print(cnt)

