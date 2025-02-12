class Solution:
    def firstUniqChar(self, s: str) -> int:
        #count the occurances
        #determine which letter came first
        hashmap = {}
        for character in s:
            hashmap[character] = hashmap.get(character, 0) + 1
        sort_items = dict(sorted(hashmap.items(), key=lambda item: item[1]))
        for ch in sort_items:
            if sort_items[ch] == 1:
                return s.index(ch)
            return -1