class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        number = 1
        while len(answer) != n:
            if number % 3 == 0 and number % 5 == 0: #if the number is divisble by both 3 and 5
                answer.append('FizzBuzz')
            elif number % 3 == 0:
                answer.append('Fizz')
            elif number % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(number))
            number += 1
        return (answer)