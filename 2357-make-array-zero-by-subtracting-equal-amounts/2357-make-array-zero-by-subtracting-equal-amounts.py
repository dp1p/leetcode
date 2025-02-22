class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #can we assume all numbers will equal to zero ?
        nums = set(nums)
        if 0 in nums:
            return len(nums) - 1
        return len(nums)
        
