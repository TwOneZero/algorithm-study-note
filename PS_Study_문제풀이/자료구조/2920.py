asc = True
desc = True

a = list(map(int, input().split(' ')))

for i in range(1, 8):
    if a[i] > a[i - 1]:
        desc = False
    elif a[i] < a[i - 1]:
        asc = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')


