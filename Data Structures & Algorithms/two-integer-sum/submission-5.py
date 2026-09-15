class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        searchMap = {} #val->index
        for i,num in enumerate(nums):
            searchMap[num] =  i 
        for i,num in enumerate(nums):
            diff = target - num
            if diff in searchMap and searchMap[diff]!=i:
                return [i,searchMap[diff]]
        return [0,0]