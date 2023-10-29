MOD = 1_000_000_000

#cache[n][d] := 길이가 n, 마지막 수가 d 인 계단수 개수
#d 는 0 ~ 9 , n 은 1 ~ 100
cache = [[0] * 10 for _ in range(101)]

#초기화
for i in range(1, 10):
  cache[1][i] = 1


#Bottom-UP
for i in range(2, 101):
  for j in range(10):
    if j > 0 :
      cache[i][j] += cache[i-1][j-1] 
      cache[i][j] %= MOD
    if j < 9 :
      cache[i][j] += cache[i-1][j+1] 
      cache[i][j] %= MOD



# 결과
ans = 0 
n =int(input())
for i in range(10) :
  ans += cache[n][i]
  ans %= MOD

print(ans)









