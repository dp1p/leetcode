class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort(key = lambda interval: interval[0])
        print(intervals)
        for interval in intervals:
            if merge == [] or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
               merge[-1][-1] = max(merge[-1][-1], interval[1])
        return (merge)