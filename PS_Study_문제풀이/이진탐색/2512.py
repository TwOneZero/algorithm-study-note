import sys

N = int(input())
req = list(map(int, sys.stdin.readline().split()))

M = int(input())

lo = 0 
hi = max(req)
mid = ( lo + hi ) // 2
ans =0

def check_possible(m):
  return sum(min(m, r) for r in req) <= M

while lo <= hi : 
  if check_possible(mid):
    lo = mid + 1
    ans = mid
  else :
    hi = mid - 1
  
  mid = (lo + hi ) // 2

print(ans)