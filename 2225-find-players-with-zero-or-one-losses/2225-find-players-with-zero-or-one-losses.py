class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #put it in a hashmap first
        wins = set() #we dont need to know how many they won, so we will use a set to avoid duplicates
        loses = {} #we want to know how many they lost
        result = [[], []] #[0] will be for zero loss, [1] will be for people with one loss

        for i in range(len(matches)): #ITERATE THRU THE MATCHES
            wins.add(matches[i][0])
            loses[matches[i][1]] = loses.get(matches[i][1], 0) + 1

        #we will check everuome that have lose first
        for item in loses.items():
            if item[1] == 1: #if the player has one loss
                result[1].append(item[0]) #add it to our result, at position

        #to check who won with zero loses
        for win in wins:
            if win not in loses: #as long as they are not in the loses
                result[0].append(win)
        print(result)
        
        result[0].sort()
        result[1].sort()

        return result