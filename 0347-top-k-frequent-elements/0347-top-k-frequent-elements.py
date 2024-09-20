class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        answer = []

        for i in range(len(nums)):
            if nums[i] not in h.keys():
                h[nums[i]] = 1
            else:
                h[nums[i]] += 1
        sortedH = (sorted(h.items(), key=lambda item:item[1], reverse=True)) #sorts by values
        # print(sortedH)
        #create another for loop to return answer for k num occurring the most

        for i in range(k):
            answer.append(sortedH[i][0]) #we are appending sortedH[i], grabbing item[0], which is the value
            

            
        # print(answer)
        return answer