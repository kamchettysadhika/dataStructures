class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        longest = 0
        for number in nums:
            if (number -1) not in numberSet:
                length = 0
                while number +length in numberSet:
                    length+=1
                longest = max(length,longest)
        return longest
