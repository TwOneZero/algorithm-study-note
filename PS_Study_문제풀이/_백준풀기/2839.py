# # 3 , 5
N = int(input())

봉지 = 0

while N > 0:
    # 5로 최대한 나눠야 함
    if N % 5 == 0:
        봉지 += (N // 5)
        N %= 5
        break
    # 3은 남는 거에서 빼주면 됨
    N -= 3
    봉지 += 1

if N != 0:
    print(-1)
else:
    print(봉지)



