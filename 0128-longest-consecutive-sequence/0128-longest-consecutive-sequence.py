class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {} #to store the nums in the hashtable
        counter = 1 #to keep track of the nums
        nums = sorted(nums) #to sort the nums
        print(nums)
        if nums == []:
            print('empty')
            return 0
        for i in range(len(nums)-1):
            # print(f'CURRENT NUM: {nums[i]} || NEXT NUM: {nums[i+1]}')
            nextNum = nums[i+1] #get the next num in the arr
            if nums[i]+1 == nextNum: #if the next number increments
                counter+=1
                # print(f'COUNTER COUNT {counter}')
            elif nums[i] == nums[i+1]: #if num is equal to the next one
                # print(f'COUNTER COUNT STAYS THE SAME {counter}')
                continue
            else: #if the number does NOT increment
                h[counter] = 0     #the key will the counter, value will just be zero.
                counter = 1         #reset counter
                # print(f'COUNTER RESET: {counter}')
            
        h[counter] = 0 #if the number keeps incrementing all the way to end of the arr

        return max(h.keys()) #return the max value key

