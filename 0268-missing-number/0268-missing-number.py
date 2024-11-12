class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = (sorted(nums))
        if len(nums) == 1:
            if nums[0] == 0:
                return nums[0]+1
            else:
                return nums[0]-1
        
        for i in range(len(sorted(nums))-1):
            # print(f"{nums[i]+1}, {nums[i+1]}")
            if nums[i]+1 != nums[i+1]:
                return nums[i]+1
        #if the number doesnt start with a zero
        if nums[0] != 0:
            return 0
        return nums[-1]+1