T = int(input())

for _ in range(T):
    result = []
    tmp = []
    for p in list(input()):
        if p == '<':
            if result:
                tmp.append(result.pop())
        elif p == '>':
            if tmp:
                result.append(tmp.pop())
        elif p == '-':
            if result:
                result.pop()
        else:
            result.append(p)

    # 커서만 왼쪽으로 움직인 경우 마지막에 더해줌
    result.extend(reversed(tmp))
    print(''.join(result))
