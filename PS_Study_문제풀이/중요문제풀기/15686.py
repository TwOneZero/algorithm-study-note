
from itertools import combinations


houses  = []
chikens = []

N , M = map(int, input().split())


# N * N 배열
for y in range(N):
  for x, v in enumerate(map(int, input().split())):
    if v == 1 :
      # 좌표 튜플로 저장
      houses.append((y, x))
    elif v == 2 :
      chikens.append((y, x))



#최대로 먼 거리로 초기화
ans = 2 * N * len(houses)

for combi in combinations(chikens, M) :
  print(combi)

