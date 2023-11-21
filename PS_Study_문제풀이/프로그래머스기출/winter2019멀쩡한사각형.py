# 잘리는 경우
# 0 정사각형 -> 변 길이 빼면 됨
# 1. 2 X 다른 수
# -1 홀수일 때, 긴 변 + 1 빼면 됨
# -2 찍수일 때, 긴 변 빼기

# 2. 3 X 3보다 큰 수 -> 긴 변 + 2 빼면 됨
w, h = map(int, input().split())

o_cnt = w * h
minus = 0

if w == h:  # 정사각형일 때
    print(o_cnt - w)

if w == 2 or h == 2:
    longer = max(w, h)
    if longer % 2:  # 홀 수
        minus = longer + 1
    else:
        minus = longer
elif w == 3 or h == 3:
    longer = max(w, h)
    minus = longer + 2
else:
    1


print(o_cnt - minus)
