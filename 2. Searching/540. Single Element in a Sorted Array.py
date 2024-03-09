class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        if len(nums) == 1:
            return nums[0]
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == nums[mid-1]:
                mid -= 1

            if mid%2 == 0:
                if ((mid == 0 or nums[mid] != nums[mid-1]) and (mid == len(nums)-1 or nums[mid] != nums[mid+1])):
                    return nums[mid]
                low = mid+2
            else:
                high = mid-1