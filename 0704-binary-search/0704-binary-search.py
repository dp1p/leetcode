class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #when it comes to to binary search, we divide to get rid half of the nums to take less "steps"
        #when you do arr.index(number), worse case it will n steps to get to a number
        #with binary search, worse case it will take log(n) to get to the numbers

        1.0
        #assuming it is sorted, we will grab the midpoint
        #once we compare it to the middle of the arr, we will determine how to divide it if target > or <
        #then iterate to the next number
        #once it hits the last num, if it is not there, return -1

        2.0
        #we have low and high
        #low, high == 0, len(nums)-1 #these are essentially pointers
        #while low < high 
            #midpoint == low + high // 2 (get midpoint)
            #if target > nums[midpoint] #if target is GREATER than the value of the midpoint 
                #low = midpoint #move the LOW pointer to where midpoint
            #elif target < nums[midpoint] #if target is LESS than the value of the midpoint
                #high = midpoint  #move the HIGH pointer 
            #elif target == nums[midpoint]:
                #return midpoint #return midpoint of where the index was found 
        #return -1
        
        low, high = 0, len(nums)-1 #to prevent going out of index
        while low <= high:
            midpoint = (low + high) // 2 #(get midpoint)
            if target > nums[midpoint]: #if value at midpoint is LESS than target num, move LOW UP
                low = midpoint + 1
            elif target < nums[midpoint]: #if value at midpoint is GREATER than target num, move HIGH DOWN
                high = midpoint - 1
            else:
                return midpoint
        return -1
           