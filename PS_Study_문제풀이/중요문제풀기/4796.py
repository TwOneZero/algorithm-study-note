

# 연속 20 일 중 10일

count = 1

while True:
  L, P, V = map(int, input().split())
  if L == 0:
    break
  ne = V // P
  rest = V % P
  print(f'Case {count}: {ne * L + min(rest, L)}')
  count += 1


