class MyException(Exception):
    def __str__(self):
        return 'Ошибка!'


def Solution(log):
    try:
        if log.islower():
            print('Логин добавлен в базу')
        else:
            raise MyException
    except MyException as e:
        print(e)
    finally:
        print('Я выучил исключения')