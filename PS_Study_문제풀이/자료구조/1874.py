

n = int(input())
count = 1
stk = []
printStack = []
for _ in range(n):
    m = int(input())
    while m >= count:
        stk.append(count)
        count += 1
        printStack.append("+")

    if m == stk[-1]:
        stk.pop()
        printStack.append("-")

    else:
        print("NO")
        exit()

print("\n".join(printStack))

