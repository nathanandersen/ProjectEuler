# Problem 59
from utils import clean_list_file
import sys

text = clean_list_file("p059_cipher.txt")

#the key is 'god'
def decode(text,key):
    temp_text = []
    for i in range(len(text)):
        temp_text.append(text[i] ^ ord(key[i%3]))
        # duplicate it
    for i in range(len(temp_text)-5):
        if (temp_text[i] == ord('T') and
            temp_text[i+1] == ord('h') and
            temp_text[i+2] == ord('e') and
            temp_text[i+3] == ord(' ')):
            return temp_text

#print(decode(text,'god'))
decoded = decode(text,'god')
for char in decoded:
    print(chr(char),end='')
print()
print(sum(num for num in decoded))
