def transpose(A):
    mixed = []
    new = []
    for i in range(len(A[0])):
        for j in range(len(A)):
            new.append(A[j][i])
        mixed.append(new)
        new = []
    return mixed


print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
