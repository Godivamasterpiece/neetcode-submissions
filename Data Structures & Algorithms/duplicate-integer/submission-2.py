class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        result = any(count[key] > 1 for key in count)
        return result
        