class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for num in nums:
            sum += num
            self.prefix.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right]
        if left > 0:
            l = self.prefix[left - 1]
        else:
            l = 0
        return r - l

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)