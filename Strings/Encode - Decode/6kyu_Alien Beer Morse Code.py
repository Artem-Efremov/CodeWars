"""
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----

"""


import re

def morse_converter(string):
    
    conversion_table = { '.----': '1', '-....': '6',
                         '..---': '2', '--...': '7',
                         '...--': '3', '---..': '8',
                         '....-': '4', '----.': '9',
                         '.....': '5', '-----': '0' }
                         
    morse_num = re.findall(r'[.-][.-][.-][.-][.-]', string) 
    answer = ''
    for i in morse_num:
        answer += conversion_table[i]

    answer = int(answer)
    return answer





