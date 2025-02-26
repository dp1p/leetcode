class Solution:
    def hasSameDigits(self, s: str) -> bool:
        #use a while loop 
        #recurisvely calculate until they equal to double digits that are the same digits
        #first calulate all idxs 
        s = list(s) #<- store it here
        numbers = []
        i = 0
        while i < len(s) - 1:
            numbers.append((int(s[i]) + int(s[i+1])) % 10)
            i += 1 
            if i == len(s) - 1: #we check if numbers is a length of two tho
                if i == 2:
                    i = 0
                    print(numbers)
                    return numbers[i] == numbers[i + 1]
                s = (numbers) #S IS NOW NUMBER
                i = 0 #I IS RESET
                numbers = []