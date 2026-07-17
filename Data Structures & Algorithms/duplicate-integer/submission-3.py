class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnew = set(nums)
        if(len(setnew) < len(nums)):
            return True
        return False