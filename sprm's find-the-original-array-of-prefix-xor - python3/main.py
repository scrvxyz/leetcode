class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        op = [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
        return [pref[0]] + op
