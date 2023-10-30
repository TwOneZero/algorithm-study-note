from bisect import bisect_left, bisect_right

# 이분 탐색을 bisect 라이브러리를 사용해서 구현
v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3)
four = bisect_right(v, 4) - bisect_left(v, 4)
six = bisect_right(v, 6) - bisect_left(v, 6)

print(f'number of 3: {three}')
print(f'number of 4: {four}')
print(f'number of 6: {six}')
