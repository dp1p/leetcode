class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """ 
        abab

        sliding window

        if letter is not in p 
        go to the next one
        FIXED WINDOW
        window = []
        ans = []
        for i in range(len(s))
            window.append(s[i])
            beginningindex = i
            while window < len(p):
                window.append(s[i])
            if window == p or window[-1] == p:
                ans.append(i)
            window.pop(0)
            
            if s[i] in p:
                add it to window
                keep track of the beginning index
            check if window is the same length as P AND is an anagram
                if it is, add the beginning index to ans
            if window > p OR window p is equal to the length of p AND != p:
                move index till it is equal its less than 
        """
        if len(p) > len(s):
            return []
        #FOR MAPPING / FREQ COUNTER of P
        hashmap_p = {}
        for letter in p:
            hashmap_p[letter] = hashmap_p.get(letter, 0) + 1


        i = 0
        #TRAVERSING S
        #still need a window to understand what letter we are popping
        window = []
        ans = []
        hashmap_s = {}
        while i < len(s): #0
            while len(window) < len(p): #[c, b, z]
                window.append(s[i]) 
                hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
                i += 1
            if hashmap_s == hashmap_p:
                ans.append(i-(len(p)))
            removee = window.pop(0)
            hashmap_s[removee] -= 1
            if hashmap_s[removee] == 0:
                del hashmap_s[removee]

        return (ans)