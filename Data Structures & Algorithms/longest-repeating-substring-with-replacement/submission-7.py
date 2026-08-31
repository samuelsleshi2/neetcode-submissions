class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxW, maxF, res, count = 0, 0, 0, 0, {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, max(count.values()))
            maxW = max(maxW, r - l + 1)
            if maxW - maxF <= k:
                res += 1
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
        return res
