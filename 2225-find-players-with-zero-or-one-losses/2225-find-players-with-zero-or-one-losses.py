class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #lets first figure out who LOST ZERO TIMES game
        zeroLoss = set() #assume everyone who has won a game hasnt lost a game YET
        loss = {} #hashmap to keep track of the loss/ ,
        oneLoss = set() #we will check the loss hashmap and determine if players have more than one loss

        for player in matches: 
            zeroLoss.add(player[0]) #we will assume everyone who has won has lost zero matches
            loss[player[1]] = loss.get(player[1], 0) + 1
        #once we figure out the losses of the players we will now take a look at them and determine their result
        
        for player, totalLoss in loss.items():
            if player in zeroLoss: #if the player we assumed in 'zeroLoss' is in LOSS
                zeroLoss.remove(player)
            if totalLoss == 1: #if the player has only one loss
                oneLoss.add(player)

        return (sorted(zeroLoss)), (sorted(oneLoss))