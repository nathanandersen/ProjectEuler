#Problem 42
from utils import is_triangular_num
from utils import word_value
from utils import clean_list_file

words = clean_list_file("p042_words.txt")

print(len([word for word in words if is_triangular_num(word_value(word))]))
