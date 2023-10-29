
# 기타 1번 ~ 6번  6개 줄

# P 개의 프렛 1 번 ~ P 번

import sys



N, _ = map(int, input().split())
stk = [[] for _ in range(7)]
cnt = 0
for _ in range(N):
  line , p = map(int, sys.stdin.readline().split())
  while stk[line] and stk[line][-1] > p:
    stk[line].pop()
    cnt += 1
  if stk[line] and stk[line][-1] == p :
    continue
  elif not stk[line] or stk[line][-1] < p :
    stk[line].append(p)
    cnt += 1
    
  
print(cnt)
  


