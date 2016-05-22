# Fibonacci numbers

from utils import next_fibonacci_set

def is_nine_pandigital(n):
    # Precondition: n is length 9
    s = set(d for d in str(n))
    try:
        s.remove("0")
    except KeyError:
        pass
    return len(s) is 9


if __name__ == "__main__":



    exit()
    # This is technically correct, but not nearly fast enough.
    counter = 3 # corresponds to Fi of c
    a = 1
    b = 1
    c = 2
    while True:
        c_string = str(c)
        print(counter)
        if is_nine_pandigital(c_string[:9]) and is_nine_pandigital(c_string[len(c_string)-9:]):
            print(c,counter)
            exit()

        (a,b,c,counter) = next_fibonacci_set(a,b,c,counter)
