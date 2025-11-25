'''
Survey Data

Imagine you're cleaning up user input data for a survey application. The data contains a list of answers, but some entries are empty due to users skipping questions. You need to remove these empty strings to prepare the data for analysis.

Task
Given a list of strings representing user answers, write a program that uses the filter() function and a lambda expression to create a new list that excludes any empty strings. Then display the new cleaned list of answers
'''


user_answers = ['Yes', '', 'No', '', 'Maybe', '', 'Yes']

# Create a new list without empty answers using filter with a lambda expression
filtered_user_answers = list(filter(lambda name: len(name) > 0, user_answers))

# Display the cleaned list of answers
print(filtered_user_answers)