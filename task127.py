name_1 = input('Enter first file name: ')
name_2 = input('Enter first file name: ')
stack = []
with open(name_1, 'r+') as f1:
    for line in f1:
        stack.append(line)
print(stack)
with open(name_2, 'w+') as f2:
    for i in range(0, len(stack)):
        f2.writelines(str(i + 1) + ': ' + stack[i])
with open(name_2, 'r+') as f3:
    print(f3.read())