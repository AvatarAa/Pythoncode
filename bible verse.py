import requests

# Function to get the text of a Bible verse
def get_verse(book, chapter, verse_range):
    url = f'https://bible-api.com/{book} {chapter}:{verse_range}'
    response = requests.get(url)
    parsed_data = response.json()
    return parsed_data['text']

# Function to get the reference of a Bible verse
def get_verse_reference(book, chapter, verse_range):
    url = f'https://bible-api.com/{book} {chapter}:{verse_range}'
    response = requests.get(url)
    parsed_data = response.json()
    return parsed_data['reference']

# Get user input
book = input("What book of the Bible will you like? \n(Romans or John): ").strip().lower()
if book not in ['romans', 'john']:
    print("Invalid book. Please enter either 'Romans' or 'John'.")
    exit()

chapter = int(input("What chapter will you like?\n (1 or 2): "))
if chapter not in [1, 2]:
    print("Invalid chapter. Please enter either 1 or 2.")
    exit()

verse_range = input("What verse range will you like? \n(1-2), (5-7), (9), or (13:1-9&10): ")

# Determine which function to call based on user input
if verse_range == '13:1-9&10':
    verse = get_verse(book, chapter, verse_range)
else:
    verse_reference = get_verse_reference(book, chapter, verse_range)
    verse = f"{verse_reference}:\n{get_verse(book, chapter, verse_range)}"

print(verse)
