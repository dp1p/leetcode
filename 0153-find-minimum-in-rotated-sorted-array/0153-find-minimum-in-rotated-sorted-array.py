class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        need to find the minimum 

        we can look at the middle

        compare if the middle number is greater than right

        [3,4,5,1,2]
        L    M    R

        is 5 < 2?
        NO!
        move left pointer cuz we want to get closer to the middle number


        [1,2]
        is 1 less than 2?

        YES!

        move right pointer cuz we know we are closer to getting a smalelr number

        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < nums[right]: #we want to find the mnimum number
                right = middle
            elif nums[middle] >= nums[right]:
                left = middle + 1
        return nums[middle]
        
