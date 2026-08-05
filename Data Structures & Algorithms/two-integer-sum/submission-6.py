class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for i, n in enumerate(nums):
            if target - n in hashmap and i != hashmap[target - n]:
                return [i, hashmap[target - n]]