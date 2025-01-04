from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        for row in range(len(image)):
            
            for column in range(len(image)):
                image[row][column] = 0 if image[row][column] == 1 else 1
            
            res = [row[::-1] for row in image]

        return res
