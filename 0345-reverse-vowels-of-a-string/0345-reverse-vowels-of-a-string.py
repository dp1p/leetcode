class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        IceCreAm

        vowels in here are
        i, e, e, A
        
        iterate twice
        first iteration is to get all the vowels
        next iteration is to replace every vowel
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_in_s = []

        for char in s:
            if char.lower() in vowels:
                vowel_in_s.append(char)
        vowel_in_s = vowel_in_s[::-1]
        s = list(s)
        print(vowel_in_s)
        for i in range(len(s)):
            if s[i].lower() in vowels:
                print(s[i])
                s[i] = vowel_in_s[0]
                vowel_in_s.pop(0)
        return ''.join(s)
