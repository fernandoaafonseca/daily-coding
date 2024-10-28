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


def main():
    fruits_calories = create_fuits_calories_dict()


def create_fuits_calories_dict() -> dict:
    # List with the names of fruits
    fruits_names: str = [
        'Apple', 'Avocado', 'Banana', 'Cantaloupe', 'Grapefruit', 'Grapes',
        'Honeydew Melon', 'Kiwifruit', 'Lemon', 'Lime', 'Nectarine', 'Orange',
        'Peach', 'Pear', 'Pineapple', 'Plums', 'Strawberries', 'Sweet Cherries',
        'Tangerine', 'Watermelon'
    ]

    # List with the calories of each fruit
    calories: int = [
        130, 50, 110, 50, 60, 90, 50, 90, 15, 20, 60, 80, 60, 100, 50, 70, 50, 100, 50, 80
    ]

    # Create a dictionary where the keys are the names of the fruits and the values ​​are their respective calories
    fruits_calories = dict(zip(fruits_names, calories))
    return fruits_calories


if __name__ == '__main__':
    main()


# Test:
# print(is_valid('ECTO88') == True)
