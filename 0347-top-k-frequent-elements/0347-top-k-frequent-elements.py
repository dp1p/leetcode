class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #two passes
        #hashmap to count
        #another loop to get the highest value
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        sorted_val = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_val[:k]
