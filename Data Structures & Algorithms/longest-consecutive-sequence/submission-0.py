class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numset:
                currlength = 0
                while currlength + num in numset:
                    currlength += 1
                longest = max(longest,currlength)

        return longest