
translation_dict = {
    "Definitely": "जरूर",
    "share your": "share करो apna",
    "feedback": "feedback",
    "in the comment section": "comment section में",
    "So": "अगर",
    "even if it's a": "even if it's a",
    "big": "बड़ा",
    "video": "video",
    "I will clearly mention all the": "मैं सब",
    "products": "products को mention करूँगा",
    "I was waiting for my": "मैं मेरा",
    "bag": "bag का wait कर रहाथा",
}

# Function to translate English text to Hinglish
def translate_to_hinglish(text):
    for key, value in translation_dict.items():
        text = text.replace(key, value)
    return text

# Test the translations
statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag."
]

for statement in statements:
    hinglish_translation = translate_to_hinglish(statement)
    print(hinglish_translation)
