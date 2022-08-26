def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for num in nums:
        if (num - 1) not in numSet:
            ln = 1
            while (num + ln) in numSet:
                ln += 1
            longest = max(ln, longest)
    return longest


if __name__ == '__main__':
    printLength = longestConsecutive([2, 3, 1, 10, 9, 30, 32, 31, 33, 34, 35])

    print(printLength)


