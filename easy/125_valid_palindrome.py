class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left, right = left + 1, right - 1
        return True

    def isPalindrome_2(self, s: str) -> bool:
        lowered_letters = [c.lower() for c in s if c.isalnum()]
        return lowered_letters == lowered_letters[::-1]
