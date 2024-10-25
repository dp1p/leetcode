class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort the words
        #if the sorted word is matching to a existing anagram (that is sorted), we add the sorted word to the key
        #key will be { sorted word } --- value will be { unsorted word }
        hashmap = {} #to store our word values
        for word in strs:
            sortedWord = sorted(word)
            if tuple(sortedWord) not in hashmap:
                #print(str(sortedWord))
                hashmap[tuple(sortedWord)] = [word]
            else:
                hashmap[tuple(sortedWord)] += [word]
        #print(list(hashmap.values()))
        return(list(hashmap.values()))