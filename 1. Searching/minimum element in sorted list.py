class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        s = nums[0]
        if s <= nums[high]:
            return s
        while low <= high:
            mid = (low+high)//2
            print(low, mid, high)
            if nums[mid] < nums[mid-1] and nums[mid] < nums[(mid+1)%len(nums)]:
                return nums[mid]
            if nums[mid] >= s:
                low = mid+1
            else:
                high = mid-1
        return -1
