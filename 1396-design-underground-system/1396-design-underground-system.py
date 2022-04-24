class UndergroundSystem:

    def __init__(self):
        self.checks = {}
        self.tracker = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = (stationName, t)
                

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        station, start = self.checks[id]
        key = (station, stationName)
        if key in self.tracker:
            count, sum_ = self.tracker[key]
            self.tracker[key] = (count+1, sum_ + (t - start))
        else:
            self.tracker[key] = (1,  (t - start))
        
        del self.checks[id]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, sum_ = self.tracker[(startStation, endStation)]
        return sum_/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)