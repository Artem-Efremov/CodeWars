"""
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

To find out more about Morse Code follow this link: https://en.wikipedia.org/wiki/Morse_code

A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code.

"""



CHAR_TO_MORSE = {'0': '-----', '2': '..---', '4': '....-', '6': '-....', '8': '---..', 'B': '-...', 'D': '-..', 'F': '..-.', 'H': '....', 'J': '.---', 'L': '.-..', 'N': '-.', 'P': '.--.', 'R': '.-.', 'T': '-', 'V': '...-', 'X': '-..-', 'Z': '--..', '1': '.----', '3': '...--', '5': '.....', '7': '--...', '9': '----.', 'A': '.-', 'C': '-.-.', 'E': '.', 'G': '--.', 'I': '..', 'K': '-.-', 'M': '--', 'O': '---', 'Q': '--.-', 'S': '...', 'U': '..-', 'W': '.--', 'Y': '-.--'}


def encryption(string):
    
    string = string.upper()
    
    morse_code = []
    for i in string.split(' '):
        word = []
        for j in i:
            word.append(CHAR_TO_MORSE[j])
        word = ' '.join(word)
        morse_code.append(word)
    
    morse_code = '   '.join(morse_code)
    
    return morse_code
    
    
