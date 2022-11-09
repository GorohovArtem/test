def change_dictionary(my_dict):
    buffer_value1 = my_dict[1]
    my_dict[1] = my_dict[5]
    my_dict[5] = buffer_value1
    del my_dict[2]
    my_dict['new_key'] = 'new_value'
    print(my_dict)


dict_ = {1: 'a',
         2: 'b',
         3: 'c',
         4: 'd',
         5: 'e'}
change_dictionary(dict_)