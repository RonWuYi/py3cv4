import os

# 107  39 40 41
my_list = ['K', 'P', 'N', ' ', 'N', 'L', '\n', 'T', '#', '3', ':', '3', '2', '\n', '@', ' ', '1', ' ', '0', ' ', '*', ' ', 'O', '\n', '4', '\n', 'C', 'P', '7', '3', '8', '\n', 'L', 'i', 'l', 'e', 'e', 'p', '\n', '1', '0', '7', ' ', '/', ' ', '1', '0', '7', ' ', 'H', 'P', '\n', '2', '8', '.', '0', '2', 'k', 'g', '\n', '1', '.', '0', '3', 'm', '\n', 'H', 'E', 'I', 'G', 'H', 'T', '\n', 'W', 'E', 'I', 'G', 'H', 'T', '\n', 'R', 'O', 'C', 'K', ' ', '/', ' ', 'G', 'R', 'A', 'S', 'S', '\n', '1', '2', '4', ',', '0', '8', '2', '\n', 'S', 'T', 'A', 'R', 'D', 'U', 'S', 'T', '\n', '6', '3', '\n', 'L', 'I', 'L', 'E', 'E', 'P', ' ', 'C', 'A', 'N', 'D', 'Y', '\n', 'P', 'O', 'W', 'E', 'R', ' ', 'U', 'P', '\n', '1', '3', ',', '0', '0', '0', '\n', '3', '\n', '*', ' ', 'E', 'V', 'O', 'L', 'V', 'E', '\n', '5', '0', '\n', 'N', 'E', 'W', ' ', 'A', 'T', 'T', 'A', 'C', 'K', '\n', '5', '0', ',', '0', '0', '0', '\n', '5', '0', '\n']

# global x
cp = []
name = []
hp = []
dust = []
position = 0
for i in my_list:
    # position += 1
    if i == 'C' and my_list[my_list.index(i) + 1] == 'P':
        position += my_list.index(i)
        for ii in my_list[my_list.index(i) + 2:]:
            if ii != '\n':
                cp.append(ii)
            else:
                position += len(cp) + 2
                flag = 0
                for iii in my_list[my_list.index(i) + 2 + len(cp):]:
                    # position = my_list.index(iii)
                    if iii != '\n':
                        name.append(iii)
                    else:
                        position += len(name) + 1
                        flag += 1
                        if flag == 2:
                            for iv in my_list[position:]:
                                if iv != '\n' and iv != ' ':
                                    hp.append(iv)
                                elif iv == ' ' and my_list[my_list.index(iv)] == '/':
                                    break
                            break
                        else:
                            continue
                    # break
                break

        break

print(''.join(cp))
print("##################################")
print(''.join(name))
print(''.join(hp))
