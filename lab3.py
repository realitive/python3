import os
user = {0: ["root", "root", "admin"]}
countUsers = len(user)
standardPassword = "qwerty1"
fileBd = "123.txt"

def rewriteBd():
    f = open(fileBd, 'w')
    for i in range(countUsers):
        f.write(str(i) + " " + user[i][0] + " " + user[i][1] + " " + user[i][2] + "\n")
    f.close()

def initBd():
    global countUsers
    OpenFile = True
    try:
        f = open(fileBd, 'r')
    except FileNotFoundError:
        OpenFile = False
    if OpenFile:
        for line in f:
            length = len(line)
            data = []
            j = 0
            temp = ""
            for i in range(length):
                if (line[i] != ' ') and (line[i] != '\n'):
                    temp += line[i]
                else:
                    data.insert(j, temp)
                    temp = ""
                    j += 1
            user[int(data[0])] = [data[1], data[2], data[3]]
        countUsers = len(user)
        f.close()
    else:
        rewriteBd()
    return

def cls():
    os.system('CLS')

def register(role = False):
    cls()
    print("Регистрация пользователя")
    check = True
    default = "user"
    global countUsers

    while check:
        login = input("Придумайте логин: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("Логин уже используется,придумайте пожалуйста новый логин!")
                check = True
                break

    password = input("Придумайте пароль: ")
    if role:
        print("Роль")
        print("1. Администратор")
        print("2. Пользователь")
        Choice = int(input("Выберите роль: "))
        if Choice == 1:
            default = "admin"
        else:
            default = "user"

    user[countUsers] = [login, password, default]
    countUsers = len(user)
    rewriteBd()
    print("Пользователь успешно зарегестрирован!")
    os.system('pause')
    return

def displayUsers():
    cls()
    print("ID\t\tLogin\t\tPassword\t\tRole")
    for i in range(countUsers):
        print(str(i)+"\t\t"+user[i][0]+"\t\t"+user[i][1]+"\t\t\t"+user[i][2])
    os.system('pause')
    return

def changeLogin(id):
    cls()
    print("Изменение логина")
    check = True
    while check:
        login = input("Придумайте новый логин: ")
        check = False
        for i in range(countUsers):
            if login == user[i][0]:
                print("Данный логин уже существует,придумайте пожалуйста новый логин!")
                check = True
                break
    user[id][0] = login
    print("Логин успешно изменен!")
    rewriteBd()
    os.system('pause')
    return

def changePassword(id):
    cls()
    print("Изменение пароля")
    user[id][1] = input("Придумайте пароль: ")
    print("Пароль успешно изменен!")
    rewriteBd()
    os.system('pause')
    return

def resetPassword():
    cls()
    print("Сбросить пароль")
    id = int(input("Введите ID пользователя "))
    if (id >= countUsers) and (id < 0):
        print("Такого ID нет в базе данных! Введите заново ID пользователя")
    else:
        user[id][1] = standardPassword
        print("Пароль успешно был сброшен!")
        rewriteBd()
    os.system('pause')
    return

def changeRole():
    cls()
    print("Изменить роль пользователя")
    id = int(input("Введите ID пользователя: "))
    if (id >= countUsers) and (id < 0):
        print("Такого ID нет в базе данных! Введите заново ID пользователя!")
    else:
        print("Роль")
        print("1. Администратор")
        print("2. Пользователь")
        Choice = int(input("Выберите роль: "))
        default = "user"
        if Choice == 1:
            default = "admin"
        user[id][2] = default
        print(user[id][0] + " изменен на " + user[id][2])
        rewriteBd()
        os.system('pause')
    return

def Apanel(id):
    work = True
    MyId = id
    while work:
        cls()
        if user[MyId][2] == "user":
            print("С вас были сброшены привилегии!")
            os.system('pause')
            return
        print("Вы вошли в систему как администратор!("+user[MyId][0]+")")
        print("1. Создать пользователя")
        print("2. Изменить логин")
        print("3. Изменить пароль")
        print("4. Сброс пароля пользователя")
        print("5. Показать всех пользователей")
        print("6. Изменить роль пользователя")
        print("7. Выйти из аккаунта")
        print("8. Выход")
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            register(True)
        elif choice == 2:
            changeLogin(MyId)
        elif choice == 3:
            changePassword(MyId)
        elif choice == 4:
            resetPassword()
        elif choice == 5:
            displayUsers()
        elif choice == 6:
            changeRole()
        elif choice == 7:
            work = False
        elif choice == 8:
            exit(0)

def Upanel(id):
    work = True
    MyId = id
    while work:
        cls()
        print("Вы вошли как пользователь!(" + user[MyId][0] + ")")
        print("1. Изменить логин")
        print("2. Изменить пароль")
        print("3. Выйти с аккаунта")
        print("4. Выход")
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            changeLogin(MyId)
        elif choice == 2:
            changePassword(MyId)
        elif choice == 3:
            work = False
        elif choice == 4:
            exit(0)

def signIn():
    cls()
    print("Вход в систему")
    login = input("Введите логин: ")
    password = input("Введте пароль: ")
    for i in range(countUsers):
        if (login == user[i][0]) and (password == user[i][1]):
            print("Вы вошли в систему!")
            if user[i][2] == "admin":
                Apanel(i)
            else:
                Upanel(i)
            return
    print("Логин или пароль были введены не верно! Введите пароль или логин заново")
    os.system('pause')
    return

def main():
    initBd()
    work = True

    while work:
        cls()
        print("Mеню: ")
        print("1. Вход в систему")
        print("2. Регистрация в системе")
        print("3. Выход")
        choice = int(input("Ваш выбор: "))
        if choice == 1:
            signIn()
        elif choice == 2:
            register()
        elif choice == 3:
            work = False
        else:
            print("Такого действие нельзя выполнить!")
            os.system('pause')
    return

main()