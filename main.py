# Generate random words in Python

import random

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


words = get_list_of_words('/usr/share/dict/words')
print(words)

random_word = random.choice(words)
print(random_word)  # 👉️ sales