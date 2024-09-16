class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a arr to store the substring
        #use a sliding window to iterate thru it
        #if the letter is not duplicate, then increase window
        #else, decrease window wherever it is duplications
        window = []
        greatestSize = 0

        for letter in s:
            if letter not in window:
                window.append(letter)
            else:
                greatestSize = max(greatestSize, len(window)) #check for the last substring length
                x = window.index(letter) # grab the index of the 1st time pops up, delete anything before it too
                window = window[x+1:] # start slicing to remove the duplicate and everything before it <-[start:stop]->
                window.append(letter) #but still append the current letter
            
        greatestSize = max(greatestSize, len(window)) #check for the last substring length
        return greatestSize