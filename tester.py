from random import randint
F = open('test_letters','r')
test_array=[]
for line in F:
    test_array.append(line)
constant=len(test_array)
for x in range(0, 3):
    print(test_array[randint(0, constant)])
    age = input(" ")