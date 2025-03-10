class Solution:
    def reverseWords(self, s: str) -> str:
        #change it to a list
        #swap them using two pointers
        l, r = 0, len(s) - 1
        s = s.split()
        ans = []

        for word in s:
            word = word[::-1]
            ans.append(word)
        # print(ans)
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1
        
        
        ans = ' '.join(ans)
        # print(ans)
        return ans