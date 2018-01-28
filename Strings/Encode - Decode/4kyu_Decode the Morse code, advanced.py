"""
Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).

When transmitting the Morse code, the international standard specifies that:

    "Dot" – is 1 time unit long.
    "Dash" – is 3 time units long.
    Pause between dots and dashes in a character – is 1 time unit long.
    Pause between characters inside a word – is 3 time units long.
    Pause between words – is 7 time units long.

However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.

For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.

For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:

1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".

That said, your task is to implement two functions:

    Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.

    Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.

The Morse code table is preloaded for you as MORSE_CODE dictionary (MorseCode class for Java), feel free to use it.

All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!



"""


# https://www.codewars.com/kata/decode-the-morse-code-advanced/train/python




MORSE_CODE = { '.-...': '&',  '--..--': ',',  '....-': '4',  '.....': '5',  '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3'}




import re

def decodeBits(bits):
    
    # 1. Cleaning
    bits = bits.strip('0')                                                  # remove the leading and trailing extra 0's
    
    # 2. Parsing
    units = re.findall(r'1+|0+', bits)                                      # set apart all units (at first 'bit + pause', then 'bit + pause + bit', then 'bit')
    
    # 3. Identify
    length = []                                                             # mapping units to unit`s length      { length = list(map(len, units))  }
    for i in units:
        length.append(len(i))
        
    units_time = min(length)                                                # time unit (how many bits are assign for a dot)
    
    dash = '1' * 3 * units_time
    dot = '1' * units_time
    word_spase = '0' * 7 * units_time
    char_pause = '0' * 3 * units_time
    bit_pause = '0' * units_time
    
    conversion_table = { dash: '-',                                         # converting table (bits => dots or dashes)
                         dot: '.',
                         word_spase: '   ',
                         char_pause: ' ',
                         bit_pause: '' }
    
    # 4. Converting
    morse_code = []
    for i in units:
        morse_code.append(conversion_table[i])
    
    # 5. Representation
    morse_code = ''.join(morse_code)
    
    return morse_code
        
    
    


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







# TESTS



def testAndPrint(got, expected):
    if got == expected:
        print('Test {} passed'.format(expected))
    else:
        print "Got {0}, expected {1}".format(got, expected)
        

# Example from description
testAndPrint(decodeMorse(decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')), 'HEY JUDE')

# Basic bits decoding
testAndPrint(decodeMorse(decodeBits('1')), 'E')
testAndPrint(decodeMorse(decodeBits('101')), 'I')
testAndPrint(decodeMorse(decodeBits('10001')), 'EE')
testAndPrint(decodeMorse(decodeBits('10111')), 'A')
testAndPrint(decodeMorse(decodeBits('1110111')), 'M')

# Multiple bits per dot handling
testAndPrint(decodeMorse(decodeBits('111')), 'E')
testAndPrint(decodeMorse(decodeBits('1111111')), 'E')
testAndPrint(decodeMorse(decodeBits('110011')), 'I')
testAndPrint(decodeMorse(decodeBits('111000111')), 'I')
testAndPrint(decodeMorse(decodeBits('111110000011111')), 'I')
testAndPrint(decodeMorse(decodeBits('111000000000111')), 'EE')
testAndPrint(decodeMorse(decodeBits('11111100111111')), 'M')
testAndPrint(decodeMorse(decodeBits('111000111000111')), 'S')
testAndPrint(decodeMorse(decodeBits('111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111')), 'HEY JUDE')

# Extra zeros handling
testAndPrint(decodeMorse(decodeBits('01110')), 'E')
testAndPrint(decodeMorse(decodeBits('000000011100000')), 'E')

# Long messages handling
testAndPrint(decodeMorse(decodeBits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110')), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
testAndPrint(decodeMorse(decodeBits('11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111')), 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
