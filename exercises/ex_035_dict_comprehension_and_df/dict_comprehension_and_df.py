import pandas as pd


sentence = "What is the Aispeed Velocity of an Unladen Swallow?"
letters_count = {word:len(word) for word in sentence.split()}
column_names = ['Word', 'Letters']
df_letters_count = pd.DataFrame(list(letters_count.items()), columns=column_names)
print(df_letters_count, '\n')


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:temp_c * 9 / 5 + 32 for (day, temp_c) in weather_c.items()}
df_weather_f = pd.DataFrame(weather_f, index=[0])
for (index, row) in df_weather_f.iterrows():
    print(row)