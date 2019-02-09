def find_missing_num(nums):
    miss = []
    for i in range(len(nums)):
            if nums[i] < 0:
                if nums[nums[i]*-1 -1] > 0:
                    nums[nums[i]*-1 -1] *= -1
            else:
                if nums[nums[i]-1] >0:
                    nums[nums[i]-1] *= -1
    for i in range(len(nums)):
        if nums[i] > 0:
            miss.append(i+1)
    return miss
    # tf = [False]*len(nums)
    # for i in range(len(nums)):
    #     tf[nums[i]-1] = True
    # missing = []
    # for i in range(len(tf)):
    #     if not tf[i]:
    #         missing.append(i+1)
    # return missing
    # missing = []
    # for i in range(1, len(nums)+1):
    #     if i not in nums:
    #         missing.append(i)
    # return missing


print(find_missing_num([1,2,6,5,2,3]))
1,2,6,5,2,3
