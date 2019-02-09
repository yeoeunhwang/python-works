def find_nexon():
    a = open('input2.5.txt')
    count = 0
    times = a.readline()
    times = times.split()
    for i in range(int(times[0])):
        st = a.readline()
        st = st.split()
        for j in range(int(times[1])):
            if st[j] == 'NEXON':
                count += 1
    print(count)


find_nexon()


