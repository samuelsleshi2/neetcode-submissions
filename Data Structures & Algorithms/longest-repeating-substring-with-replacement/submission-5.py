class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, maxF, maxW, count = 0, 0, 0, 0, {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxW = max(maxW, r - l + 1)
            maxF = max(maxF, max(count.values()))
            if maxW - maxF <= k:
                res += 1
            else:
                count[s[l]] -= 1
                l += 1
        return res