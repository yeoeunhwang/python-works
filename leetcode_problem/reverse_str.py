def reverse_str(s, k):
    new = ''
    def reverse(str):
        return str[::-1]

    for i in range(0,len(s),k):
        new += reverse(s[i:i+k])
    return new
    # new = ''
    # st = k-1
    # while len(new) < len(s):
    #     if st > len(s):
    #         for i in
    #     for i in range(st, -1, -1):
    #         new += s[i]
    #         st += k
    # return new


print(reverse_str('apple', 2))



