from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = reduce(lambda x, y: x ^ y, nums)
                
        return res
    
    
solution = Solution()

print(solution.singleNumber([4, 1, 2, 1, 2, 4, 100]))