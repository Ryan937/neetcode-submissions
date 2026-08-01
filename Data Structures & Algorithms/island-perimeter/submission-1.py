class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nodes = deque()
        n = len(grid)
        m = len(grid[0])


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    nodes.append([i, j])

        result = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while nodes:
            curr = nodes.pop()

            for d in dirs:
                x = curr[0] + d[0]
                y = curr[1] + d[1]

                if x < 0 or y < 0 or x >= n or y >= m:
                    result += 1
                
                if x >= 0 and y >= 0 and x < n and y < m and grid[x][y] == 0:
                    result += 1

        return result