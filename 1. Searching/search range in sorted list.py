class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        mid = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        i = mid
        if i == -1:
            return [-1]*2
        low, high = 0, i
        left = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] != target:
                low = mid+1
                continue
            if mid == 0 or nums[mid] != nums[mid-1]:
                left = mid
                break
            high = mid-1
        low, high = i, len(nums)-1
        right = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] != target:
                high = mid-1
                continue
            if mid == len(nums) -1 or nums[mid] != nums[mid+1]:
                right = mid
                break
            low = mid+1
            
        return [left, right]
            