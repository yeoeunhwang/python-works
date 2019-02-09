def short_term():
    f = open('input5.txt', encoding='utf-8')
    times = int(f.readline())
    for i in range(times):
        long_word = f.readline()
        short_word = long_word.split()
        changed = ''
        for w in short_word:
            changed += w[0]
        print(changed)


short_term()


