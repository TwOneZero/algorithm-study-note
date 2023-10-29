# N , L = map(int, input().split())
# coord = [False] * 1001
# count = 0


# for i in map(int, input().split()):
#   coord[i] = True

# point = 0
# while point < 1001:
#   if coord[point] :
#     count+=1
#     point+= L
#   else:
#     point +=1 

# print(count)

# !!!!!!만약 물새는 곳이 억단위 라면?
# flag 를 써서 하는 것은 메모리, 시간 비효율적
# 원하는 곳만 저장해야한다. 

# N - 물 새는 곳 // L - 테이프 길이
N, L = map(int, input().split())
arr = list(map(int, input().split()))  # 좌표 압축
arr.sort()

cnt, taping = 0, 0
for i in arr:
    if i > taping:  # 테이핑 하는 곳부터 다음 스팟이 테이프 길이보다 멀다면 추가
        cnt += 1
        taping = i + L - 1  # 테이핑 하고 있는 구간을 저장

print(cnt)


