class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        for c, v in hashmap.items():
            count[v].append(c)

        result = []
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                result.append(n)
                if len(result) == k:
                    return result