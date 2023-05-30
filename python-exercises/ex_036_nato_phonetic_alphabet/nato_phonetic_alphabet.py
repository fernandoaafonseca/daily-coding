import pandas as pd


ALPHABET_PATH = 'data/nato_phonetic_alphabet.csv'
df_nato_alphabet = pd.read_csv(ALPHABET_PATH)
nato_alphabet = {row['letter']:row['code'] for (index, row) in df_nato_alphabet.iterrows()}
print(nato_alphabet)

word = input('Enter a word:\n').upper()
phonetic_word = [nato_alphabet[letter] for letter in word]
print(phonetic_word)