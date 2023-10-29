

# N 킬로 그램 배달 최소 봉지


# 3 a + 5 b = N ( 3 <= N <= 5000 )이 돼야 함
# 3키로는 계속 빼주면서 5로 나눠지는 지 체크
N = int(input())

ans = 0
while N > 0:
  if N % 5 == 0 : 
    ans += N // 5
    N %= 5
    break
  N -= 3
  ans += 1

print(ans if N == 0 else -1)


