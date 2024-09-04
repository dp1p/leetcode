class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #make name and height key value
        #sort by height
        h = {}
        i = 0
        answer = []
        for height in heights:
            h[height] = names[i]
            i+=1
        i = 0

        heights = sorted(heights, reverse=True)

        for key in h.keys():
            answer.append(h[heights[i]])
            i+=1
        return answer
