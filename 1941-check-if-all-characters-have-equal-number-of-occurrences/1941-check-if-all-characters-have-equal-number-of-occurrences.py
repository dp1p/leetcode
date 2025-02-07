class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        val = [count for count in hashmap.values()]
        return len(set(val)) == 1
