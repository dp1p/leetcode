class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        currentGreatest = 0
        greatest = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        for items in hashmap.items():
            # print(items)
            if items[1] > currentGreatest:
                currentGreatest = items[1]
                greatest = items[0]
        return (greatest)