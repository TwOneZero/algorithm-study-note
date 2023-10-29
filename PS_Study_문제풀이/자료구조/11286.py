#
# import heapq as hq
# import sys
#
# pq = []
#
# for _ in range(int(input())) :
#   x = int(sys.stdin.readline())
#   if x:
#     #튜플로 저장
#     hq.heappush(pq, (abs(x), x))
#   # x = 0
#   else:
#     if pq :
#       print(hq.heappop(pq)[1])
#     else:
#       print(0)


# 배열에서 가장 작은 값 출력 -> min-heap 이용

import heapq as hq
import sys

pq = []

for _ in range(int(input())):
    n = int(sys.stdin.readline())  # 숫자 입력 받기
    if n:  # n is not 0
        # 튜플로 절댓값과 원본을 저장
        hq.heappush(pq, (abs(n), n))
    else: # n is 0
        if pq:
            print(hq.heappop(pq)[1])
        else:
            print(0)
