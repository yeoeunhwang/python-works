import sys


def num_to_alp():
    alp = []
    time = sys.stdin.readline()
    nums = sys.stdin.readline()
    nums = nums.split()
    for d in nums:
        print(chr(int(d)), end=' ')


num_to_alp()
