class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #put it in a hashmap first
        wins = set() #we dont need to know how many they won, so we will use a set to avoid duplicates
        loses = {} #we want to know how many they lost
        result = [[], []] #[0] will be for zero loss, [1] will be for people with one loss

        for i in range(len(matches)): #ITERATE THRU THE MATCHES
            wins.add(matches[i][0])
            loses[matches[i][1]] = loses.get(matches[i][1], 0) + 1
        # print(wins)
        # print(loses)
        #we will check everuome that have lose first
        for item in loses.items():
            if item[1] == 1: #if the player has one loss
                result[1].append(item[0]) #add it to our result, at position
        
        #to check who won
        for win in wins:
            if win not in result[1] and win not in loses.keys():
                result[0].append(win)
        # print(result)
        
        # #then we will check for anyone that has won AND is not in the ban list AND is not the result[1]
        # for item in wins.items():
        #     if item[0] not in banlist and item[0] not in result[1]:
        #         result[0].append(item[0])

        result = [sorted(result[0]), sorted(result[1])]
        return (result)