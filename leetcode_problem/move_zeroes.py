def move_zeroes(nums):
    count = 0
    for n in nums:
        if n == 0:
            nums.remove(0)
            nums.append(0)
    return nums

print(move_zeroes([1,0,2,3,0,4]))

