import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from custom_graph import Graph
from SAP import SAP
class WordNet:
    def __init__(self, synsets_file, hypernyms_file):
        self.synsets = self._load_synsets(synsets_file)
        self.hypernyms = self._load_hypernyms(hypernyms_file)
        self.G = self._create_graph()
        if self.G.has_cycle():
            raise ValueError('Graph is not a DAG')
        if not self.G.is_rooted():
            self.G.make_rooted()
        
        self.SAP = SAP(self.G)

    def _load_synsets(self, file):
        synsets = {}
        with open(file, 'r') as f:
            for line in f:
                fields = line.split(',')
                synset_id = int(fields[0])
                words = fields[1].split(' ')
                synsets[synset_id] = words
        return synsets

    def _load_hypernyms(self, file):
        hypernyms = {}
        with open(file, 'r') as f:
            for line in f:
                fields = line.split(',')
                hypernyms[int(fields[0])] = list(map(int, fields[1:]))
        return hypernyms
    
    def _create_graph(self):
        graph = Graph()
        
        # Add vertices for all synsets
        for synset_id in self.synsets:
            graph.add_vertex(synset_id)
            
        # Add edges based on the hypernyms
        for key, values in self.hypernyms.items():
            for value in values:
                graph.add_edge(key, value)
                    
        return graph

    def isNoun(self, word):
        for synset in self.synsets.values():
            if word in synset:
                return True
        return False

    def distance(self, nounA, nounB):
        synset_ids_A = self.synset_id(nounA)
        synset_ids_B = self.synset_id(nounB)

        if synset_ids_A and synset_ids_B:
            return self.SAP.length(synset_ids_A, synset_ids_B)
        else:
            raise ValueError("At least one of the nouns aren't in the graph!")

    def sap(self, nounA, nounB):
        synset_ids_A = self.synset_id(nounA)
        synset_ids_B = self.synset_id(nounB)

        if synset_ids_A and synset_ids_B:
            ancestor_id = self.SAP.ancestor(synset_ids_A, synset_ids_B)
            return " ".join(self.synsets[ancestor_id]) if ancestor_id else None
        else:
            raise ValueError("At least one of the nouns aren't in the graph!")
        
    def synset_id(self, noun):
        synset_ids = []
        for id, synset in self.synsets.items():
            if noun in synset:
                synset_ids.append(id)
        return synset_ids
    
if __name__ == "__main__":
    wn = WordNet('./test/synsets100.txt', './test/hypernyms100.txt')
    print(wn.sap('zymase', 'horror'))

