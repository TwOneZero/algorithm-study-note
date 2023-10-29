from collections import deque
import sys
#좌표계
dy  = (0 ,1 ,0 , -1)
dx  = (1 ,0 ,-1 , 0)

#지도 크기
N, M= map(int, input().split())
#갈 수 있는 길
board = [input() for _ in range(N)]

#지도 허용범위 체크
def is_valid_coord(y , x):
  return 0 <= y < N and 0 <= x < M  

#BFS 
def bfs():
  #중복방문 체크
  is_visit = [[False] * M for _ in range(N)]
  is_visit[0][0] = True

  q = deque()
  # 큐에 몇 칸을 지났는 지도 저장
  q.append((0, 0, 1))
  while q:
    y, x, d = q.popleft()
    #끝까지 도달하면 break
    if y == N -1 and x == M -1:
      return d
    nd = d + 1
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      # check
      if  is_valid_coord(ny, nx) and board[ny][nx] == '1' and not is_visit[ny][nx] :
        is_visit[ny][nx] = True
        q.append((ny, nx, nd))


print(bfs())


  


# bfs(0,0)