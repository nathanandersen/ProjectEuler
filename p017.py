# Problem 17
# How many letters are used when you count one to one thousand inclusive?


# Count one to nine
ones = ["","one","two","three","four","five","six","seven","eight","nine","onethousand"]
# Contains 0-9
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
# Contains 10 - 19

#Contains 0,10,20,30,40,... 90
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
# Contains "one hundred and".. one thousand and
hundreds = ["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred","onethousand"]
and_len = 3

def word_length(i):
    count = len(hundreds[int(i/100)])
    if i%100:
        count += and_len if (i%100 and i>100) else 0
        if int((i%100)/10) == 1:
            count += len(teens[(i%100)%10])
        else:
            count += len(tens[int((i%100)/10)]) + len(ones[(i%10)])
    return count

print(sum(word_length(i) for i in range(1,1001)))
