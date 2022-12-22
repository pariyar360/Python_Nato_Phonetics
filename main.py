
import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dataframe = pandas.DataFrame(nato)

nato_dict = {row.letter: row.code for (index, row) in nato_dataframe.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetics():
    user_input = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry! Alphabetical values only.")
        generate_phonetics()
    else:
        print(result)


generate_phonetics()
