"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldWay !

"""


def pig_it(text):
    punct = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return ' '.join([i[1:] + i[0] + 'ay' if i not in punct else i for i in text.split()])



def pig_it(text):
    return ' '.join( [i[1:] + i[0] + 'ay' if i.isalpha() else i for i in lst = text.split()])



def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())


import re
def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)



import re
def pig_it(text):
    return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)


"""['Acta est fabula', 'ctaAay steay abulafay'],
['Barba non facit philosophum', 'arbaBay onnay acitfay hilosophumpay'],
['Cucullus non facit monachum', 'ucullusCay onnay acitfay onachummay'],
['Dura lex sed lex', 'uraDay exlay edsay exlay'],
['Errare humanum est', 'rrareEay umanumhay steay'],
['Fluctuat nec mergitur', 'luctuatFay ecnay ergiturmay'],
['Gutta cavat lapidem', 'uttaGay avatcay apidemlay'],
['Hic et nunc', 'icHay teay uncnay'],
['In vino veritas', 'nIay inovay eritasvay'],
['Lux in tenebris lucet', 'uxLay niay enebristay ucetlay'],
['Morituri nolumus mori', 'orituriMay olumusnay orimay'],
['Nunc est bibendum', 'uncNay steay ibendumbay'],
['O tempora o mores !', 'Oay emporatay oay oresmay !'],
['Panem et circenses', 'anemPay teay ircensescay'],
['Quis custodiet ipsos custodes ?', 'uisQay ustodietcay psosiay ustodescay ?'],
['Requiescat in pace', 'equiescatRay niay acepay'],
['Sic transit gloria mundi', 'icSay ransittay loriagay undimay'],
['Timeo Danaos et dona ferentes', 'imeoTay anaosDay teay onaday erentesfay'],
['Ultima necat', 'ltimaUay ecatnay'],
['Veni vidi vici', 'eniVay idivay icivay']"""