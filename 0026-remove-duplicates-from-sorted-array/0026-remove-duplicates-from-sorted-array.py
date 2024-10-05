class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #once we find the duplicate, store that value in a new array?
        #then once we find all the duplicates, we slowly start deleting the values in the old arr
        #replace it with an underscore

        k = len(nums)
        seen = []
        #to add the duplicate values in here
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                seen.append(nums[i])
        # print(seen, nums)

        #IF IT IS EMPTY
        if seen == []:
            return len(nums)
        #to then POP the values in the original arr
        seenLen = len(seen)
        i = 0
        # print(seen, nums)
        while len(nums) > len(seen): #we know that the length of nums is greater than duplicates
            if nums[i] == seen[0]:
                nums.pop(i)
                seen.pop(0)
                i = 0 #when you pop, you essentially decrease the len(nums) as well.
            else:
                i += 1 #if the number isnt a duplicate, just go to the next number
            if seen == []:
                break
            

        return k-seenLen