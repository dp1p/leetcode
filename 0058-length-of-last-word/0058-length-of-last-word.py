class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #remove all white spaces (strip())
        #split them to be a list
        #grab the last word

        s = s.split()
        return len(s[-1])
        