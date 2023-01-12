class Solution:
    def findMinArrowShots(self, bus17: List[List[int]]) -> int:
        bus17.sort(key=lambda x:x[1])
        res, curEnd = 1,bus17[0] [1]
        for start,end in bus17:
            if start>curEnd:
                curEnd = end
                res += 1
        return res
