class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target: return True
            if nums[low] == nums[mid]:
                low += 1
                continue
            if nums[low] <= nums[mid]:
                # left is sorted
                if target >= nums[low] and target < nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                # right is sorted
                if target <= nums[high] and target > nums[mid]:
                    low = mid
                else:
                    high = mid-1
        return False