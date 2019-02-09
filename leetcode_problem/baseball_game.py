def baseball_game(ops):
    score = 0
    record = []
    for c in ops:
        if c == '+':
            sc = record[-2:][0] + record[-2:][1]
            score += sc
            record.append(sc)
        elif c == 'D':
            sc = record[-1] * 2
            score += sc
            record.append(sc)
        elif c == 'C':
            score -= record[-1]
            del record[-1]
        else:
            score += int(c)
            record.append(int(c))
    return score


print(baseball_game(["5","-2","4","C","D","9","+","+"]))





