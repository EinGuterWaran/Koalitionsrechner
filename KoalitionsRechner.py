from itertools import combinations
import numpy as np

# Input: election returns
# German: Wahlergebnisse
# Output: All purely mathematical coalition combinations that would have an absolute majority
# German: Alle rein rechnerische Koallitionskombinationen welche eine absolute Mehrheit hätten

## Input
er = [
        ["SPD", 26],
        ["CDU/CSU", 24],
        ["GRÜNE", 15],
        ["FDP", 12],
        ["AfD", 11],
        ["DIE LINKE", 5]
    ]
## End Input

def rSubset(arr, r):
      return list(combinations(arr, r))


if __name__ == "__main__":
    partyCombinations = []
    for x in range (len(er), 0, -1):
        partyCombinations.extend(rSubset(er, x))
    for partyCombination in partyCombinations:
        partyComb = np.array(partyCombination)
        
        voteSum = sum(partyComb[:, 1].astype(np.float))
        if voteSum >= 50:
            print(', '.join(str(x) for x in partyComb[:, 0]) +" with "+ str(voteSum)+ "%.")

