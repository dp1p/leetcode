class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #grab the shortest word
        #once we grab the shortest word, compare that prefix to everyone else
        
        shortestWord = None #empty string
        for word in strs: #we will grab the shortest
            if shortestWord == None or len(word) < len(shortestWord) :
                shortestWord = word
        
        letter = 0
        currPrefix = shortestWord

        for i in range(len(strs)): #grab the first word
            newPrefix = "" #reset everytime it iterate
            for letter in range(len(strs[i])):#iterate the word's letters, but stop at the new prefix len
                #print(strs[i][letter])
                if letter < len(currPrefix) and strs[i][letter] == currPrefix[letter]: 
                    newPrefix += shortestWord[letter]
                else:
                    #print(f'whoops do not match! current prefix is now {newPrefix}')
                    currPrefix = newPrefix
                    break
        #print(currPrefix)       
        return(currPrefix)
