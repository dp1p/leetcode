class Solution:
    def hasSameDigits(self, s: str) -> bool:
        #use a while loop 
        #recurisvely calculate until they equal to double digits that are the same digits
        #first calulate all idxs 


        s = list(s) #<- store it here
        new_numbers = []
        i = 0
        while i < len(s) - 1:
            new_numbers.append((int(s[i]) + int(s[i+1])) % 10) #calculate
            i += 1 #iterate
            if i == len(s) - 1: #if i has reached the very end
                if i == 2:#we check if numbers is a length of two 
                    return new_numbers[0] == new_numbers[1]
                
                #else reset
                s = (new_numbers) #S IS NOW NUMBER
                i = 0 #i IS RESET
                new_numbers = [] #numbers is reset