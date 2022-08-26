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