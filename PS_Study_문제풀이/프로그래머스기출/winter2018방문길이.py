import sys
#
# input = sys.stdin.readline
#
# dirs = input().rstrip()
# direction = {
#     'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)
# }
#
# board = [[] * 11 for _ in range(11)]
# cnt = 0
# y, x = 5, 5
# from_p = 0
#
# for d in dirs:
#     print(f'---------')
#
#     ny, nx = direction[d] # tuple
#     y = y + ny
#     x = x + nx
#     print(f'({y}, {x})')
#     print(f'---------')
#     if y == -1 or x == -1 or y == 11 or x == 11:
#         y = y - ny
#         x = x - nx
#     elif board[y][x] != 1:
#         board[y][x] = 1
#         cnt += 1
#
# print( cnt )

# 챗 지피티 솔루션
def solution(dirs):
    directions = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = set()
    x, y = 0, 0
    count = 0

    for move in dirs:
        dx, dy = directions[move]
        new_x, new_y = x + dx, y + dy

        # 좌표평면의 경계를 넘어가는 경우 무시
        if not (-5 <= new_x <= 5 and -5 <= new_y <= 5):
            continue

        # 캐릭터의 현재 위치와 새로운 위치를 지나간 경로에 추가
        path = (x, y, new_x, new_y)
        reversed_path = (new_x, new_y, x, y)

        if path not in visited and reversed_path not in visited:
            visited.add(path)
            visited.add(reversed_path)
            count += 1

        # 캐릭터의 위치 업데이트
        x, y = new_x, new_y

    return count

# 예시 입력
dirs = "ULURRDLLU"

# 결과 출력
print(solution(dirs))  # 7