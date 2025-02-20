class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if i < 0 or j < 0 or j >= x or i >= y or grid[i][j] != '1':
                return
            else:
                grid[i][j] = 0 #mark as visited
            dfs(i+1, j) #up
            dfs(i-1, j) #down
            dfs(i, j-1) #left
            dfs(i, j+1) #right

        count = 0
        x = len(grid[0])
        y = len(grid)
        total = []
        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count

