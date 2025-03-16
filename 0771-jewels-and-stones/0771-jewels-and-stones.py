class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        case sensitive
        we can place jewels in a hashmap
        """
        hashset = set(jewels)
        
        jewel = 0
        for s in stones:
            if s in hashset:
                jewel += 1
        return jewel