class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #works
        return sorted(s) == sorted(t)