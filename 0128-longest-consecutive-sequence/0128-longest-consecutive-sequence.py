class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            streak = 1
            if num-1 not in nums:
                current = num
                streak = 1

                while current + 1 in nums:
                    streak += 1
                    current += 1
            
            longest = max(streak, longest)
        return longest