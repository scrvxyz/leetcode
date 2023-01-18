class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current, maxi = 0, -sys.maxsize
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            current += nums[i]
            maxi = max(current, maxi)
            if current < 0:
                current = 0
        current = 0
        max2 = 0
        for i in range(len(nums)):
            maxi = max(maxi, sums+max2)
            sums -= nums[i]
            current += nums[i]
            max2 = max(max2, current)
        
        return maxi
