class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #iterate over ops
        #ans = []

        """
        match
            if its digit
                #add to ans
            if its c
                #pop from our list
                #if its empty, do not pop
            if its d
                double the prev number
                append it to ans
            if its +
                grab the sum of the two previous scores
        return ans if len(ans) > 1 else 0
        """
        ans = []
        for op in operations:
            match op:
                case str() if op.lstrip('-').isdigit():
                    ans.append(int(op))
                case 'C':
                    ans.pop()
                case 'D':
                    double_num = ans[-1] * 2
                    ans.append(double_num)
                case '+':
                    summ = ans[-1] + ans[-2]
                    ans.append(summ)
                case _:
                    print('Invalid Operation.')
        return sum(ans) if len(ans) > 1 else 0