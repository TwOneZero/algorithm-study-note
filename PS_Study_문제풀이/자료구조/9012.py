for _ in range(int(input())):
  stk = []
  isVps = True
  #한 자씩 check
  for ch in input():
    #여는 괄호
    if ch == '(':
      stk.append(ch)
    #닫는 괄호
    else:
      if stk:
        stk.pop()
      else:
        isVps = False
        break
  if stk:
    isVps = False
  
  print('YES' if isVps else 'NO')