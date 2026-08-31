class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxL, window = 0, 0, set()
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL