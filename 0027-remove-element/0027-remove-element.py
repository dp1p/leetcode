class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        if len(nums) == 1 and val == nums[0]:
            return 0
        while i < len(nums):
            if nums[i] == val and i != 0: #if the nums[i] is equal to value BUT does not start at 0
                nums.pop(i)
                i -= 1
            elif nums[i] == val and i == 0:
                nums.pop(i)
            else:
                i += 1
        print(nums)