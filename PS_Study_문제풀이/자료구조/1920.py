import sys

input = sys.stdin.readline

n = int(input())
arr = {int(x): True for x in input().split()}
# arr = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in arr:
        print('0')
    else:
        print('1')
