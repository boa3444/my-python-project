import pandas as pd

df = pd.read_csv(r"C:\Users\newon\Downloads\NATO-alphabet-start\nato_phonetic_alphabet.csv")

# Create a dictionary from the dataframe
nato_dict = {row['letter']: row['code'] for index, row in df.iterrows()}

# Get user input
user_input = input("Enter a word: ").upper()

# Generate the NATO phonetic code list
nato_list = []

try:
    for letter in user_input:
        if letter not in nato_dict:
            raise ValueError(f"Invalid character: {letter}")
        nato_list.append(nato_dict[letter])
except ValueError:
    print("Please input a word with alphabets only.")
else:
    final_outcome = ', '.join(nato_list)
    print(f"Your NATO phonetic is: {final_outcome}")