from operator import contains
from typing import List


def stringMatching(words: List[str]) -> List[str]:
    res = []
   
    for i in range(len(words)):
        for j in range(len(words)):
           if i == j:
               continue
           
           if words[i] in words[j]:
               res.append(words[i])
               break
                
    return res
    
    

print(stringMatching(["mass","as","hero","superhero"]))