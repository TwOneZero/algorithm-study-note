from itertools import combinations

N, M = map(int, input().split())

house = []
chicken = []

for i in range(N):
    for j, val in enumerate(map(int, input().split())):
        if val == 1:
            house.append((i, j))
        elif val == 2:
            chicken.append((i, j))
# 문제에서 나올 수 있는 최대보다 높게 설정
ans = 2 * N * len(house)


def get_dist(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])


for combi in combinations(chicken, M):
    tot = 0
    for h in house:
        # M 개 치킨 집 고르고 각각 치킨 거리 합 구해서 최소를 저장
        tot += min(get_dist(h, c) for c in combi)

    ans = min(ans, tot)

print(ans)
