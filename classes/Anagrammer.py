import pickle

with open('../Dict.pickle', 'rb') as handle:
    word_list = pickle.load(handle)

def GetAnagrams(s, l):
    if l < 2:
        return ''
    keys = list(set(GetAlphagrams(s, l, 0, '')))
    return keys

def GetAnagramsWith(s, l, includes):
    if l < 2:
        return ''
    includes = ''.join(sorted(includes))
    s = ''.join(sorted(s))
    keys = list(set(GetAlphagramsWith(s, l, 0, 0, includes, '')))
    return keys

def GetAlphagrams(s, l, i, current):
    if len(current) == l:
        return [current]
    if i >= len(s):
        return []
    #Don't take current letter
    nt = GetAlphagrams(s, l, i+1, current)
    t = GetAlphagrams(s, l, i+1, current+s[i])
    return nt + t

def GetAlphagramsWith(s, l, i, j, includes, current):
    if len(current) == l and j == len(includes):
        return [current]
    elif len(current) == l:
        return []
    if i >= len(s):
        return []
    #Don't take current letter
    nt = GetAlphagramsWith(s, l, i+1, j, includes, current)
    if j != len(includes) and s[i] == includes[j]:
        j += 1
    t = GetAlphagramsWith(s, l, i+1, j, includes, current+s[i])
    return nt + t

def GetValidWords(alphagrams) -> list:
    res = []
    for w in alphagrams:
        w = ''.join(sorted(w))
        if w in word_list:
            res += word_list[w]
    return res


keys = GetAnagramsWith("RETINASE", 4, 'RAE')
print(keys)
print(GetValidWords(keys))

#Need to add support for blanks