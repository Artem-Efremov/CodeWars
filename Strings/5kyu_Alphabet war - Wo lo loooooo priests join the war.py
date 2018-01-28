"""
Description:
Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters have discovered a new unit - a priest with Wo lo looooooo power.



Task
Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (but it's priest with Wo lo loooooooo power)
The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (but it's priest with Wo lo loooooooo power)
The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly letters with the same power.

mtq => wtp
wjs => mjz
A letter with adjacent letters j and t is not converted i.e.:

tmj => tmj
jzt => jzt
The priests (j and t) do not convert the other priests ( jt => jt).

Example
alphabet_war("z")         #=>  "z"  => "Right side wins!"
alphabet_war("tz")        #=>  "ts" => "Left side wins!" 
alphabet_war("jz")        #=>  "jz" => "Right side wins!" 
alphabet_war("zt")        #=>  "st" => "Left side wins!" 
alphabet_war("azt")       #=> "ast" => "Left side wins!"
alphabet_war("tzj")       #=> "tzj" => "Right side wins!"

"""




import re
def alphabet_war(fight):
    
    left = 'tsbpw'
    right = 'jzdqm'
    
    print fight
    
    fight=re.sub('js(?!t)','jz\1',fight)
    fight=re.sub('jb(?!t)','jd\1',fight)
    fight=re.sub('jp(?!t)','jq\1',fight)
    fight=re.sub('jw(?!t)','jm\1',fight)
    
    fight=re.sub('tz(?!j)','ts\1',fight)
    fight=re.sub('td(?!j)','tb\1',fight)
    fight=re.sub('tq(?!j)','tp\1',fight)
    fight=re.sub('tm(?!j)','tw\1',fight)
    
    fight=re.sub(r'([^t]+|^)s(j)',r'\1z\2',fight)
    fight=re.sub(r'([^t]+|^)b(j)',r'\1d\2',fight)
    fight=re.sub(r'([^t]+|^)p(j)',r'\1q\2',fight)
    fight=re.sub(r'([^t]+|^)w(j)',r'\1m\2',fight)
    
    fight=re.sub(r'([^j]+|^)z(t)',r'\1s\2',fight)
    fight=re.sub(r'([^j]+|^)d(t)',r'\1b\2',fight)
    fight=re.sub(r'([^j]+|^)q(t)',r'\1p\2',fight)
    fight=re.sub(r'([^j]+|^)m(t)',r'\1w\2',fight)
    
    print fight
    
    cnt=0
    for i in fight:
        if i in left:
            cnt+=left.index(i)
        elif i in right:
            cnt-=right.index(i)
    print cnt

    if cnt > 0:
        return "Left side wins!"
    elif cnt < 0:
        return "Right side wins!"
    else:
        return "Let's fight again!"




# Решение не учитывает замену atj на att и т.п. прошло тест случайно с 20 раза


import re

def alphabet_war(fight):
    left = {'w': [4, 'm'], 'p': [3, 'q'], 'b': [2, 'd'], 's': [1, 'z']}
    right = {'m': [-4, 'w'], 'q': [-3, 'p'], 'd': [-2, 'b'], 'z': [-1, 's']}

    buf1 = re.findall(r'j.t|t.j', fight)

    for i in re.findall(r'.?j.?', fight):
        s = ''
        for j in i:
            s += left[j][1] if j in left else j 
        fight = re.sub(i, s, fight)

    for i in re.findall(r'.?t.?', fight):
        s = ''
        for j in i:
            s += right[j][1] if j in right else j   
        fight = re.sub(i, s, fight)

    buf2 = re.findall(r'j.t|t.j', fight)

    # for i in range(len(buf1)):
    #     fight = re.sub(buf2[i], buf1[i], fight)

    res = 0
    for i in fight:
        if i in left:
            res += left[i][0]
        elif i in right:
            res += right[i][0]
    return buf1 #"Left side wins!" if res > 0 else "Right side wins!" if res < 0 else "Let's fight again!"







def alphabet_war(fight):
    s = 0
    SWAP = {'j':{'w':'m','p':'q','b':'d','s':'z'}, 't':{'m':'w','q':'p','d':'b','z':'s'}}
    for l, c, r in zip(' ' + fight, fight, fight[1:] + ' '):
        if l + r not in 'tjt':
            c = SWAP.get(l, {}).get(c, c)
            c = SWAP.get(r, {}).get(c, c)
        s += {'w':4, 'p':3, 'b':2, 's':1, 'm':-4, 'q':-3, 'd':-2, 'z':-1}.get(c, 0)
    return "Left side wins!" if s > 0 else "Right side wins!" if s < 0 else "Let's fight again!"







a = 'wpbs'
b = 'mqdz'
def alphabet_war(fight):
    f = list('_'+fight+'_')
    for i in range(1,len(f)):
        if f[i] in a:
            if (f[i-1] == 'j' or f[i+1] == 'j') and (f[i-1] != 't' and f[i+1] != 't'):
                f[i] = b[a.index(f[i])]
        if f[i] in b:
            if (f[i-1] == 't' or f[i+1] == 't') and (f[i-1] != 'j' and f[i+1] != 'j'):
                f[i] = a[b.index(f[i])]
    fight = ''.join(f)
    l,r = fight.count('w')*4+fight.count('p')*3+fight.count('b')*2+fight.count('s'), fight.count('m')*4+fight.count('q')*3+fight.count('d')*2+fight.count('z')    
    return "Left side wins!" if l > r else ("Right side wins!" if r > l else "Let's fight again!")






import re
def alphabet_war(f):
    p='wpbs_zdqm'
    f = re.sub(r'(?<!t)[wpbs](?=j)|(?<=j)[wpbs](?!t)|(?<!j)[zdqm](?=t)|(?<=t)[zdqm](?!j)', lambda x: p[8 - p.index(x.group(0))], f)
    r = sum(p.index(e) -4 if e in p else 0 for e in f)
    return "Let's fight again!" if r == 0 else "Left side wins!" if r < 0 else "Right side wins!"