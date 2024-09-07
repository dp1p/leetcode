class Solution:
    def containsDuplicate(self, nums):
        h = {}
        for idx, val in enumerate(nums):
            # print(idx, val)
            if val not in h.keys():
                h[val] = []
                h[val].append(idx)
            else:
                h[val].append(idx)
                break
                # print(h[val])
            
            # if len(h[val]) == 2:
            #     return True
        
        return (len(h[val])) == 2