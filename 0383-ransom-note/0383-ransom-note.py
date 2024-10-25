class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #ransomNote must be created from magazine, else false
        #we will iterate ransom note
        #if letter in ransomNote is found in magazine, we pop in both, reset the counter
        #if ransomNote is empty, return true
        #   else return False

        #WITHOUT USING BUILT IN METHODS
        i = 0
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        while i < len(magazine):
            # print(ransomNote)
            # print(magazine)
            if ransomNote == []:
                break
            elif ransomNote[0] == magazine[i]:
                # print(f'letters found, popping {ransomNote[0]} and {magazine[i]}')
                ransomNote.pop(0)
                magazine.pop(i)
                i = 0 #reset if we found where to pop
            else:
                print('letter not found')
                i += 1


        return ransomNote == []

