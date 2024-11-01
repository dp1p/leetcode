class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #we will iterate and see how many numbers of them appear in each array
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        answer = [] #where we will append our point of 'intersection'
        # print(nums1)
        # print(nums2)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    answer.append(nums2[j])
                    continue #once the point of intersection is found, go to the next number in nums1
        return answer
            

