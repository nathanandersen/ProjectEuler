# Problem 22
from utils import letter_value
from utils import word_value
from utils import clean_list_file

names = clean_list_file("p022_names.txt")
names.sort()

def name_value(n):
    return(word_value(n)*(names.index(n)+1))

print (sum(name_value(n) for n in names))
