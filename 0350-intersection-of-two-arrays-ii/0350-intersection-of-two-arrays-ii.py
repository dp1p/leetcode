class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a hashset
        #if number is in that set, append that to our ans arr
        #   if there is the same number, do not add it
        #
        # if len(nums1) >= len(nums2):
        #     shortest = nums2
        #     longest = set(nums1)
        # else:
        #     shortest = nums1
        #     longest = set(nums2)
        # ans = []
        # for num in shortest:
        #     if num in longest: #if the number is also in longest
        #         ans.append(num)
        # return ans
        #brute force
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    ans.append(nums2[j])
                    nums2.pop(j)
                    break
        return ans