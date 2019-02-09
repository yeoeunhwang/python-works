import sys


def buy_items():
    pay = sys.stdin.readline()
    pay = pay.split()
    pp = int(pay[0])
    qp = int(pay[1])
    money = sys.stdin.readline()
    money = int(money)
    cp = 0
    cq = 0
    while cp * pp < money :
        cp += 1
        cq = (money-cp*pp) // qp
        remain = (money-cp*pp) % qp
        if remain == 0:
            break

    print(str(cp) + ' ' + str(cq))


buy_items()
