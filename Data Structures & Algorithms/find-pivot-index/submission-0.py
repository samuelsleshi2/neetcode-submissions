class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        for i, item in enumerate(prefix):
            if i == len(prefix) - 1:
                return -1
            if item == prefix[len(prefix) - 1] - prefix[i + 1]:
                return i

        return -1