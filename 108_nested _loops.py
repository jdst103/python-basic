# Looping over embeded list

normal_list = [1, 2, 3, 4, 5]
embeded_list = [[1,2, 3,], [4, 5, 6]]

# for num in normal list:
#   print(num * 3.5)

# for data in embeded_list:
#     print(data)
#     #print(type(data))
#     for num in data:
#         print(num)

dict_data = {1: {'name': 'Stanley Ho', 'money': '$0.05'},
             2: {'name': 'Jeff Bezzos', 'money': '$0.08'},
             3: {'name': 'Trump', 'money': '$0.02'}}

# objective
# --> name
# -- > money * 4000000

#counter = 1

for key_dict1 in dict_data:
    #print(key_dict1)
   # print(dict_data[key_dict1])
    sub_dict = dict_data[key_dict1]
    #print(sub_dict)
    print(sub_dict['name'])
    #print(counter, '-', sub_dict['name'])
    money_var = float(sub_dict['money'].replace('$', ''))
    money_var = money_var * 4000000
    money_string = str(money_var)
    print('$' + money_string)
   # counter = counter + 1

