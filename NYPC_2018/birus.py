import sys


def virus():
    times = sys.stdin.readline()
    people, meet = times.split()
    virused = []
    order = []
    for i in range(int(people)):
        if i == 0:
            virused.append(True)
            continue
        virused.append(False)
    for i in range(int(meet)):
        meeting = sys.stdin.readline()
        meeting = meeting.split()
        time = meeting[2]
        order.append(time)
        order.sort()




