def interaction(nums1, nums2):
    single = []
    both = []
    for c in nums1:
        if c not in single:
            single.append(c)
    print(single)
    for c in single:
        if c in nums2:
            both.append(c)
    return both


print(interaction([4,7,9,7,6,7], [5,0,0,6,2,4]))
