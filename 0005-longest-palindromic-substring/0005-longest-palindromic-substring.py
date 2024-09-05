class Solution:
    def longestPalindrome(self, s: str) -> str:
        #use a INCREASING window
        #if there is a word that is a paladrome of window of 2, then increase size of window and restart
        #after iteration of i, then go to the next letter

        if len(s) == 1:
            return s

        greatestPalindrome = '' #store the empty palidrome
        for i in range(len(s)-1):
            windowSize = 1 #reset the window size to length of the paldinrome
            for windowSize in range(1, len(s) - i + 1):
                window = s[i:i+ windowSize]
                if window == window[::-1] and len(window) > len(greatestPalindrome):
                    greatestPalindrome = window
                    
                    
        # print(f'the greatest palindrome is: {greatestPalindrome}')
        return greatestPalindrome