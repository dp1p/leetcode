class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = [True]
        greatestCandy = candies[0]
        for i in range(1, len(candies)):
            if candies[i] + extraCandies > greatestCandy:
                answer.append(True)
                greatestCandy = candies[i]
            else:
                answer.append(False)
        return (answer)