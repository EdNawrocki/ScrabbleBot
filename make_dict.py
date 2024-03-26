import pickle

Dict = {}
s = set()
with open('dictionary.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        s.add(line)
        sortline = line
        alphabetized = ''.join(sorted(sortline))
        if alphabetized in Dict:
            Dict[alphabetized].append(line)
        else:
            Dict[alphabetized] = []
            Dict[alphabetized].append(line)

with open('Dict.pickle', 'wb') as handle:
    pickle.dump(Dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('ValidList.pickle', 'wb') as handle:
    pickle.dump(s, handle, protocol=pickle.HIGHEST_PROTOCOL)