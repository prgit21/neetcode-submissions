class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''.join(ch.lower() for ch in s if ch.isalnum())
        rev_string =stripped[::-1]
        return stripped == rev_string