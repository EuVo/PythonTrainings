def task1():
    price = 5.99

    rubles = str(price).split('.')[0]
    cents = str(price).split('.')[1]

    print(f'Rubles: {rubles}, cents: {cents}')

def task2():
    digit = input("Integer: ")
    arr = list(digit)
    for i in range(len(arr)):
        print(f'{i+1} digit equal to {arr[i]}')

#cut symbols between first and last 'h'
def task3():
    value = "aqwrhgdsdfghtyopthahnum"

    #VAR1
    # array of symbols
    arr = list(value)
    # array ids of 'h' position
    res = []
    # resulted array
    fin = []
    result_string = ""

    # get ids of 'h' position
    for i in range(len(arr)):
        if arr[i] == "h":
            res.append(i)
        else:
            pass

    # get resulted array
    for x in range(len(arr)):
        if x < res[0] or x > res[len(res)-1]:
            fin.append(arr[x])
        else:
            pass

    print(result_string.join(fin))

    #VAR2
    #res = value.split("h")
    #print(res[0] + res[len(res)-1])

def task4():
    value = "first second"

    #VAR2
    result = value.split(' ')
    result[0], result[1] = result[1], result[0]
    print(" ".join(result))

def task5():
    value = "first sec third fourth"
    result = value.split(' ')
    print(len(result))

task5()


