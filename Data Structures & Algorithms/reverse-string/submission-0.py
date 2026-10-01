class Solution:
    def reverseString(self, s: List[str]) -> None:
        res = []
        for char in reversed(s):
            res.append(char)

        for i in range(len(s)):
            s[i] = res[i]

        