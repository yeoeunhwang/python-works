def numSpecialEquivGroups(A):
    group = []
    for c in A:
        if c not in group:
            group.append(c)
    return group
