class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = {}
        for i in range(len(nums)):
            if nums[i] not in answer:
                answer[nums[i]] = 1
            else:
                answer[nums[i]] += 1
        
        for key in answer.items():
            if key[1] == 1:
                return key[0]
        
            