def fizz_buzz(n):
    total = []
    for i in range(n):
        num = i + 1
        s = ''
        if num % 3 == 0:
            s += 'Fizz'
        if num % 5 == 0:
            s += 'Buzz'
        elif num % 3 != 0:
            s += str(num)
        total.append(s)
    return total


print(fizz_buzz(3))
