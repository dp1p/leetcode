class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #so we will be constantly adding from n
        #then we got to find when was the highest altitude
        answer = 0
        greatest = 0
        for num in gain:
            answer += num
            if answer > greatest:
                greatest = answer
        return (greatest)