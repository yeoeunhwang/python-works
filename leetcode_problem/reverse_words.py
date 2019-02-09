def reverse_words(s):
    origin_words = []
    reversed_words = []
    origin_words += s.split()
    for w in origin_words:
        reversed_words += w[::-1]
    rws = ' '.join(reversed_words)
    return rws


reverse_words()
