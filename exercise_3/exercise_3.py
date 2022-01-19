def task1():
    value = int(input("Enter some integer: "))

    if(value % 2):
        print("Odd")
    else:
        print("Even")

def task2():
    value = int(input("Enter month number: "))

    if(value in range(3, 6)):
        print("Spring")
    elif(value in range(6, 9)):
        print("Summer")
    elif (value in range(9, 12)):
        print("Autumn")
    elif(value in (1, 2, 12)):
        print("Winter")
    else:
        print("Invalid month number")

def task3():
    value = [6, 3, -1, 1, 1]
    min_num = None
    #var1
    #print(min(value))

    #var2 - last array index is not in use
    for i in range(len(value)-1):
        temp_min = 0
        if value[i] > value[i+1]:
            temp_min = value[i]
            if(min_num != None):
                if(temp_min < min_num):
                    min_num = temp_min
                else:
                    pass
            else:
                min_num = temp_min
        else:
            pass

    print(min_num)

def task4():
    for i in range(1, 101):
        if ((i % 15) == 0):
            print("FizzBuzz")
        elif ((i % 3) == 0):
            print("Fizz")
        elif ((i % 5) == 0):
            print("Buzz")
        else:
            print(i)

a = [4,2,1]
def task5(x):
    sum = 0
    for i in x:
       sum = sum + i

    print(sum)

def task6(x):
    sum = 0
    i = 0
    while i != len(x):
        sum = sum + x[i]
        i += 1
    print(sum)

task6(a)

