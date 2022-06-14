class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1
        return True

    def isPalindrome_2(self, s: str) -> bool:
        lowered_letters = [c.lower() for c in s if c.isalnum()]
        return lowered_letters == lowered_letters[::-1]

    def isPalindrome_3(self, s: str) -> bool:
        from string import ascii_letters
        ascii_letters_set = set(ascii_letters)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in ascii_letters_set:
                left += 1
            elif s[right] not in ascii_letters_set:
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1
        return True


if __name__=="__main__":
    import timeit
    from string import ascii_letters
    from random import choices
    test_string = choices(ascii_letters, k=10000)
    test_string = test_string + test_string[::-1]
    setup = """from __main__ import Solution"""
    print(timeit.timeit(f"s=Solution();s.isPalindrome({test_string})", setup=setup, number=1000))
    print(timeit.timeit(f"s=Solution();s.isPalindrome_2({test_string})", setup=setup, number=1000))
    print(timeit.timeit(f"s=Solution();s.isPalindrome_3({test_string})", setup=setup, number=1000))
