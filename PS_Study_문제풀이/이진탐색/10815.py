from bisect import bisect_left, bisect_right

import sys

N =int(input())
cards = sorted(map(int, sys.stdin.readline().split()))
#To find
M = int(input())
f_cards = list(map(int, sys.stdin.readline().split()))

#check_list
check_list = []

for f in f_cards:
  l = bisect_left(cards, f)
  r = bisect_right(cards, f)
  
  check_list.append(1 if r -l > 0 else 0)

print(*check_list)
