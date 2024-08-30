class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #if there are two of the same element values, grab the index of them
        #then subtract and get their abs value
        #i will store them using a hashmap
        #hashmap { 0:1
        #           1:2           
        #           2:3
        #           3:1
        #}
        #if they are same value, we will subtract and check if it <= k
        #if not, then we will return false
        #e;se, add to hashmap
        #we use i and j
        #if abs(i-j) <= k:
        # return true
        #else:
        #return false

        hashmap = {} #to store our arr by idx : val
        

        for idx, val in enumerate(nums):
            if val not in hashmap:
                print(f'val not found. adding {val} to hashmap')
                hashmap[val] = idx
            else:
                print(f'VALUE {val} FOUND!')
                indexInHash = hashmap[val]
                print(f'VALUE {val} at index {indexInHash} vs {idx}' )
                difference = abs(indexInHash - idx)

                if difference <= k:
                    print(f'is {difference} <= {k}? TRUE')
                    return True
                else:
                    hashmap[val] = idx #update
        return False

            #     #create an arr cooresponding of that value
            #     #grab the keys of that value
            #     for dupe in hashmap.items():
            #         print(dupe)
        print(hashmap)
                

            


        # for i in range(len(nums)):
        #     print('this is i:', i)
        #     for j in range(i+1, numLength):
        #         print(j)
        #         val = abs(nums[i] - nums[j])
        #         if val <= k:
        #             print('THIS VAL:', val, 'is greater than K:', k)
        #             return True


        # return False