class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                ##sorted left
                if nums[left] <= target < nums[mid]:
                    #target in left sorted
                    right = mid - 1
                else:
                    #target in right
                    left = mid + 1
            else:
                ##sorted right
                if nums[mid] < target <= nums[right]:
                    #target in right sorted
                    left = mid + 1
                else:
                    # target in left
                    right = mid - 1
        
        return -1