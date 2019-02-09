def jewels_in_stones(J,S):
    jewels = []
    count = 0
    for c in J:
        jewels += c
    for c in S:
        if c in jewels:
            count += 1
    return count


print(jewels_in_stones('aA', 'aAdAbfd'))
