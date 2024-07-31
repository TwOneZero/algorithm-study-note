T = int(input())

for _ in range(T):
    n, m = list(map(int, input().split(' ')))
    tmp = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(tmp)]

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if m == queue[0][1]: # 조건 만족하면 끝
                print(count)
                break
            else: # 제일 큰 수 이지만, 찾는 인덱스가 아니라면 그냥 추출
                queue.pop(0)

        else: # 맨 앞이 제일 큰 수가 아니라면 추출해서 뒤로 보내기
            queue.append(queue.pop(0))
