
def separate_id(S):
    one_by_one = []
    nums = []
    new_n = []
    for i in range(len(S)+1):
        nums.append(i)
    for c in S:
        one_by_one += c
    for c in one_by_one:
        if c == 'I':
            new_n.append(nums[0])
            nums.remove(nums[0])
        elif c == 'D':
            new_n.append(nums[-1])
            nums.remove(nums[-1])
    new_n.append(nums[0])
    return new_n


print(separate_id('DDI'))



