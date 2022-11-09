def key_number_value_amount(numbers):
    list_of_numbers = []
    list_of_amount_of_numbers = []
    dict_ = dict()
    for i in range(0, len(numbers)):
        list_of_numbers.append(int(numbers[i]))
    for x in set(list_of_numbers):
        if numbers.find(str(x)) != -1:
            list_of_amount_of_numbers.append(list_of_numbers.count(x))
    j = 0
    for x in set(list_of_numbers):
        dict_[x] = list_of_amount_of_numbers[j]
        j += 1
    print(dict_)

numbers_ = "0139412831055230677798"
key_number_value_amount(numbers_)