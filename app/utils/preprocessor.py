import re
import string

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Remove digits
    text = re.sub(r"\d+", "", text)
    
    # Remove extra whitespace
    text = " ".join(text.split())
    
    return text