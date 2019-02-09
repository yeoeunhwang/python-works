def reverse_string(st):
    r = ''
    for c in reversed(st):
        r += c
    return r


print(reverse_string('hello'))
