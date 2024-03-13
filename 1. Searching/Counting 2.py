# Problem Statement

# There is a class with
# N students. The height of the i-th student (1≤i≤N) is

# Ai​.

# For each

# j=1,2,…,Q, answer the following question.

#     How many of the 

# N students have a height of at least

#     xj​?

# Constraints

# 1≤N,Q≤2×105
# 1≤Ai​≤109
# 1≤xj​≤109
# All values in input are integers.

q = int(input().split()[1])
arr = list(map(lambda x: int(x), input().split()))
arr.sort(reverse=True)
for i in range(q):
    x = int(input())
    low, high = 0, len(arr)
    ans = 0
    while low < high:
        mid = (low+high)//2
        if arr[mid] >= x:
            low = mid+1
            ans = low
        else:
            high = mid - 1
    print(ans)