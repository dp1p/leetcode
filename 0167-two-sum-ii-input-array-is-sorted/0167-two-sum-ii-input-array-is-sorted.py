class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use hashmap
        #subtract index from target to get a difference
        #if difference not in there, append it to hashmap
        h = {} #store difference
        for i in range(len(numbers)):
            difference = target - numbers[i] #
            if numbers[i] in h: #if the difference is in keys #is 7 in there? #is 2 in there
                # print(f"{difference} is in hashmap")
                # print(f"VALUES {difference}, {numbers[i]}")
                return ([h[numbers[i]]+1, i+1])
            else:
                # print(f"{target} - {numbers[i]} != {difference}") #store 7
                h[difference] = i
                # print(h)