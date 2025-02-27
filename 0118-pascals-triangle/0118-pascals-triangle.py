class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #we are given 1
        #num rows determine how many rows are in the trianle
        
        #use a while loop to iterate the num rows
        #arr increases by 1
        #we know the outer edges will always be 1
        #if arr is empty
        #add 1 to it
        #if arr is not 0 or is not the end of the arr
        #add nums[i], nums[i+1] and append it to a new arr

        """
        answer = []
        counter = 0
        while counter < numRows:
            res = []
            counter + 1
            if counter < 1:
                res = [1]
                answer.append(res)
            elif counter < 2:
                res = [1,1]
                answer.append(res)
            else:
                while res < counter:
                    prevLevel = answer[-1]
                    if res == []:
                        res.append(1)
                    elif res == counter - 1:
                        res.append(1)
                    elif:
                        res.append(prevLevel[i] + prevLevel[i+1])
                answer.append(res)

            
        """
        #1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,29,21,22,23,24

        answer = []
        counter = 0
        while counter < numRows:
            i = -1
            res = []
            counter += 1
            if counter == 1:
                #print('less than 1')
                res = [1]
            elif counter == 2:
                #print('less than 2')
                res = [1,1]
            else:
                while True:
                    prevLevel = answer[-1] #[1, 1]
                    if res == []:
                        res.append(1) #[1]
                    elif len(res) == counter-1:
                        res.append(1)
                        break
                    else:
                        i += 1
                        #print('nice')
                        res.append(prevLevel[i] + prevLevel[i+1]) #iterate 
                        print(res)
            answer.append(res)
            # print('answer')
            # print(answer)
        return answer