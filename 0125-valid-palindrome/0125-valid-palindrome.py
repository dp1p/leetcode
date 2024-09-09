class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1. remove spaces 
        #2. make everything lowercase
        #3. left and right pointers
        #left starts at s[0]
        #right start at len(str)-1 (to prevent out of idx)

        #4. to check left and right 
        
        #for i in s:
            #if len(s) % 2 == 0:  #if even
        
        newStr = ''
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                newStr += letter

        newStr = newStr.lower()
        left = 0
        right = len(newStr)-1
        print(newStr)


        if len(newStr) % 2 == 0: #if newStr is even
            while left < right: #where to stop
                if newStr[left] == newStr[right]: #to check letters
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        else: #else if its not even
            while left != right:
                if newStr[left] == newStr[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
                
                






        