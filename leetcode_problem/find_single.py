def single_number(nums):
    while len(nums) != 1:
        for i in range(1, len(nums)):
            print('i = ', i)
            if nums[0] == nums[i]:
                del nums[i]
                del nums[0]
                break
        else:
            return nums[0]
    return nums[0]


print(single_number([4,1,2,1,2]))
