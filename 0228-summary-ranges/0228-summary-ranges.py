class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        track where the number starts to increase
        when the number is not increasing by 1, make it to a str aned return it
        also track if the number is the last iteration, because i will not print last num
        """
        incrementTracker = False
        answer = []
        if nums == []:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        for i in range(len(nums)-1): #prevent going out of range #0
            if incrementTracker == False:
                incrementTracker = True
                beginningNum = nums[i]
            
            if nums[i] + 1 != nums[i+1]:#if the next number is not incrementing
                if nums[i] == beginningNum: #if the nums[i] did not change
                    numStr = f'{beginningNum}'
                    answer.append(numStr)
                    incrementTracker = False #reset increment tracker
                else:
                    numStr = f'{beginningNum}->{nums[i]}' 
                    answer.append(numStr)
                    incrementTracker = False #reset increment tracker
                    
            
            
            #if this is the last index of the for loop, grab the last number in nums
            if i == len(nums)-2 and nums[i]+1 != nums[i+1]: #if it is not incrementing
                numStr = f'{nums[i+1]}'
                answer.append(numStr)
            
            if i == len(nums)-2 and nums[i]+1 == nums[i+1]: #if it is incrementing
                numStr = f'{beginningNum}->{nums[i+1]}'
                answer.append(numStr)

        return answer
