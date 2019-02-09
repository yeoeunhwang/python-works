def judge_circle(moves):
    p = [0,0]
    for c in moves:
        if c == 'U':
            p[1] += 1
        elif c == 'D':
            p[1] -= 1
        elif c == 'L':
            p[0] -= 1
        else:
            p[0] += 1
    if p == [0,0]:
        return True
    elif p != [0.0]:
        return False
