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





print(alphabet_war("ssjdabjztzwjtwjatqbbbsjjabjjpzdqjttdsap"))
