'''
https://leetcode.com/problems/merge-intervals/submissions/
'''

class Solution:
    def merge(self, intervals):
        if len(intervals) <2 :return intervals
        intervals = sorted(intervals)
        # print(intervals)
        i = 1
        while True:
            # print(i)
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i][1],intervals[i-1][1])
                r = intervals.pop(i)
                # print(r)
            else:
                i+=1
            if i >= len(intervals):
                break
            # print(intervals)
        return intervals