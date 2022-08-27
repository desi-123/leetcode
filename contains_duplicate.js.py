def containsDuplicate(nums):
    seen = set()

    for val in nums:
        if val in seen:
            return True

        seen.add(val)
    return False


if __name__ == '__main__':
    duplicate = containsDuplicate([1, 2, 3, 1])
    print(duplicate)