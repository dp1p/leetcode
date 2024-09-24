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
        if len(nums) == 1:
            if target != nums[0]:
                return -1
            else:
                return 0

        while low < high:
            print(f"{low} + {high} + {low} / 2 =")
            midpoint = (low + high) // 2 #(get midpoint)
            print(midpoint)
          
            if target == nums[midpoint]: #if the target is found right at midpoint
                print("nicely done, found ! ")
                return midpoint
            elif target > nums[midpoint]: #if value at midpoint is LESS than target num, move LOW UP
                print(f'{target} > {nums[midpoint]}')
                print(f'moving low midpoint to {midpoint}')
                low = midpoint 
            elif target < nums[midpoint]: #if value at midpoint is GREATER than target num, move HIGH DOWN
                print(f'moving high midpoint to {midpoint}')
                print(f'{target} < {nums[midpoint]}')
                high = midpoint
            
            if midpoint == 1 or midpoint == len(nums) - 2: #if midpoint is at index 1 or at very end of arr
                print('checking beginning')
                if target == nums[0]: #we will check at index 0 for the user
                    return 0
                elif target == nums[-1]: #we will check very last index for the user
                    return len(nums)-1
                else:
                    print('not found')
                    return -1
       
        # if len(nums) % 2 == 0: #if the length of sequence is even print('not even')
        #     midpoint = int(len(nums) / 2 )#grab index of midpoint
        #     if target == nums[midpoint]: #if the value of midpoint is equal to the target
        #         print("other hi")
        #         print("VALUE WAS FOUND ALREADY!!! LOL")
        #         return midpoint #return index 

            # while target < nums[midpoint]: #we go down the sorted arr and find it
            #     print("target is LESS than nums")
            #     if target == nums[midpoint]:
            #         print(f"found")
            #         return midpoint
            #     else:
            #         print(f"not found yet")
            #         midpoint -= 1
            #     if midpoint == 0: #if midpoint is at the very last index
            #         return -1

            # while target > nums[midpoint]: #we go down the sorted arr and find it
            #     print("target is GREATER than nums")
            #     midpoint +=1 
            #     if midpoint >= len(nums): #if this goes out of bounds
            #         return -1
            #     print(f"INCREASING {midpoint}")
                # print(nums[midpoint])
                # if target == nums[midpoint]:
                #     print(f"found")
                #     return midpoint
                # else:
                #     print(f"not found yet")
                #     midpoint += 1
                # if midpoint == len(nums) - 1: #if midpoint is at the very last index
                #     print("last")
                #     return -1

           
                
            


                
        # else:
        #     print('not even')
        #     midpoint = len(nums)+1 / 2
        #     print(midpoint)
        # midpoint = len(nums) 

