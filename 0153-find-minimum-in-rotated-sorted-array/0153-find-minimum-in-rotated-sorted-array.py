class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the output looks like it prints the starting number
        #must return the minimum rotations to get its original starting point
        #we need to somehow 'rotate the numbers' to get to its original starting point
        #and implement a counter so we can return that value
        rotationCounter = 0 #to keep track
        minNum = min(nums)
        
        for num in nums:
            lastNum = nums.pop()
            nums.insert(0, lastNum) #insert at index 0
            #print(nums, rotationCounter)
            rotationCounter += 1
            if nums[0] == minNum:
                #print( f'it needs to be rotated {rotationCounter} times')
                return nums[0]

            
