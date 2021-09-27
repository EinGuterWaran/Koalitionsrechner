from itertools import combinations
import numpy as np

# Input: Wahlergebnisse
# English: Election returns
# Output: Alle rein rechnerischen Koalitionsmöglichkeiten welche eine absolute Mehrheit ergeben würden
# English: All coalition combinations that would have an absolute majority

## Input
er = [
        ["SPD", 25.7],
        ["CDU/CSU", 24.1],
        ["GRÜNE", 14.8],
        ["FDP", 11.5],
        ["AfD", 10.3],
        ["DIE LINKE", 4.9]
    ]
## End Input

def rSubset(arr, r):
      return list(combinations(arr, r))

coalInd = 1
if __name__ == "__main__":
    partyCombinations = []
    for x in range (len(er), 0, -1):
        partyCombinations.extend(rSubset(er, x))
    for partyCombination in partyCombinations:
        partyComb = np.array(partyCombination)
        
        voteSum = sum(partyComb[:, 1].astype(np.float))
        if voteSum > 50:
            print("#"+str(coalInd)+": "+', '.join(str(x) for x in partyComb[:, 0]) +" mit "+ str(round(voteSum,2))+ "%.")
            coalInd += 1

