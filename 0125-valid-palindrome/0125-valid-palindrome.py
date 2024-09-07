class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        
        s = s.lower()
        
        for letter in s:
            if letter.isalpha():
                newStr += letter
            else:
                newStr = newStr.replace(letter, ' ')
            
        if len(newStr) == 0:
            return True

        left = 0
        right = len(newStr)-1

        if len(newStr) % 2 == 0:
            # print(f'right {right}')
            # print(f'left {left}')
            while left <= right:
               
                if newStr[left] == newStr[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        else:
            while left != right:
                if newStr[left] == newStr[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True