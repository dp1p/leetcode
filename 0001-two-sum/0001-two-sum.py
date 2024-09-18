class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h ={}
        total_diff = 0
        for i in range(len(nums)):
            total_diff = target - nums[i]
            # h[nums[i]]=i
            if total_diff in h.keys():
                return h[total_diff], i
            else:
                h[nums[i]]=i
            print(h)
        return False