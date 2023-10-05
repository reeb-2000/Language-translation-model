# Define a dictionary to map English words/phrases to Hinglish
translation_dict = {
    "Definitely": "जरूर",
    "share your feedback": "अपना feedback share करो",
    "in the comment section": "comment section में",
    "So": "even if it's a",
    "a big": "बड़ा",
    "video": "video,",
    "I will clearly mention all the": "मैं सब products को mention करूँगा",
    "I was": "मैं मेरा",
    "waiting for": "bag का wait कर रहाथा",
    "my": "मेरा",
    "bag": "bag"

}

# Function to translate English text to Hinglish
def translate_to_hinglish(text):
    for key, value in translation_dict.items():
        text = text.replace(key, value)
    return text

# Get user input for an English statement
english_statement = input("Enter an English statement: ")

# Translate the input statement to Hinglish
hinglish_translation = translate_to_hinglish(english_statement)

# Print the Hinglish translation
print("Hinglish Translation:")
print(hinglish_translation)
