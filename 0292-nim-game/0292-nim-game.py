class Solution:
    def canWinNim(self, n: int) -> bool:
        #you can remove 1 - 3 stones at a time
        #1 - 3 you can win
        #4 you cannot win because the other person will bee winning
        #assuming if you go first, if you subtrac
        #5 false
        #6 false
        #check how many stones are left over
        #if stone left over === 3, 2, 1 return false
        #if 0, return true
        #always subtract three
        if n % 4 == 0:
            return False
        else:
            return True