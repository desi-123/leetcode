def threeSum(nums):
    nums = sorted(nums)
    lst = []
    for i, val in enumerate(nums):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            tot = val + nums[left] + nums[right]
            if tot == 0:
                elements = [val, nums[left], nums[right]]
                if elements not in lst:
                    lst.append(elements)
                right -= 1
            elif tot < 0:
                left += 1
            else:
                right -= 1
    return lst

if __name__ == '__main__':
    print(threeSum([-1, 0, 1, 2, -1, -4]))