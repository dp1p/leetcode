class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        greatestAvg = None
        j = 0 #increment in the else statement
        if len(nums) == k:
            sumArr = sum(nums)
            avg = sumArr / k
            return avg

        for i in range(len(nums)-k+1):
            if greatestAvg == None: #for the first instance
                array = nums[i:k+i]
                sumArr = sum(array) 
                avg = sumArr / k
                greatestAvg = avg
            else: #second instance + more . instead of creating a new arr, we just pop and push
                left = array.pop(0) #subtract the left
                sumArr -= left
                right = nums[k+j] #add the right from the nums from the nums
                array.append(right)
                sumArr += right
                j += 1  #this will increment everytime the else statement is called
                avg = sumArr / k
            
            if avg > greatestAvg:
                greatestAvg = avg

        return greatestAvg