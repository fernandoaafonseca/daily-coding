import string
alphabet = [letter for letter in string.ascii_lowercase]


def transform_sentence(sentence):
    sentence_words = sentence.split(' ')
    new_sentence = []
    for word in sentence_words:
        new_word = ''
        for i in range(len(word)):
            if i == 0:
                new_word += word[i]
            else:
                current_location = alphabet.index(word[i].lower())
                preceding_location = alphabet.index(word[i-1].lower())
                if current_location > preceding_location:
                    new_word += word[i].upper()
                elif current_location < preceding_location:
                    new_word += word[i].lower()
                else:
                    new_word += word[i]
        new_sentence.append(new_word)
    final_sentence = ' '.join(word for word in new_sentence)
    return final_sentence
