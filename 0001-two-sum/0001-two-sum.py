class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #subtract target from the first num
        #if the difference is not in the nums arr, continue
            #we will store our value in a hash map [idx, number]
        #if the difference is in our nums arr (and a different index)
            #return nums, difference
        #if len(nums) == 1 and nums[0] == target
            #return nums
        
        h = {} #to store nums, and if difference is in here, then return it
        for idx, number in enumerate(nums):
            difference = target - number #9-7
            # print(difference)
            if difference not in h.keys():
                # print(f'{difference} NOT IN HASHMAP ADDING {number}')
                h[number] = idx
            else:
                # print(f' {difference} IN HASHMAP')
                number = h.get(difference)
                return idx, nums.index(difference)
                
        # print(h)