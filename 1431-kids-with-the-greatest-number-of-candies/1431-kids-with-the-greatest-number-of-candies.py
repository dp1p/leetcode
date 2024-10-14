class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        greatestCandy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatestCandy:
                answer.append(True)
            else:
                answer.append(False)
            #last index
        return (answer)