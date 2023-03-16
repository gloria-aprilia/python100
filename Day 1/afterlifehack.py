# import json library
import json


## Choose Language
# load available languages
with open('lang/languages.json') as file:
    available_languages = json.load(file)

# List all languages
print("Available languages:")
for i in range(1, len(available_languages)+1):
    print(f"{i}. {available_languages[str(i)].capitalize()}")

# Choose language
chosen_language_no = str(input("Choose your language: (type '1' for Indonesian)\n"))
while str(chosen_language_no) not in list(available_languages.keys()):
    print("Error input. Please try again.")
    chosen_language_no = str(input("Choose your language: (type '1' for Indonesian)\n"))

# Storing chosen language
chosen_language = available_languages[chosen_language_no]


## Welcoming message
with open('lang/words.json') as file:
    words = json.load(file)
print(f"\n{words['welcome'][chosen_language].upper()}")


## Enter birth month as subject
# Load birth month
path = f'lang/{chosen_language}/subject.json'
with open(path) as file:
    subject = json.load(file)

# Enter birth month prompt
month = str(input(f"\n{words['month'][chosen_language]}")).lower()
while month not in list(subject.keys()):
    print(words['error_input'][chosen_language])
    month = str(input(f"{words['month'][chosen_language]}:")).lower()


## Last number of birst date
# Load alphabet
path = f'lang/{chosen_language}/verb.json'
with open(path) as file:
    verb = json.load(file)

# Enter first letter
number = str(input(f"\n{words['number'][chosen_language]}"))
while number not in list(verb.keys()) or len(number)>1:
    print(words['error_input'][chosen_language])
    first_letter= str(input(f"{words['number'][chosen_language]}"))


## First letter of first name
# Load alphabet
path = f'lang/{chosen_language}/object.json'
with open(path) as file:
    object = json.load(file)

# Enter first letter
first_letter= str(input(f"\n{words['letter'][chosen_language]}"))
while first_letter not in list(object.keys()) or len(first_letter)>1:
    print(words['error_input'][chosen_language])
    first_letter= str(input(f"{words['letter'][chosen_language]}"))


## Display result
result = (subject[month], verb[number], object[first_letter])
print(f"\n{words['result'][chosen_language]} {' '.join(result).upper()}")

## Closing
input(f"\n{words['closing'][chosen_language]}")