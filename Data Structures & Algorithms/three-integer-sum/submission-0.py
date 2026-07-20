class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []

        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triplets.append((n, nums[l], nums[r]))
                    l += 1
                    r -= 1

        return list(set(triplets))