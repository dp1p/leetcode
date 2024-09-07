class Solution:
    def containsDuplicate(self, nums):
        h = {}
        for idx, val in enumerate(nums):
            if val not in h.keys():
                h[val] = []
                h[val].append(idx)
            else:
                return True
        return False