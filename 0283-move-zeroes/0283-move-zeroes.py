class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #cannot make new arr
        #has to be original
        
        #for loop to iterate nums
        #if num == zero
        #pop the num, and save it to a variable
        #then we push the zero at the end of the nums once we get all the zeros
        storeZero = []
        i = 0
        numLength = len(nums)
        while i <= len(nums)-1:
            if nums[i] == 0:
                # print(f"yes {nums[i]} is a zero")
                zero = nums.pop(i) #popping searches by index, not element
                storeZero.append(zero)
            else:
                # print('not zero')
                i += 1
        
        nums.extend(storeZero)

        return(nums)
