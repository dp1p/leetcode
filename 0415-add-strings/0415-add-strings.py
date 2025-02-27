class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #convert a single digit to a str, start reversed order
        #make each of them a list
        #pop if we can from each number
        #add them together
        #if the digit is a two digit number, make it a carry can use % 10 to get last digit

        num1 = list(num1)
        num2 = list(num2)
        ans = []
        carry = 0
        while num1 or num2 or carry != 0: #while these have numbers
            num_1 = num1.pop() if num1 else 0
            num_2 = num2.pop() if num2 else 0
            
            total = int(num_1) + int(num_2) + carry
            print(total)
            if total > 9:
                carry = total // 10 # to get the carry
                total = total % 10 # get the last digit
            else:
                carry = 0
            ans.append(str(total))
        return (''.join(ans[::-1]))

