class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #work
        return sorted(s) == sorted(t)