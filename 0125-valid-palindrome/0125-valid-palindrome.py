class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make it a list, because strs are immutable
        #remove all white spaces, puncuations, and as well as capitalizations
        #if str[::-1] == str 
        #return true
        #else it is false
        answer = '' #make answer empty str
        s = s.lower() #lowercase
        specialChars = [',', '.', ':', ' ', '.', '@', '#', '_', '', '`', "'", "{", '}', '/', '[', ']', "\"", "\\", "-", "?", ";", "!"]
        for i in range(len(s)):
            if s[i] in (specialChars):
                # print(f'SPECIAL CHARACTER FOUND: || {s[i]} ||')
                pass
            else:
                answer+=(s[i])
        print(answer)
        return answer[::-1] == answer
        

        # listStr = list(s.lower().replace(',','').replace(':','').replace(' ','').replace('.','').replace('@','').replace("#",'').replace('_',''))