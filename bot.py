import sys
import string
import requests
import os

from threading import Thread, Timer
from json import load
from time import sleep, strftime
from fake_useragent import UserAgent

ua = UserAgent()

def idk():
    print("Я не знаю что мне делать")
    sleep(99999)

def error():
    print("Неверный Token в config.json")
    sleep(99999)    

def checktoken():
    try:
        response = requests.post(
            "https://slaves21.publicvm.com/app/api.php?" + auth,
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "22",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Host": "slaves21.publicvm.com",
                "Origin": "https://slaves21.publicvm.com",
                "Referer": "https://slaves21.publicvm.com/app/api.php" + auth, 
                "sec-ch-ua": "'Google Chrome';v='89', 'Chromium';v='89', ';Not A Brand';v='99'",
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": ua['google chrome'],
                "X-Requested-With": "XMLHttpRequest",
            },
            data={
                "notify": "true",
                "method": "info",
            }
        )
        if response.text == "Invalid sign":
            mess = "error"
        else:
            mess = "success"
        return mess
    except Exception as e:
        mess = "error"
        return mess

def raz(asd):
    return '{:,}'.format(asd).replace(',', '.')

def asd():
    return

def profile(asd):
    if asd == "asd":
        Timer(60, profile).start()
        try:
            response = requests.post(
                "https://slaves21.publicvm.com/app/api.php?" + auth,
                headers={
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Length": "22",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "slaves21.publicvm.com",
                    "Origin": "https://slaves21.publicvm.com",
                    "Referer": "https://slaves21.publicvm.com/app/api.php" + auth, 
                    "sec-ch-ua": "'Google Chrome';v='89', 'Chromium';v='89', ';Not A Brand';v='99'",
                    "sec-ch-ua-mobile": "?0",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": ua['google chrome'],
                    "X-Requested-With": "XMLHttpRequest",
                },
                data={
                    "notify": "true",
                    "method": "info",
                }
            )
            print(
                "\nОбнаружил аккаунт: " + response.json()['res']['name'] +
                "\n -> Ваш владелец: " + response.json()['res']['owner']['name'] +
                "\n -> Место в топе: " + response.json()['res']['myrating'] +
                "\n -> Ваш баланс: " + response.json()['res']['balance'] + "\n"
            )
        except Exception as e:
            print(" - | Ошибка")
        sleep(4)

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

def farm():
    while True:
        try:
            response = requests.post(
                "https://slaves21.publicvm.com/app/api.php?" + auth,
                headers={
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Connection": "keep-alive",
                    "Content-Length": "22",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Host": "slaves21.publicvm.com",
                    "Origin": "https://slaves21.publicvm.com",
                    "Referer": "https://slaves21.publicvm.com/app/api.php" + auth, 
                    "sec-ch-ua": "'Google Chrome';v='89', 'Chromium';v='89', ';Not A Brand';v='99'",
                    "sec-ch-ua-mobile": "?0",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": ua['google chrome'],
                    "X-Requested-With": "XMLHttpRequest",
                },
                data={
                    "method": "on_watсhed",
                }
            )
            print(
                " + | Новый баланс: " + raz(int(response.json()['changes']['balance'])) + ""
            )
        except Exception as e:
            print(" - | Ошибка")
            # print(e)
        sleep(4)

if __name__ == "__main__":
    global token
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "Вас приветствует бот для Рабство 2.0 / vk.com/watershack\n" +
        "   Version: 1.0.0\n" +
        "Мои команды:\n" +
        "   1. token - для изменения подключения к аккаунту\n" +
        "   2. run - для запуска бота\n" +
        "   3. error - для просмотра или решения ошибок\n" +
        "   4. ask - как узнать свой токен"
    )
    token = input("\nВведите цифру команду: ")

    if token == "1" or token == "token":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Вы успешно зашли в меню редактирования токена\n")
        newtoken = input("Введите ваш новый токен: ")
        infile = open('config.json', 'r+')
        content = infile.readlines()
        content[1] = '  "authorization": "' + newtoken + '",\n'
        infile.close
        infile = open('config.json', 'w')
        infile.close
        infile = open('config.json', 'r+')
        for item in content:
            infile.write("%s" % item)
        infile.close()
        print("Вы успешно изменили токен\nНажмите любую кнопку для продолжения...")
        com = input()
        execfile("bot.py")
    if token == "2" or token == "run":
        os.system('cls' if os.name == 'nt' else 'clear')
        with open("config.json") as f:
            try:
                config = load(f)
            except:
                print("Неверный конфиг")
                sys.exit()
        auth = str(config["authorization"])
        farm1 = int(config["farm"])
        checktok = checktoken()
        if checktok == "success":
            if auth == " ":
                Thread(target=error).start()
            else:
                if farm1 == 1:
                    profile("asd")
                    Thread(target=farm).start()
                elif farm1 == 0:
                    Thread(target=idk).start()  
        else:
            print("Неверный токен! Измените его")
            asdasda = input("Нажмите любую кнопку для продолжения...")
            execfile("bot.py")
    if token == "3" or token == "error":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            "Возможные ошибки:\n" +
            "   1. '- | Ошибка':\n" +
            "       Либо у вас нет интернета, либо у вас неправильно введен токен\n"
        )
        newcom = input("\nНажмите любую кнопку для продолжения...")
        execfile("bot.py")
    if token == "4" or token == "ask":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            '1. Открываешь приложение: "F12"' +
            '\n2. В гугл вводишь "ВК"' +
            '\n3. Там входишь в свою страницу' +
            '\n4. Сверху в меню ВК нажимаешь на три полоски' +
            '\n5. Заходишь в приложение "Рабство 2.0"' +
            '\n6. Слева снизу есть иконка "F12", нажимаешь на нее' +
            '\n7. Там заходишь в вкладку "Network"' +
            '\n8. Ставишь галочки на "Preserve" и "Advance"' +
            '\n9. Слева сверху в приложении есть кнопка перезагрузить, нажимаешь на нее' +
            '\n10. Нажимаешь на надпись в Network которая появилась' +
            '\n11. Копируешь всё после "https://slaves21.publicvm.com/app/app.php?", копируем без вопросительного знака'
        )
        newcom = input("\nНажмите любую кнопку для продолжения...")
        execfile("bot.py")
    if token == "token" or token == "1" or token == "2" or token == "3" or token == "4" or token == "run" or token == "error" or token == "ask":
        asd()
    else:
        print("\nНеизвестная команда")
        asdasda = input("Нажмите любую кнопку для продолжения...")
        execfile("bot.py")