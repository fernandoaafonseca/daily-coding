'''
Bank loan system

-> Request:
	- age
	- monthly income
	- loan amount

-> The loan is only approved if:
	- aged between 21 and 60 years,
	- monthly income >= 3000,
	- loan amount does not exceed 10x income.

Tip: combine "and" and relational operators into a single "if".
'''


def main() -> None:
	client_age = get_client_age()
	client_monthly_income = get_client_monthly_income()
	client_loan_amount = get_client_loan_amoun()
	is_loan_approved = check_for_approval(client_age, client_monthly_income, client_loan_amount)

	display_result(is_loan_approved)


def get_client_age() -> int:
	while True:
		try:
			age = int(input('Enter your age: '))
			if 0 < age <= 120:
				return age
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid age (between 1 and 120).\n')


def get_client_monthly_income() -> float:
	while True:
		try:
			monthly_income  = float(input('Enter your monthly income: $ '))
			if monthly_income >= 0:
				return monthly_income
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid amount.\n')


def get_client_loan_amoun() -> float:
	while True:
		try:
			loan_amount  = float(input('Enter how much you want to borrow: $ '))
			if loan_amount > 0:
				return loan_amount
			else:
				raise ValueError
		except ValueError:
			print('\nPlease enter a valid amount bigger than $ 0.00.\n')


def check_for_approval(client_age: int, client_monthly_income: float, client_loan_amount: float) -> bool:
	is_age_approved = check_age(client_age)
	is_monthly_income_approved = check_monthly_income(client_monthly_income)
	is_loan_amount_approved = check_loan_amount(client_monthly_income, client_loan_amount)

	return is_age_approved and is_monthly_income_approved and is_loan_amount_approved


def check_age(client_age: int) -> bool:
	return 21 <= client_age <= 60


def check_monthly_income(client_monthly_income: float) -> bool:
	return client_monthly_income >= 3000


def check_loan_amount(client_monthly_income: float, client_loan_amount: float) -> bool:
	return client_loan_amount <= 10 * client_monthly_income


def display_result(is_loan_approved) -> None:
	result = '👍 approved' if is_loan_approved else '👎 declined'

	print(f'\nYour loan application has been {result}.')


if __name__ == '__main__':
	main()