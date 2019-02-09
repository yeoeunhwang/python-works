def detect_capital_use(word):
    def is_capital(letter):
        return 'A' <= letter <= 'Z'
    judge = []
    cap = 0
    not_cap = 0
    for l in word:
        judge.append(is_capital(l))
        if is_capital(l):
            cap += 1
        else:
            not_cap += 1
    if cap == len(word):
        return True
    elif not_cap == len(word):
        return True
    elif judge[0] == True and not_cap == len(word) -1:
        return True
    else:
        return False


print(detect_capital_use('deefed'))
