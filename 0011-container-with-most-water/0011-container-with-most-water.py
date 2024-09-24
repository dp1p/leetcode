class Solution:
    def maxArea(self, height: List[int]) -> int:
        #we can intialize the greatestArea
        #we can use pointers, one starts at the end (left), the other starts at the beginning (right),
        #whatever pointer has the shortest height, both must be equal heights to store water (prevent overfill)
        #whatever has the shortest length, that pointer must move
        #if BOTH are equal, just move left

        #STOP if left = right
        left, right = 0, len(height) - 1
        greatestArea = 0 #intialize
        #DONT FORGET ! AREA = BASE * HEIGHT
        #WIDTH WILL BE THE INDEX'S
        while left != right: #while the pointers are not equal 
            if height[left] < height[right]: #if the value height[left] is less than value height[left]
                rightHeight = height[left] #rightHeight is now equal to the value of left
                width = right - left
                if (rightHeight * width) > greatestArea: #if new area is greater than the current area
                    greatestArea = rightHeight * width
                    print(f"greatestArea is {greatestArea}")
                    left += 1 #we move the left pointer because it is the shortest
                else:
                    left += 1
            elif height[left] > height[right]: #if left is greater than right
                leftHeight = height[right] #leftHeight is now equal to the value of right
                width = right - left
                if (leftHeight * width) > greatestArea: #if current area is greater than the current area
                    greatestArea = (leftHeight * width)
                    print(f"greatestArea is {greatestArea}")
                    right -= 1 #we move the right pointer because it is the shortest
                else:
                    right -= 1
            elif height[left] == height[right]: #if left is greater than right
                rightHeight = height[left] #value is now equal to the value of left (doesnt matter what side)
                width = right - left
                if (rightHeight * width) > greatestArea: #if current area is greater than the current area
                    greatestArea = (rightHeight * width)
                    print(f"greatestArea is {greatestArea}")
                    left += 1 #we move the left pointer 
                else:
                    left += 1
        return greatestArea