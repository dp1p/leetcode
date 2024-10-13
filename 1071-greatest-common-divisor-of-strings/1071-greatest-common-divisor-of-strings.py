class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def canConstruct(base, target):
            return base * (len(target) // len(base)) == target

        len_gcd = gcd(len(str1), len(str2))
        candidate = str1[:len_gcd]

        if canConstruct(candidate, str1) and canConstruct(candidate, str2):
            return candidate
        return ""
