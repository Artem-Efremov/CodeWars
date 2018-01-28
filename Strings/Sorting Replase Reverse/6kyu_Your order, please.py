"""
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est"


"""


def order(sentence):
    if sentence:
        seq1 = sentence.split()
        seq2 = []
        for i in range(1,10):
            for j in seq1:
                if str(i) in j:
                    seq2.append(j)
        sentence = ' '.join(seq2)
    return sentence







def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))







def extract_number(word):
    for l in word: 
        if l.isdigit(): 
            return int(l)

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))









Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
Test.assert_equals(order("d4o dru7nken sh2all w5ith s8ailor wha1t 3we a6"), "wha1t sh2all 3we d4o w5ith a6 dru7nken s8ailor")
Test.assert_equals(order(""), "")
Test.assert_equals(order("3 6 4 2 8 7 5 1 9"), "1 2 3 4 5 6 7 8 9")
