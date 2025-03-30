class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        hashmap = {}
        arr = []
        for word in s1:
            hashmap[word] = hashmap.get(word, 0) + 1
        for word in s2:
            hashmap[word] = hashmap.get(word, 0) + 1
        for word in hashmap:
            if hashmap[word] == 1:
                arr.append(word)
        return arr
