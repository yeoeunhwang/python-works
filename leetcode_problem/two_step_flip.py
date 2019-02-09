def flip_and_invert(A):
    flip = A
    invert = A
    for i in range(len(A)):
        flip[i].reverse()
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                invert[i][j] = 1
            elif A[i][j] == 1:
                invert[i][j] = 0
    return invert
