class Solution:
    def equalFrequency(self, word: str) -> bool:
        #hashmap to iterate over the freq

        hashmap = Counter(word)

        for char in list(hashmap.keys()):
            hashmap[char] -= 1
            if hashmap[char] == 0:
                del hashmap[char]
            if len(set(list(hashmap.values()))) == 1:
                return True
            hashmap[char] += 1
        return False