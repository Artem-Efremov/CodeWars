"""
Given a number, return a string with dash'-'marks 
before and after each odd integer, 
but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

"""


def dashatize(num):
    if num is not None:
        res, pat = [], '-'
        b = ''.join([(pat + i + pat if int(i) % 2 else i) for i in str(abs(num))]).strip('-')
        for i in range(len(b)):
            if not b[i].isdigit() and b[i+1] == pat:
                continue
            else:
                res.append(b[i])
        return ''.join(res)
    return 'None'



def dashatize(num, pat='-'):
    return 'None' if num is None else ''.join([(pat + i + pat if int(i) % 2 else i) for i in str(abs(num))]).strip(pat).replace(pat+pat, pat)



import re
def dashatize(num):
    return '-'.join( re.findall(r'[13579]|[02468]+', str(num)) ) if num is not None else 'None'



print(dashatize(274), "Should return 2-7-4")
print(dashatize(5311), "Should return 5-3-1-1")
print(dashatize(86320), "Should return 86-3-20")
print(dashatize(974302), "Should return 9-7-4-3-02")
print(dashatize(None), "Should return 'None' ")
print(dashatize(0), "Should return 0")
print(dashatize(-1), "Should return 1")
print(dashatize(-28369), "Should return 28-3-6-9")



