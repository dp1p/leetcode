class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search is when you search through an ALREADY sorted arr of nums
        #and instead of searching for a number in O(n) (index & for loop), you search the number by...
        #splitting the arr in half, you grab the midpoint, see if target is greater or less than midpoint and 
        #split
        #you have low = index 0, high = last index, then once you split you move either or the pointers
        #low = midpoint + 1 
        #high = midpoint - 1
        low = 0
        high = len(nums)-1 #to prevent going out of index
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        #< means itll break when low is greater than or EQUAL
        while low <= high: #while low is less than high, it is <= cuz it will break when LOW is GREATER than high
            midpoint = (low + high) // 2 #we will get the midpoint by adding both nums, then dividing 2
            # print(midpoint)
            if nums[midpoint] == target:
                return midpoint #we return the index of the num
            elif nums[midpoint] < target: #if the midpoint is LESS than the target
                # print('low')
                low = midpoint + 1 #we will make low equal the midpoint, but go to the next index above midpoint
            elif nums[midpoint] > target:
                # print('high')
                high = midpoint - 1
        return -1 #if number is not found, return -1