cur_lsit = []
str = "this2016"
for i in str:
    if i.isalpha():
        cur_lsit.append(i)

print(''.join(cur_lsit))

str = "23443434"
print (str.isnumeric())