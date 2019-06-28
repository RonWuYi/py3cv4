import string


# print(string.ascii_letters)

my_list = ['K', 'P', 'N', ' ', 'N', 'L', '\n', 'T', '#', '3', ':', '3', '2', '\n', '@', ' ', '1', ' ', '0', ' ', '*', ' ', 'O', '\n', '4', '\n', 'C', 'P', '7', '3', '8', '\n', 'L', 'i', 'l', 'e', 'e', 'p', '\n', '1', '0', '7', ' ', '/', ' ', '1', '0', '7', ' ', 'H', 'P', '\n', '2', '8', '.', '0', '2', 'k', 'g', '\n', '1', '.', '0', '3', 'm', '\n', 'H', 'E', 'I', 'G', 'H', 'T', '\n', 'W', 'E', 'I', 'G', 'H', 'T', '\n', 'R', 'O', 'C', 'K', ' ', '/', ' ', 'G', 'R', 'A', 'S', 'S', '\n', '1', '2', '4', ',', '0', '8', '2', '\n', 'S', 'T', 'A', 'R', 'D', 'U', 'S', 'T', '\n', '6', '3', '\n', 'L', 'I', 'L', 'E', 'E', 'P', ' ', 'C', 'A', 'N', 'D', 'Y', '\n', 'P', 'O', 'W', 'E', 'R', ' ', 'U', 'P', '\n', '1', '3', ',', '0', '0', '0', '\n', '3', '\n', '*', ' ', 'E', 'V', 'O', 'L', 'V', 'E', '\n', '5', '0', '\n', 'N', 'E', 'W', ' ', 'A', 'T', 'T', 'A', 'C', 'K', '\n', '5', '0', ',', '0', '0', '0', '\n', '5', '0', '\n']
my_list2 = ['.', '.', '1', ' ', 'K', 'P', 'N', ' ', 'N', 'L', '\n', 'T', 'F', '3', ':', '3', '2', '\n', '@', '\n', '1', ' ', '0', ' ', '*', '\n', '4', '\n', 'C', 'P', '7', '7', '0', '\n', '2', '0', '1', '8', '\n', '1', '1', '/', '1', '1', '\n', 'M', 'a', 'n', 't', 'i', 'n', 'e', '\n', '8', '6', '/', ' ', '8', '6', ' ', 'H', 'P', '\n', '2', '.', '2', '5', 'm', '\n', '2', '0', '9', '.', '6', '8', 'k', 'g', '\n', 'W', 'E', 'I', 'G', 'H', 'T', '\n', 'W', 'A', 'T', 'E', 'R', ' ', '/', ' ', 'F', 'L', 'Y', 'I', 'N', 'G', '\n', 'H', 'E', 'I', 'G', 'H', 'T', '\n', '|', ' ', '1', '2', '4', ',', '0', '8', '2', '\n', 'S', 'T', 'A', 'R', 'D', 'U', 'S', 'T', '\n', '1', '1', '\n', 'M', 'A', 'N', 'T', 'I', 'N', 'E', ' ', 'C', 'A', 'N', 'D', 'Y', '\n', 'P', 'O', 'W', 'E', 'R', ' ', 'U', 'P', '\n', '1', ',', '6', '0', '0', '\n', '2', '\n', 'N', 'E', 'W', ' ', 'A', 'T', 'T', 'A', 'C', 'K', '\n', '7', '5', ',', '0', '0', '0', '\n', '7', '5', '\n', 'G', 'Y', 'M', 'S', ' ', '&', ' ', 'R', 'A', 'I', 'D', 'S', '\n', 'T', 'R', 'A', 'I', 'N', 'E', 'R', ' ', 'B', 'A', 'T', 'T', 'L', 'E', 'S', '\n']


new_lsit = [x for x in my_list if x in string.ascii_letters or x in string.octdigits]
print(new_lsit)


#
# fixed_list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
#
# fixed_list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
#
# fixed_list3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
#
cp = []
name = []
hp = []
dust = []

# for idx, val in enumerate(new_lsit):
#     if val == 'C' and my_list2[idx + 1] == 'P':
#         for idx1, val1 in enumerate(my_list2[idx + 2:]):
#             if val1.isdigit():
#                 cp.append(val1)
#             else:
#                 for idx2, val2 in enumerate(my_list2[idx + idx1 + 2:]):
#                     if val2.isalpha():
#                         name.append(val2)
#                     else:
#                         # flag += 1
#                         # if flag == 2:
#                             for idx3, val3 in enumerate(my_list2[idx + idx1 + idx2 + 3:]):
#                                 if val3.isdigit():
#                                     hp.append(val3)
#                                 elif val3 == ' ' and my_list2[idx + idx1 + idx2 + idx3 + 2] == '/':
#                                     new_lsit = my_list2[idx + idx1 + idx2 + idx3 + 3:]
#                                     for idx4, val4 in enumerate(my_list2[idx + idx1 + idx2 + idx3 + 3:]):
#                                         if val4 == ' ' and new_lsit[idx4 + 1] == 'U' and new_lsit[idx4 + 2] == 'P':
#                                             flagI = 0
#                                             for idx5, val5 in enumerate(my_list2[idx + idx1 +
#                                                                                  idx2 + idx3 + idx4 + 3 + 2 + 1:]):
#                                                 if val5.isdigit():
#                                                     dust.append(val5)
#                                                 else:
#                                                     flagI += 1
#                                                     if flagI >= 3:
#                                                         break
#                                                     else:
#                                                         continue
#                                         # pass]
#                                         # break
#                                             break
#                                     break
#                             break
#                         else:
#                             continue
#                 break
#
#         break

print(''.join(cp))
print(''.join(name))
print(''.join(hp))
print(''.join(dust))

# for idx, val in enumerate(my_list):
#     if not val.isalpha():
#         if my_list[idx - 2] == 'C' and my_list[idx - 1] == 'P':
#             if val.isdigit():
#                 cp.append(val)
#             elif not val.isdigit() and not val.isalpha():
#                 continue
#             else:
#                 if not my_list[idx - 1].isalpha():
#                     name.append(val)
#                 elif val.isalpha():
#                     name.append(val)
#                 elif not my_list[idx + 1].isalpha():
#                     name.append(val)
#                     break
#
# print(''.join(cp))
# print(''.join(name))