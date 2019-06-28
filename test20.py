

my_list = ['K', 'P', 'N', ' ', 'N', 'L', '\n', 'T', '#', '3', ':', '3', '2', '\n', '@', ' ', '1', ' ', '0', ' ', '*', ' ', 'O', '\n', '4', '\n', 'C', 'P', '7', '3', '8', '\n', 'L', 'i', 'l', 'e', 'e', 'p', '\n', '1', '0', '7', ' ', '/', ' ', '1', '0', '7', ' ', 'H', 'P', '\n', '2', '8', '.', '0', '2', 'k', 'g', '\n', '1', '.', '0', '3', 'm', '\n', 'H', 'E', 'I', 'G', 'H', 'T', '\n', 'W', 'E', 'I', 'G', 'H', 'T', '\n', 'R', 'O', 'C', 'K', ' ', '/', ' ', 'G', 'R', 'A', 'S', 'S', '\n', '1', '2', '4', ',', '0', '8', '2', '\n', 'S', 'T', 'A', 'R', 'D', 'U', 'S', 'T', '\n', '6', '3', '\n', 'L', 'I', 'L', 'E', 'E', 'P', ' ', 'C', 'A', 'N', 'D', 'Y', '\n', 'P', 'O', 'W', 'E', 'R', ' ', 'U', 'P', '\n', '1', '3', ',', '0', '0', '0', '\n', '3', '\n', '*', ' ', 'E', 'V', 'O', 'L', 'V', 'E', '\n', '5', '0', '\n', 'N', 'E', 'W', ' ', 'A', 'T', 'T', 'A', 'C', 'K', '\n', '5', '0', ',', '0', '0', '0', '\n', '5', '0', '\n']


cp = []
name = []
hp = []
dust = []

for idx, val in enumerate(my_list):
    if val == 'C' and my_list[idx + 1] == 'P':
        for idx1, val1 in enumerate(my_list[idx + 2:]):
            if val1 != '\n':
                cp.append(val1)
            else:
                flag = 0
                for idx2, val2 in enumerate(my_list[idx + idx1 + 2:]):
                    if val2 != '\n':
                        name.append(val2)
                    else:
                        flag += 1
                        if flag == 2:
                            for idx3, val3 in enumerate(my_list[idx + idx1 + idx2 + 3:]):
                                if val3 != '\n' and val3 != ' ' and val3 != '/':
                                    hp.append(val3)
                                elif val3 == ' ' and my_list[idx + idx1 + idx2 + idx3 + 2] == '/':
                                    new_lsit = my_list[idx + idx1 + idx2 + idx3 + 3:]
                                    for idx4, val4 in enumerate(my_list[idx + idx1 + idx2 + idx3 + 3:]):
                                        if val4 == ' ' and new_lsit[idx4 + 1] == 'U' and new_lsit[idx4 + 2] == 'P':

                                            flagI = 0
                                            for idx5, val5 in enumerate(my_list[idx + idx1 +
                                                                                idx2 + idx3 + idx4 + 3 + 2 + 1:]):
                                                if val5 != '\n' and val5 != ',':
                                                    dust.append(val5)
                                                else:
                                                    flagI += 1
                                                    if flagI >= 3:
                                                        break
                                                    else:
                                                        continue
                                        # pass]
                                        # break
                                            break
                                    break
                            break
                        else:
                            continue
                break

        break

print(''.join(cp))
print("##################################")
print(''.join(name))
print(''.join(hp))
print(''.join(dust))
