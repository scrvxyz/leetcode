class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        f = t = 0
        for e in s:
            if e == '1':
                t +=1
            else:
                f = min(f+1, t)
        return f
