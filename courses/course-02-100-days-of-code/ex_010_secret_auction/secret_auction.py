import os

def cls():
	# Function to clear the console/terminal depending on OS
	# 'nt' -> Windows
	# else -> Linux/MacOS
    os.system('cls' if os.name=='nt' else 'clear')

def winning_bid(biddings):
	# Checks all the bids
	# and return the highest bid and the name of the winner
	winner = ''
	highest_bid = 0
	
	for bidder in biddings:
		current_bid = int(biddings[bidder])
		if current_bid > highest_bid:
			highest_bid = current_bid
			winner = bidder
	
	print(f'\nThe winner is {winner} with a bid of ${highest_bid}.')

biddings_record = {}
continue_auction = True

while continue_auction:
	# Adds to the dictionary 'biddings_record' the names and bids
	name = input('What is your name? ')
	bid = ''
	
	while type(bid) != 'int':
		# Checks if the bid is an integer
		try:
			int(bid)
			break
		except:
			bid = input('What is your bid? $')
	
	biddings_record[name] = bid
	
	other_bidders = ''
	valid_answers = ['yes', 'no']
	
	while other_bidders not in valid_answers:
		# Checks if the answer is valid ('yes' or 'no')
		other_bidders = input('Are there any other bidders? Type "yes" or "no": ').lower()
		if other_bidders == 'yes':
			# Clears the screen
			other_bidders = ''
			cls()
			break
		elif other_bidders == 'no':
			# If there's no other bidders,
			# stops the loop
			# and calls the funcion 'winning_bid'
			# passing the dictionary 'biddings_record'
			continue_auction = False
			winning_bid(biddings_record)
			break