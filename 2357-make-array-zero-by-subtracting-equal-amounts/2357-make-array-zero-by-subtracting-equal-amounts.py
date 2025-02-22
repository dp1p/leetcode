class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #1. find the smallest number
        #2.1 if it is zero, pop it
        #else:
        #2.2 find the next smallest number
        #3. subtract it from every number in arr
        #4. after that, keep going
        #if all numbers are zero, return a counter that keeps track of it
        if nums[0] == 0 and len(nums) == 1:
            return 0
        if 0 in set(nums) and len(set(nums)) == 1:
            return 0
        if set(nums) == 0:
            return 0
        if len(set(nums)) == 1:
            return 1
        counter = 0
        while len(set(nums)) != 1:
            smallest_num = float('inf')
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                if smallest_num > nums[i]:
                    smallest_num = nums[i]
                print(smallest_num)
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue
                else:
                    nums[i] -= smallest_num
            counter += 1
            print(nums)
        return counter

        # def recursion(nums, counter)
        #     if nums is []:
        #         return counter
            
        #     smallest_num = [num for i in range(len(nums)) if nums[i] < nums[i+1]]
            
        
        # recursion(nums[0]) # -> represents the start of iteration
        
