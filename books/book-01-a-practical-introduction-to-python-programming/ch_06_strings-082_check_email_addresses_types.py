'''
At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the user how many email addresses they will be entering, and then has the user enter those addresses. After all the email addresses are entered, the program should print out a message indicating either that all the addresses are student addresses or that there were some professor addresses entered.
'''


def main() -> None:
	num_addresses = get_quantity_email_addresses()
	list_email_addresses = get_list_of_email_addresses(num_addresses)
	types_of_email_addresses = get_list_of_email_addresses_types(list_email_addresses)
	all_student = check_all_types_are_student(types_of_email_addresses)
	display_result(all_student)


def get_quantity_email_addresses() -> int:
	while True:
		try:
			quantity = int(input('Enter how many email addresses you want to add: '))
			# Not checking is email is valid here
			return quantity
		except ValueError:
			print('\nPlease enter a valid number.\n')


def get_list_of_email_addresses(num_addresses: int) -> list[str]:
	list_email_addresses = []
	for _ in range(num_addresses):
		new_email_address = get_new_email_address()
		list_email_addresses.append(new_email_address)

	return list_email_addresses


def get_new_email_address() -> str:
	while True:
		try:
			email_address = str(input('Enter the email address: '))
			# Not checking is email is valid here
			return email_address
		except ValueError:
			print('\nPlease enter a valid email.\n')


def get_list_of_email_addresses_types(list_email_addresses: list[str]) -> list[str]:
	types_of_email_addresses = []

	for address in list_email_addresses:
		new_email_address_type = check_email_address_type(address)
		types_of_email_addresses.append(new_email_address_type)

	return types_of_email_addresses


def check_email_address_type(email_address: str) -> str:
	if email_address.endswith('@student.college.edu'):
		return 'student'
	elif email_address.endswith('@prof.college.edu'):
		return 'professor'
	else:
		return 'unknown'


def check_all_types_are_student(types_of_email_addresses: list[str]) -> bool:
	'''
	Set always returns a list without duplicates.
	'''
	types_removing_duplicates = set(types_of_email_addresses)
	all_the_same = len(types_removing_duplicates) == 1

	if all_the_same:
		# If there's just one value, checks if it's "student" or "professor"
		return "student" in types_removing_duplicates


def display_result(all_student: bool) -> None:
	print()
	if all_student:
		print('All the addresses are student addresses.')
	else:
		print('Not all the addresses are student addresses.')


if __name__ == '__main__':
	main()