class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #as long as they do not overlap
        #sort it
        #if intervals[1] overlaps intervals[i+1][1]
        #return false
        sorted_items = sorted(intervals, key= lambda intervals: intervals[0])
        # print(sorted_items)
        for i in range(len(sorted_items)-1):
            # print(sorted_items[i], sorted_items[i+1])
            if sorted_items[i][1] > sorted_items[i+1][0]:
                return False
            
        return True