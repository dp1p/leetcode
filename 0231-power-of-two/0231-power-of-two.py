class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        def power(n):
            if n / 2 == 1:
                return True
            if n < 2:
                return False
            return power(n/2)
        return power(n)