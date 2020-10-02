'''
    https://leetcode.com/contest/weekly-contest-189/problems/number-of-students-doing-homework-at-a-given-time/
    1450. Number of Students Doing Homework at a Given Time
'''

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        for i, j in zip(startTime, endTime):
            
            if i<= queryTime<=j:
                res += 1
        return res