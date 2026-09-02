class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #workz
        return sorted(s) == sorted(t)