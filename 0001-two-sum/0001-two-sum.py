class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #2
        #print(f'starting number {nums[i]}')
            for j in range(i+1, len(nums)): #
                #print(f'DOES {nums[i]} + {nums[j]} == {target}?') 
                if nums[i] + nums[j] == target:
                    #print('IT DOES')
                    return [i,j]

                    #print('it does not')
            
        