# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

# SOLVE >>>>
#  순서없이 9개 중 7개 뽑아서 합이 100이 될 때 출력
#
from itertools import combinations

gathered = []
for _ in range(9):
  gathered.append(int(input()))
gathered.sort()

##combination 사용
# for combi in combinations(gathered, 7):
#   if sum(combi) == 100 :
#     for h in sorted(combi):
#       print(h)
#     break


##combination 없이
total = sum(gathered)
def f():
  for i in range(8):
    for j in range(i+1, 9):
      if total - gathered[i] - gathered[j] == 100:
        for k in range(9):
          if( k != i and  k != j):
            print(gathered[k])

        return

f()


