def create_dict():
    power_of_number = 2
    dictionary = dict()
    for i in range(1, 11):
        dictionary[i] = pow(i, power_of_number)
    print(dictionary)


create_dict()