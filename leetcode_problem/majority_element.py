def majority_element(nums):
    nums.sort()
    return nums[len(nums)//2]


print(majority_element([2,1,5,4,3,5,6]))
