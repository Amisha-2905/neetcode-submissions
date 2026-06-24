class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newstr = ''
        for l in s:
            if l.isalnum():
                newstr += l
        return newstr == newstr[::-1]

