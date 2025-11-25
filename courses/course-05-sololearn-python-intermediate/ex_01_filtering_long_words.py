'''
Filtering Long Words

Imagine you're creating content for a vocabulary-building app. You want to challenge users by showing them only the longer words from a provided list.

Task
Given a list of words, use a list comprehension to create a new list that includes only the words that are longer than 4 letters
'''


words = ["tree", "button", "cat", "window", "defenestrate"]

# Use a list comprehension to filter out words longer than four letters
filtered_words = [w for w in words if len(w) > 4]

# Display the filtered list
print(filtered_words)