#Problem 40
int_str = ""

for i in range(1000000):
    int_str += str(i)

print(int(int_str[1])*
      int(int_str[10])*
      int(int_str[100])*
      int(int_str[1000])*
      int(int_str[10000])*
      int(int_str[100000])*
      int(int_str[1000000]))
