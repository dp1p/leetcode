class Solution:
    def longestPalindrome(self, s: str) -> str:
        #use a INCREASING window
        #if there is a word that is a paladrome of window of 2, then increase size of window and    restart
        #after iteration of i, then go to the next letter

        if len(s) == 1:
            return s

        greatestPalindrome = '' #store the empty palidrome
        for i in range(len(s)-1):
            print(f'ITERATION {i} || GREATEST SIZE CURRENTLY {len(greatestPalindrome)}')
            for j in range(len(s)):
                window = s[i:j+1]
               
                if len(window) > len(greatestPalindrome):
                    if window == window[::-1] and len(window) > len(greatestPalindrome):
                        # print(window)
                        # print(f'{window} IS PALDROMIC')
                        greatestPalindrome = window
                    # else:
                        # print("NOT PALIDROMIC")

        # print(f'the greatest palindrome is: {greatestPalindrome}')
        return greatestPalindrome