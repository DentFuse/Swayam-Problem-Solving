class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, min(x, 2**16)
        ans = high
        while low <= high:
            mid = (low+high)//2
            s = mid*mid
            if s == x:
                return mid
            if s < x:
                low = mid+1
            else:
                high = mid-1
                ans = high
        return ans