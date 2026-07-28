class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            elif nums[m] >= nums[l]:
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            # right sorted portion
            else:
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1
