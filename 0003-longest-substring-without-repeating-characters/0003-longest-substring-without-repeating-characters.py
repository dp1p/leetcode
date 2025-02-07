class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_sub = 0
        left = 0
        if len(s) == 1:
            return 1
        
        for right in range(len(s)):
            if s[right] not in substring:
                substring.add(s[right])
                print(substring)
            else:
                max_sub = max(max_sub, len(substring))
                print(max_sub)
                while s[right] in substring: #how do i iterate till it hits s[i]
                    substring.remove(s[left])
                    left += 1
                substring.add(s[right])
        return  max(max_sub, len(substring))