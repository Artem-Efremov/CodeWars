"""
If you have completed the Tribonacci sequence kata, you would know by now that mister Fibonacci has at least a bigger brother. If not, give it a quick look to get how things work.

Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 4 elements and each following element is the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian, but it would also sound really awful) with a signature of 5 elements and each following element is the sum of the 5 previous, and so on.

Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - and remember each next element is the sum of the last X elements - and returns the first n elements of the so seeded sequence.

xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}
xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}
xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}
xbonacci {1,1} produces the Fibonacci sequence

"""




def Xbonacci(signature,n):
    result = signature[:n]
    len_object = len(signature)
    while len(result) < n:
        result.append(sum(result[-len_object:]))
    return result[:n]








Test.describe("Basic tests")
Test.assert_equals(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
Test.assert_equals(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])
Test.assert_equals(Xbonacci([0,0,0,0,1],10),[0,0,0,0,1,1,2,4,8,16])
Test.assert_equals(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
Test.assert_equals(Xbonacci([1,0,0,0,0,0,0,0,0,0],20),[1,0,0,0,0,0,0,0,0,0,1,1,2,4,8,16,32,64,128,256])
Test.assert_equals(Xbonacci([0.5,0,0,0,0,0,0,0,0,0],10),[0.5,0,0,0,0,0,0,0,0,0])
Test.assert_equals(Xbonacci([0.5,0,0,0,0,0,0,0,0,0],20),[0.5,0,0,0,0,0,0,0,0,0,0.5,0.5,1,2,4,8,16,32,64,128])
Test.assert_equals(Xbonacci([0,0,0,0,0,0,0,0,0,0],20),[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(Xbonacci([1,2,3,4,5,6,7,8,9,0],9),[1,2,3,4,5,6,7,8,9])
Test.assert_equals(Xbonacci([1,2,3,4,5,6,7,8,9,0],0),[])

Test.describe("Random tests")
from random import randint
def Xsol(s,n):
    l=len(s)
    while len(s)<n:
        s+=[sum(s[-l:])]
    return s[:n]

for _ in range(40):
    sign=[randint(0,20) for x in range(randint(1,20))]
    n=randint(1,50)
    Test.it("Testing for signature: "+str(sign)+" and n: "+str(n))
    Test.assert_equals(Xbonacci(sign[:],n),Xsol(sign,n),"It should work for random inputs too")