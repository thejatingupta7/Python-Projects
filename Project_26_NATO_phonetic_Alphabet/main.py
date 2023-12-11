import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")


# TODO 1: Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_data = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2: Create a list of the phonetic code words from a word that the user inputs.

def entry():
    name = input("Enter a word : ").upper()
    try:
        result = [dict_data[letter] for letter in name]
    except KeyError:
        print("Sorry, only input letters")
        entry()
    else:
        print(result)

entry()

