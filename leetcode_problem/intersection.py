def intersect(nums1, nums2):
    both = []
    for c in nums1:
        if c in nums2:
            nums2.remove(c)
            both.append(c)
    return both
