'''
When I was a kid, we used to play this game called Mad Libs. The way it worked was a friend would ask me for some words and then insert those words into a story at specific places and read the story. The story would often turn out to be pretty funny with the words I had given since I had no idea what the story was about. The words were usually from a specific category, like a place, an animal, etc.
For this problem you will write a Mad Libs program. First, you should make up a story and leave out some words of the story. Your program should ask the user to enter some words and tell them what types of words to enter. Then print the full story along with the inserted words. Here is a small example, but you should use your own (longer) example:

	Enter a college class: CALCULUS
	Enter an adjective: HAPPY
	Enter an activity: PLAY BASKETBALL

	CALCULUS class was really HAPPY today. We learned how to PLAY BASKETBALL today in class. I can't wait for tomorrow's class!
'''


def main() -> None:
	word_types = ['College class', 'Adjective', 'Activity']
	user_strings = []
	for type in word_types:
		new_word = get_user_string(type)
		user_strings.append(new_word)

	display_result(user_strings)


def get_user_string(word_type: str) -> str:
	while True:
		try:
			user_string = str(input(f'{word_type}: '))
			return user_string
		except ValueError:
			print('\nPlease enter a valid string.\n')


def display_result(user_strings: list[str, str, str]) -> None:
	college_class = user_strings[0]
	adjective = user_strings[1]
	activity = user_strings[2]

	print()
	print(f'{college_class} class was really {adjective} today. We learned how to {activity} today in class. I can\'t wait for tomorrow\'s class!')


if __name__ == '__main__':
	main()