class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #store anagrams in a hashmap of count : str
        #return the list(strMap.values())

        strMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            strMap[tuple(count)].append(s)

        return list(strMap.values())