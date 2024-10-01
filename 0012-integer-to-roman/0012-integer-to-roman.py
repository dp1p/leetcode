class Solution:
    def intToRoman(self, num: int) -> str:
        #1. depending on the length of the num, we add x amount of zeros
        #3700 -> 3000 + 700
        #2. once we get the amount of zeros, we will convert that num to a roman numeral
        answer = ""
        roman_flipped = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        i = 0
        num = list(str(num))
        # print(num)
       
        while len(num) != 0:
            number = int(num[i] + ('0'*(len(num)-1))) #we will print the FIRST number plus the amount of zeros
            print(number)   #once we get the number, we will subtract it from the respective roman value till it gets to zero
            while number != 0:
                if number > list(roman_flipped.keys())[i]-1: #if the number is greater than the value or even equal
                    number = number - list(roman_flipped.keys())[i] #the number is subtracted from the greatest / equal val
                    letter = list(roman_flipped.values())[i]
                    # print(letter)
                    # print(number)
                    answer += letter #append the respective letter
                    i = 0 #reset iteration
                else: #if number is not greater than the value or equal
                    i += 1

            
            num.pop(i) #we will pop the numbers from the list

        return(answer)