import math
class Solution:
	def NthRoot(self, n, m):
		# Code here
		low, high = 0, min(10**(math.ceil(9/n)), m)
		
		while low <= high:
			mid = (low+high)//2
			s = mid**n
			if s == m:
				return mid
			if s < m:
				low = mid+1
			else:
				high = mid-1
		return -1