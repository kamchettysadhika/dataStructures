class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l = 0 
        profit = 0 
        maxProfit = 0 
        for r in range(len(nums)):
            if nums[l]>nums[r]:
                l = r 
            else:
                profit = nums[r] - nums[l]
                maxProfit = max(maxProfit,profit)
        return maxProfit