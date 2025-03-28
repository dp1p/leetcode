class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []
        i = 0
        j = 0
        while i < len(temperatures):
            if j == len(temperatures):
                answer.append(0)
                stack = []
                j = i + 1
                i += 1
            elif temperatures[i] < temperatures[j]:
                answer.append(len(stack))
                stack = []
                j = i + 1
                i += 1
            else:
                stack.append(temperatures[j])
                j += 1
        return answer