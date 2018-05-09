import random
import itertools

def createCode():
    result = ""
    ch = str(round(random.uniform(0, 9)))
    work = True
    while(work):
        if ch in result:
            ch = str(round(random.uniform(0, 9)))
        else:
            result += ch
        if len(result) >= 4:
            work = False
    return result

def Check(data):
    for i in range(len(data)):
        j = i + 1
        while (j < len(data)):
            if (data[i] == data[j]) :
                return False
            j += 1
    return True

def CheckBulls(secret, data):
    result = 0
    for i in range(len(secret)):
        if secret[i] == data[i]:
            result += 1
    return result

def CheckCows(secret, data):
    result = 0
    for i in range(len(secret)):
        j = 0
        while(j < len(secret)):
            if (data[i] == secret[j] and i != j):
                result += 1
            j += 1
    return result

def userPlay(secret):
    countTry = 0
    countBulls = 0
    countCows = 0
    work = True
    while work:
        while (True):
            inData = input("Введите 4-х значное число: ")
            res = len(inData)
            if (res == 4) and Check(inData):
                countTry += 1
                break
            else:
                print("Вы вели некоректное число!")
        print(inData)
        countBulls = CheckBulls(secret, inData)
        countCows = CheckCows(secret, inData)
        print(str(countBulls) + " Быки " + str(countCows) + " Коровы!")
        if (countBulls == 4):
            print("Вы угадали число с " + str(countTry) + " попыток!")
            work = False



def main():
    secret = createCode()
    print("1 - Вы готовы к игре?Если да, то нажмите 1")
    choice = input('Ваш выбор: ')
    if choice == '1':
        userPlay(secret)
    else:
        print("Ошибка!!!")
main()