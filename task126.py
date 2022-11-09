"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""
with open('joke2.txt', 'w') as f:
    f.write(', но у меня не получается')
with open('joke.txt', 'r') as a:
    text = a.readline()
print(text)
with open('joke2.txt', 'r') as b:
    t = b.readline()
print (t)
with open('joke3.txt', 'w') as h:
    h.write(text + t)