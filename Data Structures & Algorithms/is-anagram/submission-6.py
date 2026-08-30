class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #TESTT 
        return sorted(s) == sorted(t)