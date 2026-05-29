class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numsSet = sorted(nums)
        longest = 1
        for n in numsSet:
            num = n
            current = 1
            if num - 1 not in numsSet:
                while num + 1 in numsSet:
                    current += 1
                    num += 1
                if longest < current:
                    longest = current

        return longest