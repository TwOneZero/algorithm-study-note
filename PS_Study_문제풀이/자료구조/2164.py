# from collections import deque
#
# dq = deque()
# for i in range(int(input())):
#   dq.append(i+1)
# while(len(dq) > 1):
#   dq.popleft()
#   dq.append(dq.popleft())
# print(dq.pop())
#


# 큐로  풀 수 있음
from collections import deque

dq = deque()

for i in range(int(input())):
    dq.append(i + 1)  # 왼쪽부터 채워짐

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

# 마지막 남은 수 출력
print(dq.pop())
