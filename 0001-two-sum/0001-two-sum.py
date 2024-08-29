class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we know hashmaps are O(1) when it comes to key
        #we can subtract the target - num = difference
        #if difference is not in our dict, we can just store it as the difference the key, value is the index

        #we do it reverse, instead of having the index of nums as keys, we have the value of nums as key 
        hashMap = {} #store the difference in here in here

        i = 0
        for idx, value in enumerate(nums): 
            # print(idx, value)
            difference = target - value
            if difference not in hashMap: #if the difference not in the hashMap
                hashMap[value] = idx
                # print(hashMap)
            else:
                return idx, hashMap[difference] #hashMap[difference] will use `difference` as a key

        
        
        # for i in range(len(nums)): #now we will subtract the num[i] from target and find it in hashmap
        #     findNum = target - nums[i]
        #     if findNum in hashMap.values():
        #         return i, hashMap[i]


