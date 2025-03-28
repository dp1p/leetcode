class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        need to search vertically
        see if target is between the first and last index

        once that number is that target, then return it
        """

        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            print('helo')
            if matrix[m][0] <= target <= matrix[m][-1]:
                left = 0
                right = len(matrix[m]) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if matrix[m][middle] < target:
                        left = middle + 1
                    elif matrix[m][middle] > target:
                        right = middle - 1
                    else:
                        return True
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        return False