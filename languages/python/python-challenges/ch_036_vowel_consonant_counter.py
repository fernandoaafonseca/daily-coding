'''
Create a Python program that prompts the user for a phrase or word.
The program should then count and display the total number of vowels and consonants present in the input, disregarding spaces, numbers, and special characters.

Requirements:

1. The counting must be case-insensitive (i.e., 'A' and 'a' should be treated as the same vowel).
2. Disregard any characters that are not letters (numbers, punctuation, spaces, etc.).
3. Display the total number of vowels and the total number of consonants separately.

Example Execution:

Enter a phrase or word: Hello World! 123
Number of vowels: 3
Number of consonants: 7
'''


from string import ascii_lowercase as ALPHABET


VOWELS = 'aeiou'
CONSONANTS = ''.join(letter for letter in ALPHABET if letter not in VOWELS)


def main() -> None:
	user_text = input('Enter a phrase or word: ')
	vowels_count, consonants_count = count_consonants_and_vowels(user_text, VOWELS, CONSONANTS)

	print()
	print(f'Number of vowels: {vowels_count}')
	print(f'Number of consonants: {consonants_count}')


def count_consonants_and_vowels(user_text: str, VOWELS: str, CONSONANTS: str) -> tuple[int, int]:
	vowels_count = 0
	consonants_count = 0

	for char in user_text:
		if char.lower() in VOWELS:
			vowels_count += 1
		elif char.lower() in CONSONANTS:
			consonants_count +=1
		else:
			pass

	return vowels_count, consonants_count


if __name__ == '__main__':
	main()