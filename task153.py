def emails(mails):
    keys = list(mails.keys())
    values = list(mails.values())
    symbol = '@'
    try:
        for i in range(0, len(keys[0]) - 1):
            print(values[0][i] + symbol + keys[0])
    except IndexError:
        pass
    try:
        for i in range(0, len(keys[1])):
            print(values[1][i] + symbol + keys[1],
                  values[2][i] + symbol + keys[2],
                  values[4][i] + symbol + keys[4],
                  values[5][i] + symbol + keys[5])
    except IndexError:
        pass
    try:
        for i in range(0, len(keys[3]) - 1):
            print(values[3][i] + symbol + keys[3])
    except IndexError:
        pass


my_emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
             'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
             'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
             'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
             'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
             'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
emails(my_emails)