class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a arr to store the substring
        #use a sliding window to iterate thru it
        #if the letter is not duplicate, then increase window
        #else, decrease window
        window = []
        greatestSize = 0

        for letter in s:
            print(f"letter is {letter}")
            if letter not in window:
                # print('Not in window')
                window.append(letter)
            else:
                # print(f'there is a duplicate {letter}')
                if len(window) > greatestSize:
                    greatestSize = len(window)
                    # print(f'greatest size is now {greatestSize}')
                window = [] #resets the window
                window.append(letter) #but still append the current letter
            
        if len(window) > greatestSize: #this statement is here if the 'else' statement is never triggered (as in no duplicates)
            greatestSize = len(window)
        # print(window)
        # print(greatestSize)
        return greatestSize