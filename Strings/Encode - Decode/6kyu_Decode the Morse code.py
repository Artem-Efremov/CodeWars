"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superceded by voice and digital data communication channels, it still has its use in some applications around the world.

The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decodeMorse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"

The Morse code table is preloaded for you as a dictionary, feel free to use it. In CoffeeScript, C++, Go, JavaScript, PHP, Python, Ruby and TypeScript, the table can be accessed like this: MORSE_CODE['.--'], in Java it is MorseCode.get('.--'), in C# it is MorseCode.Get('.--'), in Haskell the codes are in a Map String String and can be accessed like this: morseCodes ! ".--", in Elixir it is morse_codes variable.

All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.


"""

MORSE_CODE = { '.-...': '&',  '--..--': ',',  '....-': '4',  '.....': '5',  '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}


def decodeMorse(morse_code):
    
    # 1. Converting
    text = []
    for i in morse_code.split('   '):                                       # set apart all encrypted words from encrypted text
        word = []
        for j in i.split(' '):                                              # set apart all encrypted letters from each encrypted word
            word.append(MORSE_CODE[j])                                      # create word
        text.append(''.join(word))                                     
    
    # 2. Representation
    text = ' '.join(text)                                          
    
    return text







def testAndPrint(got, expected):
    if got == expected:
        print('Test {} passed'.format(expected))
    else:
        print "Got {0}, expected {1}".format(got, expected)
        
        
        

# Example from description
testAndPrint(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

# Basic Morse decoding
testAndPrint(decodeMorse('.-'), 'A')
testAndPrint(decodeMorse('.'), 'E')
testAndPrint(decodeMorse('..'), 'I')
testAndPrint(decodeMorse('. .'), 'EE')
testAndPrint(decodeMorse('.   .'), 'E E')
testAndPrint(decodeMorse('...---...'), 'SOS')
testAndPrint(decodeMorse('... --- ...'), 'SOS')
testAndPrint(decodeMorse('...   ---   ...'), 'S O S')

# Extra zeros handling
testAndPrint(decodeMorse(' . '), 'E')
testAndPrint(decodeMorse('   .   . '), 'E E')

# Complex tests
testAndPrint(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '), 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')








