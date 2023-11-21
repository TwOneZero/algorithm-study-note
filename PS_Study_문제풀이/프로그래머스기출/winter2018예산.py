don = list(map(int, input().split()))

budget = int(input())

don.sort()
cnt = 0
for d in don:
    budget -= d
    cnt += 1
    if budget < 0:
        cnt -= 1
        break

print(cnt)
