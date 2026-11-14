class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        splitS, splitT = list(s), list(t)
        splitS.sort()
        splitT.sort()
        return splitS == splitT