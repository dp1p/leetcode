class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #we can have n as a counter
        i = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: #we first make sure the pot is empty
                if i == 0 or flowerbed[i-1] != 1: # we check the left of the pot or if its the first iteration
                    if i == len(flowerbed)-1 or flowerbed[i+1] != 1: # we check the right of the pot / last iter
                        n -= 1 #subtract n
                        flowerbed[i] = 1 #we change the flowerbed 0 to 1 (just an extra step)
        # print(flowerbed)
        return n <= 0