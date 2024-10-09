class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #we have word1, word2
        #alternate grabbing words from eachother
        #word1 always goes first
        #find out which one is longer
        #use a while loop, 
        #if word1 is not empty
        #   append word1 letter
        #pop
        #if word2 is not empty a
        #append word2 letter
        #pop
        #answer = ""
        #if word1 < word2:
        #   for 
        answer = ""
        word1 = list(word1)
        word2 = list(word2)
        i = 0
        while len(answer) < len(word1) + len(word2):
            if i < len(word1):
                answer += word1[i]
            if i < len(word2):
                answer += word2[i]
            i += 1
        return answer