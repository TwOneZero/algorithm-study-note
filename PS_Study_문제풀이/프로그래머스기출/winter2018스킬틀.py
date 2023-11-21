skill = "CBD"

skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


tmp = []
cnt = 0
for s_tree in skill_trees:
    is_valid = True
    skill_stk = list(reversed(skill)) # DBC
    for s in s_tree:
        if s in skill:
            tmp.append(s)

    tmp = list(reversed(tmp)) #DCB
    print(f'skill-stk : {skill_stk}')
    print(f'tmp : {tmp}')
    while tmp:
        if skill_stk.pop() != tmp.pop():
            # D B C
            # D C B
            is_valid = False

    print(f'is_valid : {is_valid}')
    if is_valid:
        cnt += 1

print(cnt)