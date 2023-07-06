import os
from wordnet import WordNet
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class OutCast:
    
    def __init__(self, wordnet):
        self.wordnet = wordnet

    def outcast(self, nouns):
        outcast = None
        max = 0
        dist = float("inf")
        for noun in nouns:
            dist = 0
            for noun2 in nouns:
                if noun is not noun2:
                    dist += self.wordnet.distance(noun, noun2)
            
            if dist > max:
                max = dist
                outcast = noun

        return outcast
            

if __name__ == "__main__":
    wn = OutCast(wordnet= WordNet('./test/synsets.txt', './test/hypernyms.txt'))
    print(wn.outcast(["horse", "zebra", "cat", "bear", "table"]))


