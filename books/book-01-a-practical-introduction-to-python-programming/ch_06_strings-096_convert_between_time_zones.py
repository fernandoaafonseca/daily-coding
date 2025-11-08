'''
Write a program that converts a time from one time zone to another. The user enters the time in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters is that of the original time and the second is the desired time zone. The possible time zones are "Eastern", "Central", "Mountain", or "Pacific".

	Time: 11:48pm
	Starting zone: Pacific
	Ending zone: Eastern
	2:48am
'''


from datetime import datetime, timedelta


def main() -> None:
    time_str = get_user_time()
    start_zone = get_zone('starting')
    end_zone = get_zone('ending')

    # Convert the user's input string into a datetime object
    t = datetime.strptime(time_str, '%I:%M%p')

    # Hour offsets relative to the Eastern Time Zone
    # (Eastern = 0, Central = -1, Mountain = -2, Pacific = -3)
    zone_offsets = {'eastern': 0, 'central': -1, 'mountain': -2, 'pacific': -3}

    # Calculate the time difference (in hours) between the two zones
    offset = zone_offsets[end_zone] - zone_offsets[start_zone]

    # Apply the time difference using timedelta
    converted = t + timedelta(hours=offset)

    # Display the result in a formatted way
    print(f'\nTime: {t.strftime('%I:%M%p').lower()}')
    print(f'Starting zone: {start_zone.capitalize()}')
    print(f'Ending zone: {end_zone.capitalize()}')
    print(f'Converted time: {converted.strftime('%I:%M%p').lower()}')


def get_user_time() -> str:
    '''
    Ask the user to enter a time string and validate its format.
    '''
    while True:
        try:
            time_str = input('Enter a time (e.g., 3:48pm or 11:26am): ').strip().lower()
            # Test if the input string matches the expected 12-hour format (e.g., "2:15pm")
            datetime.strptime(time_str, "%I:%M%p")
            return time_str
        except ValueError:
            print('\nPlease enter a valid time in the format "h:mmam" or "h:mmpm".\n')


def get_zone(prompt_label: str) -> str:
    '''
    Ask the user for a U.S. time zone (E, C, M, or P) and return its full name.
    '''
    zones = {'e': 'eastern', 'c': 'central', 'm': 'mountain', 'p': 'pacific'}
    while True:
        zone = input(f'Enter the {prompt_label} time zone (E, C, M, or P): ').strip().lower()
        # Check that the first letter matches one of the valid zones
        if zone and zone[0] in zones:
            return zones[zone[0]]
        else:
            print('\nInvalid input. Please enter E, C, M, or P.\n')


if __name__ == "__main__":
    main()
