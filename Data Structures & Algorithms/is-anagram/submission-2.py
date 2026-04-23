class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = []
        for _ in s:
            s_chars.append(_)
        s_chars.sort()
        
        t_chars = []
        for _ in t:
            t_chars.append(_)
        t_chars.sort()

        if s_chars != t_chars:
            return False
        return True