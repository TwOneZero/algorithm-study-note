import sys

input = sys.stdin.readline

N = int(input())

req = list(map(int, input().split()))

M = int(input())

# 이분 탐색을 위해 지점을 설정
lo = 0
hi = max(req)
mid = (hi + lo) // 2  # 예산 지급 상한액
ans = 0


def is_possible(mid):  # 예산이 가능한지 확인
    return sum(min(r, mid) for r in req) <= M


# lo 와 hi 가 가까워지고, lo 가 hi 보다 커지면 종료
while lo <= hi:
    # print(f'lo: {lo}  , mid: {mid}  , hi: {hi}  , ans: {ans}')
    if is_possible(mid):  # 예산이 가능한 범위라면 -> lo 를 mid 로 늘림
        lo = mid + 1
        ans = mid
    else:  # 불가능이면 hi 를 mid 로 낮춤
        hi = mid - 1
    mid = (lo + hi) // 2

print(ans)
