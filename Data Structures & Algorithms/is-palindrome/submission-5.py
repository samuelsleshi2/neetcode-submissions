class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum() and c != " ":
                string += c.lower()
        l = 0
        r = len(string) - 1

        while (l < r):
            if string[l] == string[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
        
        return True