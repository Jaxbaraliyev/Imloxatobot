from krillsozlar import words
from difflib import get_close_matches

def checkWords(word, words=words):
    matches = set(get_close_matches(word,  words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'х' in word:
        word = word.replace('х', 'x')
        matches.update(get_close_matches(word, words))
    elif 'x' in word:
        word = word.replace('x', 'х')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}