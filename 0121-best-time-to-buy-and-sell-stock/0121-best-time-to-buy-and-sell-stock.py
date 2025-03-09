class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #when it comes to sliding window
        #we use left and right
        #left starts at 0
        #r will be the for loop

        #WHAT ARE WE DEALING WITH
        #we know that we have to find the max profit we can get
        #f we find any day that is greater than the lowest
        # subtract it
        #if there is a day that is lower than the lowest
        # lowest equal that value
        
        #variable window - as in it can change
        l = 0
        lowest = prices[0]
        profit = 0
        for r in range(len(prices)):
            if prices[r] < lowest: #we get the lowest price
                lowest = prices[r]
            elif prices[r] > lowest:
                profit = max(profit, prices[r] - lowest)
        return profit