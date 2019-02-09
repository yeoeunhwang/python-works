def addDigits(num):
    while num >= 10:
        sum_last = 0
        while num:
            num, last = divmod(num, 10)
            sum_last += last
        num = sum_last
    return num

    # while num >= 10:
    #     add = 0
    #
    #     num = str(num)
    #     for c in num:
    #         add += int(c)
    #     num = add
    # return num


print(addDigits(444))
