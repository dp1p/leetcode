class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        #since its sorted, we can move the pointers based on if its closer to the sum or further
        #we will move the left pointer if the added values is too small compared to the total
        #we will move the right pointer if the added values too big compared to the total
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            if numbers[left] + numbers[right] > target: #if the added up value is too big
                right -= 1
            else:
                left += 1
