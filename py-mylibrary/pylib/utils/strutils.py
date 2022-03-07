'''
String Utilities
'''
import string
import random

EMPTY = ""
WHITESPACE = " "
DEGREES = "\u00B0"
DEGREES_CELSIUS = "\u2103"
DEGREES_FAHRENHEIT = "\u2109"
PRIME = "\u2032"
DOUBLE_PRIME = "\u2033"

# FUNCIONS A NIVELL DE CLASS
def truncate(text: str, max_length: int, placeholder: str = "...") -> str:
    return text if len(text) <= max_length else f"{text[:max_length - len(placeholder)]}{placeholder}"


def randcode(length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> str:
    alphabet = f"{string.ascii_uppercase if uppercase_letters else EMPTY}{string.ascii_lowercase if lowercase_letters else EMPTY}{string.digits if digits else EMPTY}{string.punctuation if punctuation else EMPTY}"
    code = EMPTY
    for i in range(length):
        code += random.choice(alphabet)
    return code


def randcode_v2(length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> str:
    alphabet = f"{string.ascii_uppercase if uppercase_letters else EMPTY}{string.ascii_lowercase if lowercase_letters else EMPTY}{string.digits if digits else EMPTY}{string.punctuation if punctuation else EMPTY}"
    code =  EMPTY.join([random.choice(alphabet) for i in range(length)])
    return code


def randcodes(num_codes: int, length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> list[str]:
    codes = []
    for i in range(num_codes):
        code = randcode(length, uppercase_letters, lowercase_letters, digits, punctuation)
        codes.append(code)
    return codes


def randcodes_v2(num_codes: int, length: int = 8, uppercase_letters: bool = True, lowercase_letters: bool = True, digits: bool = True, punctuation: bool = False) -> list[str]:
    codes = [randcode(length, uppercase_letters, lowercase_letters, digits, punctuation) for i in range(num_codes)]
    return codes
