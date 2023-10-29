# (N - 7) * (M - 7) * 64 * 2

# print(43 * 43 * 64  * 2)



N, M = map(int, input().split())
#N 개의 줄에 걸쳐 문자열 입력
board = [input() for _ in range(N)]

# 최대 64개를 다시 칠해야 함
ans = 64

# bw : 맨왼쪽 맨위의 색
def fill(y, x, bw):
  global ans
  cnt = 0 
  for i in range(8):
    for j in range(8):
      if (i + j) % 2: #홀수 인덱스
        # 기준인 bw 과 같으면 바꿈
        if board[y + i][x + j] == bw:
          cnt += 1
      else: # 짝수 인덱스
        if board[y + i][x + j] != bw:
          cnt += 1
  ans = min(ans, cnt)

for i in range(N-7):
  for j in range(M-7):
    fill(i, j, 'B')
    fill(i, j, 'W')
    
print(ans)
