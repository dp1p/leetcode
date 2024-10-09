class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #use three pointers (BASE, left, right)
        #sort the nums
        nums = sorted(nums)

        answer = {} 
        for i in range(len(nums)):
            # print(f"base {i}")
            left = i + 1 #to always reset for each iteration and start at i for better efficency 
            right = len(nums)-1
            while left < right:
                if left == right:
                    break

                pointers = (nums[i], nums[left], nums[right]) 

                if nums[i] + nums[left] + nums[right] == 0: #if sum is equal to zero
                    if tuple(sorted(pointers)) not in answer: #if the pointers not in our hashmap
                        answer[tuple(sorted(pointers))] = 1 #insert into hashmap (key must be immutable)
                        # print(f'adding {pointers} to key')
                    left += 1


                    #once we add a triplet, we will check if the next num on the right is a dupe
                    while left < right and nums[right] == nums[right-1]: #IF THE NEXT NUMBER IS A DUPE
                        right -= 1
                    # print(f'duplicate from the right')
                    # print(f'sum is {nums[i] + nums[left] + nums[right]} moving right')

                    while left < right and nums[left] == nums[left+1]: #IF THE NEXT NUMBER IS A DUPE
                        left += 1
                    # print(f'sum is {nums[i] + nums[left] + nums[right]} moving left')

                elif nums[i] + nums[left] + nums[right] > 0: #if the sum is a positive number
                    right -= 1 #we move the right pointer
                elif nums[i] + nums[left] + nums[right] < 0: #if the number is a negative number
                    left += 1
  
        print(answer)
        return answer

        #KEY TAKEAWAYS
        #order of operation matters
        # while left < right and nums[left] == nums[left+1]: #this makes sures it is in bounds FIRST
