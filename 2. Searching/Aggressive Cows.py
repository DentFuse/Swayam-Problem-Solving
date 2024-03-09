class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        low, high = 0, stalls[-1] - stalls[0]
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if self.possible(stalls, k, mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        
        return ans
        pass
    
    def possible(self, stalls, cows, space):
        prev = None
        for i in stalls:
            if not prev or i - prev >= space:
                prev = i
                cows -= 1
                if cows == 0:
                    break
        return cows == 0