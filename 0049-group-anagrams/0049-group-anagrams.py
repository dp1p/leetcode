class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s not in hashmap:
                hashmap[s] = []
            
            hashmap[s].append(word)
        listt = list(hashmap.values())
        return(listt)