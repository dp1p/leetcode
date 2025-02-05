class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left, right = 0, 1
        intervals.sort()
        print(intervals)
        while right < len(intervals):

            if intervals[left][1] >= intervals[right][0]:
                if intervals[left][1] >= intervals[right][1]:
                    intervals.pop(right)
                else:
                    intervals[left].pop(1)
                    intervals[left].append(intervals[right][1])
                    intervals.pop(right)
            else:
                left = right
                right += 1
            # print(intervals)
        return (intervals)