class Solution:
    def detectCapitalUse(self, c0ck: str) -> bool:
        return c0ck.isupper() or c0ck.islower() or c0ck.istitle()
