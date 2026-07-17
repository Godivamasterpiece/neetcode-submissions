class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i, num in enumerate(nums):
            left = target - num
            if left in targets:
                return [ targets[left],i]
            targets[num] = i