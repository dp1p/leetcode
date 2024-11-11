class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while left != len(numbers)-1:
            if left == right: #if both pointers are at the same index
                right += 1
            elif numbers[left] + numbers[right] == target:
                return sorted([left+1, right+1])
            elif right == len(numbers)-1: #if right has reached the end of the array
                right = 0
                left += 1
            else: #if they do not sum up to the target
                right += 1