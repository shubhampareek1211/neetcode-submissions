import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]'
        s1 = re.sub(pattern, '', s).lower()
        i = 0
        j = len(s1) -1
        while i<j:
            if s1[i]==s1[j]:
                i += 1
                j -= 1
            else:
                return False
        return True 