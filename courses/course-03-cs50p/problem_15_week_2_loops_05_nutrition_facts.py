'''
Nutrition Facts

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

Source:
https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version

Hints
Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a dict to associate a fruit with its calories!
If k is a str and d is a dict, you can check whether k is a key in d with code like:
if k in d:
    ...
Take care to output the fruit’s calories, not calories from fat!
'''


# List with the names of fruits
fruits_names: list[str] = [
    'Apple', 'Avocado', 'Banana', 'Cantaloupe', 'Grapefruit', 'Grapes',
    'Honeydew Melon', 'Kiwifruit', 'Lemon', 'Lime', 'Nectarine', 'Orange',
    'Peach', 'Pear', 'Pineapple', 'Plums', 'Strawberries', 'Sweet Cherries',
    'Tangerine', 'Watermelon'
]

# List with the calories of each fruit
fruits_calories: list[int] = [
    130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 60, 80, 60, 100, 50, 70, 50, 100, 50, 80
]


def main():
    dict_fruits_calories = create_dict_fruits_calories(
        fruits_names, fruits_calories)
    user_input_fruit = get_user_input_fruit()
    calories = get_calories_value(user_input_fruit, dict_fruits_calories)
    result = generate_result(user_input_fruit, calories)
    print(result)


def create_dict_fruits_calories(fruits_names: list[str], fruits_calories: list[int]) -> dict[str, int]:
    '''
    Create a dictionary where the keys are the names of the fruits and the values ​​are their respective calories
    '''
    dict_fruits_calories = dict(zip(fruits_names, fruits_calories))
    return dict_fruits_calories


def get_user_input_fruit() -> str:
    return input('Plese enter the name of a fruit: ')


def get_calories_value(user_input_fruit: str, dict_fruits_calories: dict[str, int]) -> int | None:
    '''
    If the fruit exists in the dict, it returns its calories.
    '''
    # Case insensitive dictionary search
    for key in dict_fruits_calories:
        if key.lower() == user_input_fruit.lower():
            return dict_fruits_calories[key]
    return None


def generate_result(user_input_fruit: str, calories: int | None) -> str:
    '''
    Genenrates the final text for ptinting the name of the fruit and its calories.
    Returns an empty string if the dict doesn't contain the fruit.
    '''
    if calories != None:
        item_line = f'Item: {user_input_fruit.title()}'
        calories_line = f'Calories: {calories}'
        final_text: list[str] = [item_line, calories_line]
        return '\n'.join(final_text)
    else:
        return ''


if __name__ == '__main__':
    main()


# Test:
dict_fruits_calories = create_fuits_calories_dict(
    fruits_names, fruits_calories)
print(get_calories_value('apple', dict_fruits_calories) == 130)

print(get_calories_value('Avocado', dict_fruits_calories) == 50)

print(get_calories_value('chocolate', dict_fruits_calories) == None)

print(get_calories_value('Kiwifruit', dict_fruits_calories) == 90)

print(get_calories_value('pear', dict_fruits_calories) == 100)

print(get_calories_value('Strawberry', dict_fruits_calories) == None)

print(get_calories_value('strawberries', dict_fruits_calories) == 50)

print(get_calories_value('Sweet Cherries', dict_fruits_calories) == 100)

print(get_calories_value('Tomato', dict_fruits_calories) == None)
