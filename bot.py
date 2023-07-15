min_word_length = 2
max_word_length = 6

valid_words = []
with open('3letterwords.txt') as f:
    valid_words.extend(f.read().splitlines())

with open('4letterwords.txt') as f:
    valid_words.extend(f.read().splitlines())

with open('5letterwords.txt') as f:
    valid_words.extend(f.read().splitlines())

with open('6letterwords.txt') as f:
    valid_words.extend(f.read().splitlines())

# sends text of results
def generate_permutations(letters, min_length=2, max_length=6, valid_words=valid_words):
    letters = [*letters]
    perms = []
    for length in range(min_length, max_length + 1):
        backtrack(letters, length, [], perms, valid_words)

    results = []
    [results.append(x) for x in perms if x not in results]

    return results
    

def backtrack(letters, length, path, perms, valid_words):
    if len(path) == length:
        word = ''.join(path)
        if is_valid_word(word, valid_words):
            perms.append(word)
        return

    for i in range(len(letters)):
        letter = letters[i]
        remaining_letters = letters[:i] + letters[i+1:]
        path.append(letter)
        backtrack(remaining_letters, length, path, perms, valid_words)
        path.pop()

def is_valid_word(word, valid_words):
    return word in valid_words





