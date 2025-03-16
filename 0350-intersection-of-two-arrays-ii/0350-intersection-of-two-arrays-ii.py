class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a hashset
        #if number is in that set, append that to our ans arr
        #   if there is the same number, do not add it
        #
        hashmap = {}
        for num in nums1:
            hashmap[num] = hashmap.get(num, 0) + 1
        ans = []
        for num in nums2:
            if num in hashmap:
                ans.append(num)
                hashmap[num] -= 1
                if hashmap[num] == 0:
                    del hashmap[num]
            if len(hashmap) == 0:
                return ans
        return ans
        #brute force
        # ans = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums2[j] == nums1[i]:
        #             ans.append(nums2[j])
        #             nums2.pop(j)
        #             break
        # return ans