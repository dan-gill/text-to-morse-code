# Text to Morse code converter

MORSE_CODE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    'End of work': '...-.-',
    'Starting signal': '-.-.-',
    ' ': '       ',
    # Non-Latin extensions
    'à': '.--.-',
    'ä': '.-.-',
    'å': '.--.-',
    'ą': '.-.-',
    'æ': '.-.-',
    'ć': '-.-..',
    'ĉ': '-.-..',
    'ç': '-.-..',
    'đ': '..-..',
    'ð': '..--.',
    'é': '..-..',
    'è': '.-..-',
    'ę': '..-..',
    'ĝ': '--.-.',
    'ĥ': '----',
    'ĵ': '.---.',
    'ł': '.-..-',
    'ń': '--.--',
    'ñ': '--.--',
    'ó': '---.',
    'ö': '---.',
    'ø': '---.',
    'ś': '...-...',
    'ŝ': '...-.',
    'š': '----',
    'þ': '.--..',
    'ü': '..--',
    'ǔ': '..--',
    'ź': '--..-.',
    'ż': '--..-'
}
LETTER_SPACE = '   '


def to_morse_code(char):
    try:
        print(MORSE_CODE[char], end=LETTER_SPACE)
    except KeyError:
        # If an unknown character is entered, skip it.
        pass


if __name__ == '__main__':
    text = input("Enter string to convert to morse code: ")
    print(f"{MORSE_CODE['Starting signal']}")
    for c in text:
        to_morse_code(c.lower())
    print(f"\n{MORSE_CODE['End of work']}")
