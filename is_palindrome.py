def isPalindrome(s):
    left, right = 0, len(s) - 1

    def alphanum(char):
        return (
                ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9')
        )

    while left < right:
        while left < right and not alphanum(s[left]):
            left += 1
        while left < right and not alphanum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(isPalindrome('A man, a plan, a canal: Panama'))



