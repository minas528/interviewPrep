class DetectSquares:

    def __init__(self):
        self.matrix = [[0]*1001 for i in range(1001)]
        

    def add(self, point: List[int]) -> None:
        pass
        self.matrix[point[0]][point[1]] += 1
        

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        ans = 0
        
        for i in range(1, 1001):
            if(x-i>=0 and x-i<=1000 and y-i>=0 and y-i<=1000):
                ans+=self.matrix[x-i][y]*self.matrix[x-i][y-i]*self.matrix[x][y-i]
            
            if(x+i>=0 and x+i<=1000 and y-i>=0 and y-i<=1000): 
                ans+=self.matrix[x+i][y]*self.matrix[x][y-i]*self.matrix[x+i][y-i]
            
            if(x+i>=0 and x+i<=1000 and y+i>=0 and y+i<=1000):
                ans+=self.matrix[x+i][y]*self.matrix[x+i][y+i]*self.matrix[x][y+i]
            
            if(x-i>=0 and x-i<=1000 and y+i>=0 and y+i<=1000):
                ans+=self.matrix[x-i][y]*self.matrix[x-i][y+i]*self.matrix[x][y+i];
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)