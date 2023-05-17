from spellchecker import SpellChecker
corrector = SpellChecker()


word = input('Write a word:\n')
if word in corrector:
    print('The word was spelled correctly.')
else:
    correct_word = corrector.correction(word)
    print(f'The correct spelling is: {correct_word}.')