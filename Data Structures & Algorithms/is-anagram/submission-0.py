class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ar1, ar2 = list(s), list(t)
        ar1.sort()
        ar2.sort()
        return ar1 == ar2