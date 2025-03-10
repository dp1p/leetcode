class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        def reverse(word):
            word = word[::-1]
            return word
        
        ans = list(map(reverse, s))
        
        return ' '.join(ans)