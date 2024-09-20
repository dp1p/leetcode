class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        we will use a for loop to iterate
            two pointer method
            sell pointer - will be the one moving, sells if it is higher, value will be called 'profit'
            buy pointer, reassign itself to a index if there is a lower number assign it'profit'                
            sell pointer will be starting at wherever buy pointer is
            if profit <= the current profit
                currentprofit = profit
        """
        buyPointer = prices[0] #finds where the stock is at its lowest
        sellPointer = 0 #sells where the stock increases, will be moving
        profit = 0 # sell - buy
        
        for i in range(1, len(prices)): #starting at index 1
            if prices[i] < buyPointer: #if the next day the price is lower than yesterday #5 < 1
                buyPointer = prices[i]
            else:
                sellPointer = prices[i] #we sell when the price is higher on the next day
                currentProfit = sellPointer - buyPointer
                if currentProfit > profit:
                    profit = currentProfit
        
        return profit
                