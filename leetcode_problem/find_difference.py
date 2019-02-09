def find_difference(s, t):
    list_s = list(s)
    for c in t:
        if c not in list_s:
            return c
        list_s.remove(c)


print(find_difference('abcd', 'abcde'))
