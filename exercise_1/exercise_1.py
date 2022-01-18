#Print username with format
def task1():
    name = "PythonUser"
    print(f'Username: {name}')

#Print perimeter and square of rectangle
def task2():
    a = 7
    b = 5

    perimeter = 2*(a + b)
    square = a*b

    print(f'Perimeter: {perimeter}')
    print(f'Square: {square}')

#Print money after N years contribution
def task3():
    #start money(euro)
    money = 10000

    #years of contributions
    years = 3

    percents = 10000 * (1+0.1*3)
    print(f'Money with percents: {money + percents}')

#// and % execution
def task4():
    #students count
    n = 4

    #apples count in bag
    k = 6

    print(f'Apples to each students: {k//n}')
    print(f'Apples remain in bag: {k%n}')

#Print clock value after adding N minutes to day beggining
def task5():
    #minutes past from day beginning
    n = 1439

    #convert minutes to hh and mm
    hours = n // 60
    minutes = n % 60

    if(hours < 10 and minutes < 10):
        hours = "0" + str(hours)
        minutes = "0" + str(minutes)
    elif(hours > 10 and minutes < 10 ):
        minutes = "0" + str(minutes)
    elif (hours < 10 and minutes > 10):
        hours = "0" + str(hours)
    else:
        pass

    if(hours < 24):
        print(f'Clock value: {hours}:{minutes}')
    else:
        print("The 'hours' parameter can not be more or equal to 24")








