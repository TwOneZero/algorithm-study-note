n, m = map(int, input().split(' '))

cards = sorted(list(map(int, input().split())), reverse=True)

length = len(cards)
result = 0
for i in range(length):
    if cards[i] >= m:
        continue
    for j in range(i+1, length):
        if cards[i] + cards[j] >= m:
            continue
        for k in range(j+1, length):
            blackSum = cards[i] + cards[j] + cards[k]
            if m >= blackSum:
                result = max(result, blackSum)

print(result)
