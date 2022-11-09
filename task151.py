def music_chart():
    dict_ = {}
    while input != 'off':
        place = input('Введите место в чарте: ')
        if place != 'off':
            singer = input('Введите исполнителя: ')
            if singer != 'off':
                name = input('Введите название: ')
                if name != 'off':
                    if place and singer and name:
                        dict_[place, singer] = name
                else:
                    print(dict_)
            else:
                print(dict_)
        else:
            print(dict_)
    print(dict_)


music_chart()