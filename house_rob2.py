def rob(nums):
    if len(nums) == 1: return nums[0]
    rob0, rob1, rob2, rob3 = 0, 0, 0, 0
    for i in range(len(nums) - 1):
        temp = max(rob0 + nums[i], rob1)
        rob0 = rob1
        rob1 = temp
    for val in nums[1::]:
        temp = max(rob2 + val, rob3)
        rob2 = rob3
        rob3 = temp
    return max(rob1, rob3)


if __name__ == '__main__':
    print(rob([2, 3, 2]))