# 조합 라이브러리 안쓰고 풀기
# M = []
# for _ in range(9):
#     M.append(int(input()))
# M.sort()
#
# total = sum(M)
#
#
# # 두 번 돌면서 두개를 뺏을 때 나머지 합이 100인 경우
# def solution():
#     for i in range(8):
#         for j in range(i + 1, 9):
#             if total - M[i] - M[j] == 100:
#                 for k in range(9):
#                     if k != i and k != j:
#                         print(M[k])
#                 return
# solution()

# combi 사용
from itertools import combinations

h = []
for _ in range(9):
    h.append(int(input()))
h.sort()

# 7개 뽑아서 합이 100인지 확인
for combi in combinations(h, 7):
    if sum(combi) == 100:
        for h in sorted(combi):
            print(h)
        break
