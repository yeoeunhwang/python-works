def find_single2(nums):
    single_time = []
    for n in nums:
        if n in single_time:
            single_time.remove(n)
        else:
            single_time.append(n)
    return single_time[0]


print(find_single2([2,2,2,2,3,5,3,5,3]))
