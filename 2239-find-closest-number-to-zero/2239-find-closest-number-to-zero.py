class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        current_closest = float('inf')
        for num in nums:
            if abs(num) == abs(current_closest):
                current_closest = max(num, current_closest)
            if 0 <= abs(num) < abs(current_closest):
                current_closest = num
        return current_closest
        """
        if abs(num) is close to zero compared to the current closest

            current_closest = num
        """