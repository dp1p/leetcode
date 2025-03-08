class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity = sorted(capacity, reverse=True)
        i = 0
        count = 0
        while total_apples > 0:
          total_apples -= capacity[i]
          i += 1
          count += 1
        return count
