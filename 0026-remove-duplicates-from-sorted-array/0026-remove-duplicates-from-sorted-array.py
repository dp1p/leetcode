class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #TWO POINTER METHOD
        #we will have a left and right pointer
        #left pointer starts at zero
        #right pointer starts at i + 1
        
        #the left pointer will be the unique value
        #the purpose of the right pointer is to scan and swap places wherver the left pointer is

        #while right pointer != len(nums)-1
            #if the nums[left pointer] == nums[right pointer[]:
                #move right pointer
                #move left pointer 
            #elif nums[left pointer] != nums[right pointer[]:
                #nums[left pointer] = nums[right pointer]
                #move right pointer
                #move left pointer
        
        counter = 1 #to count how many times there is a unique number
        if len(nums) == 1:
            return counter

        left = 0
        right = 1

        while right != len(nums):
            # print(nums[left], nums[right])
            if nums[left] != nums[right]:
                left += 1 #we move to the left once we find a number that is NOT equal to eachother
                #print('swapping!')
                nums[left] = nums[right]
                right += 1
                counter += 1
            else:
                #print('they equal eachother, no swap')
                right += 1
        # print(nums)
        return counter
