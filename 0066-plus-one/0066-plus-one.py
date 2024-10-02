class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #convert list to str so the nums STACK, not add
        #convert STR to INT to add just 1
        #then convert INT to STR, THEN TO LIST
        strHolder = ""
        answer =[]
        for num in digits: #CONVERTING THE LIST TO A STR
           strHolder += str(num) #to stack the nums so they do not ACTUALLY add to eachother
        strHolder = int(strHolder) + 1 #converting STR TO INT to add one
                
        for char in str(strHolder): #we append the STR chars to a LIST, but making sure we convert the str to num
            answer.append(int(char))
        return answer

    