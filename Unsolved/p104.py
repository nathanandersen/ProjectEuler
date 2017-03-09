# Fibonacci numbers

from utils import next_fibonacci_set

def is_nine_pandigital(n):
    # Precondition: n is length 9
    return len(set(d for d in str(n) if d != '0')) == 9


base_mod = 10**10
if __name__ == "__main__":
    # This is technically correct, but not nearly fast enough.
    counter = 3 # corresponds to Fi of c
    a = 1
    b = 1
    c = 2
    while True:
        if not counter % 1000:
            print(counter)
        str_c = str(c)
        if is_nine_pandigital(c % base_mod) and is_nine_pandigital(str_c[:10]):
            print(c,counter)
            exit()

        (a,b,c,counter) = next_fibonacci_set(a,b,c,counter)
