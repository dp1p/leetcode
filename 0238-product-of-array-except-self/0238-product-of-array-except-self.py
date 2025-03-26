class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        l_multi = 1
        r_multi = 1
        for i in range(len(nums)):
            j = -i -1
            right[j] = r_multi
            r_multi *= nums[j]
            left[i] = l_multi
            l_multi *= nums[i]
             
        return [l*r for l, r in zip(left, right)]