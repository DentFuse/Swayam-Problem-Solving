class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        if len(nums) == 1:
            return 0
        while low <= high:
            mid = (low+high)//2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]):
                return mid
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if mid == 0 or nums[mid] > nums[mid-1]:
                low = mid+1
            else:
                high = mid-1