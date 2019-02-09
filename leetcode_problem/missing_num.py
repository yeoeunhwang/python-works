def missing_num(nums):
    origin_sum = sum(range(len(nums) + 1))
    diff = origin_sum - sum(nums)
    return diff


print(missing_num([1]))
