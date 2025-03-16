class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        case sensitive
        we can place jewels in a hashmap
        """
        hashmap = {}
        for j in jewels:
            hashmap[j] = 0
        
        jewel = 0
        for s in stones:
            if s in hashmap:
                jewel += 1
        return jewel