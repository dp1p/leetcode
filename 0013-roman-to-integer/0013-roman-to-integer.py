class Solution:
    def romanToInt(self, s: str) -> int:
        #make a dictionary to represent the symbol to value
        #key could be the ROMAN NUMERALS, value can be the  NUMBERS

        #then when we check the value, we print the greatest NUMBER value equavlent to the the ROMAN NUM
        #we make str a list, whenever we add, we can just pop
        answer = 0 #where we will add our number
        i = 0 #to intialize
        roman = {
            "M" : 1000,
            "CM": 900,
            "D" : 500,
            "CD":400,
            "C" : 100,
            "XC": 90,
            "L" : 50,
            "XL":40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV": 4,
            "I" : 1,
        }
        listRoman = list(s)
        while listRoman != []:
            print(listRoman)
            if len(listRoman) >= 2 and (listRoman[i]+listRoman[i+1]) in roman: #first check the TWO indices are in our dict
                print('double found')
                romanValue = listRoman[i]+listRoman[i+1]
                # print(s[i]+s[i+1])
                # print(roman[romanValue])
                answer += roman[romanValue]
                print(answer)
                listRoman.pop(i) #when you pop, it decreases the length immediately
                listRoman.pop(i) #which is why i do not add +1, it skips
                doubleFound = True 
            else: #if the SINGULAR roman value is in our dictionary
                # print('single')
                # print(roman[s[i]])
                # print(s[i])
                # numberValue = roman[s[i]]
                # print(numberValue)
                answer += roman[listRoman[i]]
                print(answer)
                listRoman.pop(i)
                doubleFound = False
            if len(listRoman) == 1 and doubleFound == False:  #if we are at the last index:
                # print('last index')
                answer += roman[listRoman[i]]
                print(answer)
                listRoman.pop(i)
        # for i in range(len(s)-1): #to prevent going out of index
       
            
        
        # # if s[-1] in roman: #to check our last number
        # #     answer+=roman[-1]
        return answer


