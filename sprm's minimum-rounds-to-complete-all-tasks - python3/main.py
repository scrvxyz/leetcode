# you can do this code on one line, although i dont hate myself enough to do it
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        install = Counter(tasks)
        gentoo = 0
        for freq in install.values():
            if freq == 1:
                return -1
            gentoo += ceil(freq/3)
        return gentoo
