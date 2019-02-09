def uncommon_from_sentence(A,B):
    uncommon = []
    total = []
    already= []
    total += A.split()
    total += B.split()
    for c in total:
        if c not in uncommon:
            if c not in already:
                uncommon.append(c)
        elif c in uncommon:
            uncommon.remove(c)
            already.append(c)
    return uncommon




print(uncommon_from_sentence('s z z z s', 'z ehs'))

