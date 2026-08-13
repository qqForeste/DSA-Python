class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a hashmap of all the numbers and their frequencies
        #make buckets and sort where index = frequency for each number
        #iterate through the buckets until k = 0 or n > -1

        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1
        
        n = len(nums)

        buckets = [[] for _ in range(n + 1)]

        for num, frequency in frequencies.items():
            buckets[frequency].append(num)
        

        res = []

        while n > -1 and k > 0:
            if buckets[n]:
                res.append(buckets[n].pop())
                k -= 1
            else:
                n -= 1
            
        return res


        