def reverse_st(s, k):
    def reverse(str):
        return str[::-1]
    group = []
    new = ''
    for i in range(0, len(s), k*2):
        group.append(s[i:i+2*k])
    for s in group:
        if len(s) == k*2 or k<len(s)<2*k:
            new += reverse(s[:k])
            new += s[k:]
        if k >= len(s):
            new += reverse(s)
    return new


print(reverse_st('abcdefg', 2))
