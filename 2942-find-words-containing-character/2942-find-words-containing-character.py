class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            for word in words[i]:
                if word == x:
                    result.append(i)
                    break
        print(result)
        return result
