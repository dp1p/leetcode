class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # THREE POINTER APPROACH
        
        x, y = m-1, n-1
        for z in range(len(nums1)-1, -1, -1):

            #if one of them reaches zero
            if y < 0:
                break
            elif x < 0: #if x reaches zero, we know that y is sorted
                nums1[z] = nums2[y] #just replace the values from nums1
                y -= 1

            #if nums1 value is LESS than nums2
            elif nums1[x] < nums2[y]:
                nums1[z] = nums2[y] 
                y -= 1
            elif nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                x -= 1

            
        print(nums1)  
        return nums1
