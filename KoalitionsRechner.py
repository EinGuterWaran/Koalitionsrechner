from itertools import combinations
import numpy as np

# Input: Wahlergebnisse
# English: Election returns
# Output: Alle rein rechnerischen Koalitionsmöglichkeiten welche eine absolute Mehrheit ergeben würden
# English: All coalition combinations that would have an absolute majority

## Instesamt Sitze
sitze = 735
# Anzahl Sitze pro Partei
er = [
        ["SPD", 206],
        ["CDU/CSU", 196],
        ["GRÜNE", 118],
        ["FDP", 92],
        ["AfD", 83],
        ["DIE LINKE", 39]
    ]
#Sitzanzahl wird in Prozent umgerechnet
for el in er:
    el[1] = round(el[1]/sitze*100,5)

#Hilfsfunktion welche Kombinationen der Länge r von Parteien zurückgibt
def rSubset(arr, r):
      return list(combinations(arr, r))

if __name__ == "__main__":
    coalInd = 1
    partyCombinations = []
    for x in range (len(er), 0, -1):
        partyCombinations.extend(rSubset(er, x))
    for partyCombination in partyCombinations:
        partyComb = np.array(partyCombination)
        voteSum = sum(partyComb[:, 1].astype(float))
        if voteSum > 50:
            print("#"+str(coalInd)+": "+', '.join(str(x) for x in partyComb[:, 0]) +" mit "+ str(round(voteSum,2))+ "%.")
            coalInd += 1

