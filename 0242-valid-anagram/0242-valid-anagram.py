class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we will first put the letters in an hashmap
        #we will keep track of the letters, the key being the letter, value is the number times it pccurs
        #once we get the key values, we will compare if each key (character) matches from s == t

        if len(s) != len(t):
            return False
        hashmapS = {} #to store the character values in a dict
        hashmapT = {}
        for i in range(len(s)): #iterate through s, but also iterates through t because they have same length
            hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1 #checks if we have the char, if not, default is 0
            hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1
        j = 0
        print(hashmapT)

        return hashmapT == hashmapS
            