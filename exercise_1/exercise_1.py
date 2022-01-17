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





