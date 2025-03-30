class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def valid(m, h):
            #this to determine the minimum amount of bananas she can eat minimally 
            total_time = 0
            for num in piles:
                total_time += ceil((num / m))
                # print(f'rounded is {ceil((num / m))}')
                # print(num)
            # print(total_time, h)
            if total_time <= h:
                # print('VALID')
                return m #return the minimum amount of bananas koko can eat
            # print('INVALID')
            return float('inf')

        l = 1
        r = max(piles)
        k = float('inf')
        while l <= r:
            m = (l + r) // 2
            # print(m)
            check = valid(m, h)
            if check < k: #if the time is valid and under k
                k = check
                #can we get it smaller?
                r = m - 1
            elif check >= k:
                l = m + 1
        return k

            #we will pass m if its valid
    