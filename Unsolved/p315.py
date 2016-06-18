# Problem 315
from utils import sieve
# These are the lettered clock segments
#. a .
#b . c
#. d .
#e . f
#. g .

zero = {"a","c","f","g","b","e"}
one = {"c","f"}
two = {"a","c","d","e","g"}
three = {"a","c","d","f","g"}
four = {"b", "d", "c", "f"}
five = {"a","b","d","f","g"}
six = {"a","b","d","e","f","g"}
seven = {"b","a","c","f"}
eight = {"a","b","c","d","e","f","g"}
nine = {"a","b","c","d","f","g"}

digitPatterns = {0:zero,1:one,2:two,3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}

def digitalRootStep(n):
    return sum(int(digit) for digit in str(n))


clockDifCtDict = {}
def clockDifferenceCt(n):
    if n in digitPatterns:
        return 0
    elif n not in clockDifCtDict:
        cost = sum(len(digitPatterns[int(digit)]) for digit in str(n))
        

samClockCountDict = {}
def samClockCount(n):
    if n in digitPatterns:
        return 2*len(digitPatterns[n])
    elif n not in samClockCountDict:
        cost = sum(len(digitPatterns[int(digit)]) for digit in str(n))
        samClockCountDict[n] = cost*2 + samClockCount(digitalRootStep(n))
    return samClockCountDict[n]



#maxClockCountDict = {}
#def maxClockCount(n):

#for n in range(a,b):

if __name__ == "__main__":
    a = 10**7
    b = 2 * a
    _primes = sieve(b)
    for index in range(len(_primes)):
        if _primes[index] > a:
            _primes = _primes[index:]
            break

    print(_primes)

    for p in _primes:
        print(p,samClockCount(p))
