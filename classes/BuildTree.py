import pickle
from string import ascii_uppercase

def BuildTree(lexicon) -> dict:
    tree = {"WORD": ""}
    curr_dict = tree
    for word in lexicon:
        for letter in word:
            if letter in curr_dict:
                curr_dict = curr_dict[letter]
            else:
                curr_dict[letter] = {"WORD": curr_dict["WORD"] + letter}
                curr_dict = curr_dict[letter]
        curr_dict["END"] = True
        curr_dict = tree
    return tree

if __name__ == "__main__":
    big_list = open("../dictionary.txt", "r").readlines()
    big_list = [word.strip("\n") for word in big_list]
    t = BuildTree(big_list)
    with open('Tree.pickle', 'wb') as handle:
        pickle.dump(t, handle, protocol=pickle.HIGHEST_PROTOCOL)