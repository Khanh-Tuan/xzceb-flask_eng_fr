"""
Translator
"""
import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_to_french(french_text):
    """
    This function translates English to French
    """
    return french_text

def french_to_english(english_text):
    """
    This function translates French to English
    """
    return english_text

