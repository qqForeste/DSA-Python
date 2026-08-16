class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1

        
        maxfruits = 0

        for left in range(len(fruits) - 1):
            ftype = set()

            fruitspicked = 1

            right = left + 1

            ftype.add(fruits[left])

            while right < len(fruits):
                
                if not fruits[right] in ftype:
                    if len(ftype) < 2:
                        ftype.add(fruits[right])
                    else:
                        print("too big")
                        break                
                
                fruitspicked += 1
                right += 1
            
            print(ftype)
            maxfruits = max(maxfruits, fruitspicked)

        return maxfruits

