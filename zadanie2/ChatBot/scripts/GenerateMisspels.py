import string
import random

nearbykeys = {
    'a': ['q','w','s','x','z'],
    'b': ['v','g','h','n'],
    'c': ['x','d','f','v'],
    'd': ['s','e','r','f','c','x'],
    'e': ['w','s','d','r'],
    'f': ['d','r','t','g','v','c'],
    'g': ['f','t','y','h','b','v'],
    'h': ['g','y','u','j','n','b'],
    'i': ['u','j','k','o'],
    'j': ['h','u','i','k','n','m'],
    'k': ['j','i','o','l','m'],
    'l': ['k','o','p'],
    'm': ['n','j','k','l'],
    'n': ['b','h','j','m'],
    'o': ['i','k','l','p'],
    'p': ['o','l'],
    'q': ['w','a','s'],
    'r': ['e','d','f','t'],
    's': ['w','e','d','x','z','a'],
    't': ['r','f','g','y'],
    'u': ['y','h','j','i'],
    'v': ['c','f','g','v','b'],
    'w': ['q','a','s','e'],
    'x': ['z','s','d','c'],
    'y': ['t','g','h','u'],
    'z': ['a','s','x'],
    '-': [' ', '+', "_", ' ', ' ', ' '],
    ' ': ['c','v','b','n','m']
}

def word_misspell(word: str):

    ix = random.choice(range(len(word)))
    typos = nearbykeys[word[ix].lower()]
    new_word = ''.join([word[w] if w != ix else random.choice(typos) for w in range(len(word))])

    # add some chance to drop some of
    return new_word

def word_drop(word: str):
    ix = random.choice(range(len(word)))
    new_word = ''.join([word[w] if w != ix else '' for w in range(len(word))])

    return new_word

YAML_PATH = r"../data/misspells.yml"

def generate_misspells_yaml(words: list):
    file = open(YAML_PATH, "w")
    file.write("version: \"3.1\"\nnlu:\n")

    for word in words:
        file.write("  - synonym: "+ word + "  \n    examples: |\n")
        for i in range(10):
            file.write("      - " + str(word_drop(word)) + "\n")

        for i in range(15):
            file.write("      - " + str(word_misspell(word)) + "\n")


word_to_misspell = ["Lasagne", "Pizza", "Hot-dog", "Burger", "Spaghetti Carbonara", "Tiramisu"]
generate_misspells_yaml(word_to_misspell)