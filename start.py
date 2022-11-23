from collections import Counter


def choose_mode():        ###Начальный экран
    start_output()
    first_in = input()
    if first_in == '1':
        code_txt_choice('ru')
    elif first_in == '2':
        end_way_to_file_in()
    elif first_in == '3':
        code_txt_choice('ru', True)
    elif first_in == '4':
        end_way_to_file_in(True)
    else:
        print('Некорректный ввод')
        choose_mode()


def code_txt_choice(language, decrypt=False):           ###для текстового выбор шифрования
    output_txt()
    code_txt_in = input()
    if code_txt_in == '1':
        zesar_txt_input(decrypt)
    elif code_txt_in == '2':
        vizh_txt_input(decrypt)
    elif code_txt_in == '3':
        vernam_txt_input(decrypt)
    else:
        print('Некорректный ввод')
        code_txt_choice(language, decrypt)


def zesar_txt_input(decrypt=False):               ###для текстового ввод шифра Цезаря
    print('Введите текст:')
    txt = input()
    if(ord(txt[0]) > 1000):
        language = 'ru'
    else:
        language = 'en'
    auto = False
    if decrypt:
        print('Желаете провести автоматическую расшифровку?')
        while True:
            ch = input()
            if (ch == 'Да'):
                auto = True
                break
            elif (ch == 'Нет'):
                auto = False
                break
            else:
                print('Ошибка ввода, попробуйте еще раз')
    key_input_zesar_txt(language, txt, decrypt, auto)


def vizh_txt_input(decrypt=False):             ###для текстового ввод шифра Цезаря
    print('Введите текст:')
    txt = input()
    if ord(txt[0]) > 1000:
        language = 'ru'
    else:
        language = 'en'
    print('Введите ключ:')
    key = input()
    vizh_code_end(language, txt, key, decrypt)


def vernam_txt_input(decrypt=False):  ###для текстового ввод шифра Цезаря
    print('Введите текст:')
    txt = input()
    if ord(txt[0]) > 1000:
        language = 'ru'
    else:
        language = 'en'
    print('Введите ключ:')
    key = input()
    vernam_code_end(language, txt, key, decrypt)


def zesar_code_end(language, txt, key, decrypt=False, auto=False):               ###для текстового вывод шифра Цезаря
    if language == 'en':
        if decrypt:
            if auto:
                print('Расшифрованный текст:')
                print(zesar_out_txt_en_auto(txt))
            else:
                print('Расшифрованный текст:')
                print(zesar_out_txt_en(txt, key))
        else:
            print('Зашифрованный текст:')
            print(zesar_in_txt_en(txt, key))
    elif language == 'ru':
        if decrypt:
            if auto:
                print('Расшифрованный текст:')
                print(zesar_out_txt_ru_auto(txt))
            else:
                print('Расшифрованный текст:')
                print(zesar_out_txt_ru(txt, key))
        else:
            print('Зашифрованный текст:')
            print(zesar_in_txt_ru(txt, key))


def vizh_code_end(language, txt, key, decrypt=False):           ###для текстового вывод шифра Вижинера
    if language == 'en':
        if decrypt:
            print('Расшифрованный текст:')
            print(vizh_out_txt_en(txt, key))
        else:
            print('Зашифрованный текст:')
            print(vizh_in_txt_en(txt, key))
    elif language == 'ru':
        if decrypt:
            print('Расшифрованный текст:')
            print(vizh_out_txt_ru(txt, key))
        else:
            print('Зашифрованный текст:')
            print(vizh_in_txt_ru(txt, key))


def vernam_code_end(language, txt, key, decrypt=False):           ###для текстового вывод шифра Вижинера
    if (len(txt.replace(" ", "")) == len(key)):
        if language == 'en':
            if decrypt:
                print('Расшифрованный текст:')
                print(vizh_out_txt_en(txt, key))
            else:
                print('Зашифрованный текст:')
                print(vizh_in_txt_en(txt, key))
        elif language == 'ru':
            if decrypt:
                print('Расшифрованный текст:')
                print(vizh_out_txt_ru(txt, key))
            else:
                print('Зашифрованный текст:')
                print(vizh_in_txt_ru(txt, key))
    else:
        print('Ключ не соответствует требованиям.')


def key_input_zesar_txt(language, txt, decrypt=False, auto=False):    ###для текстового получение ключа шифра Цезаря
    if not auto:
        key_output()
        key = input()
        try:
            key = int(key)
            zesar_code_end(language, txt, key, decrypt, auto)
        except ValueError:
            print('Некорректный ключ')
            key_input_zesar_txt(language, txt, decrypt, auto)
    else:
        zesar_code_end(language, txt, 0, decrypt, auto)


def zesar_in_txt_en(txt, key):          ##процесс зашифровки англ текста Цезарем
    f = ord('a')
    l = ord('z')
    txt = txt.lower()
    txt_zesar = ''
    n = 26
    for i in txt:
        if 'z' >= i >= 'a':
            txt_zesar += chr((ord(i) - l - 1 + key) % n + f)
        else:
            txt_zesar += i
    return txt_zesar


def zesar_in_txt_ru(txt, key):          ###процесс зашифровки рус текста Цезарем
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    txt = txt.lower()
    txt_zesar = ""
    for letter in txt:
        position = alphabet.find(letter)
        newPosition = position + key
        if letter in alphabet:
            txt_zesar = txt_zesar + alphabet[newPosition % 33]
        else:
            txt_zesar = txt_zesar + letter
    return txt_zesar


def zesar_in_file(way_to_file, key):        ###процесс зашифровки файла Цезарем
    f = open(way_to_file, 'rb')
    n = 256
    bs = f.read()
    crypt_bs = []
    for bit in bs:
        crypt_bs.append((bit + key) % n)
    f.close()
    f = open(way_to_file, 'wb')
    f.write(bytes(crypt_bs))
    f.close()


def vizh_in_txt_en(txt, key_w, mult=1):      ###процесс зашифровки англ текста Вижинером
    f = ord('a')
    l = ord('z')
    txt = txt.lower()
    key_w = key_w.lower()
    txt_vizh = ''
    n = 26
    index_of_key = 0
    for i in txt:
        if 'z' >= i >= 'a':
            key = ord(key_w[index_of_key % len(key_w)]) - f
            index_of_key += 1
            txt_vizh += chr((ord(i) - l - 1 + key * mult) % n + f)
        else:
            txt_vizh += i
    return txt_vizh


def vizh_in_txt_ru(txt, key_w, mult=1):  ###процесс зашифровки рус текста Вижинером
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    f = alphabet.find('а')
    l = alphabet.find('я')
    txt = txt.lower()
    key_w = key_w.lower()
    txt_vizh = ''
    n = 33
    index_of_key = 0
    for i in txt:
        if i in alphabet:
            key = alphabet.find(key_w[index_of_key % len(key_w)]) - f
            txt_vizh += alphabet[(alphabet.find(i) - l - 1 + key * mult) % n + f]
        else:
            txt_vizh += i
        index_of_key += 1
    return txt_vizh


def vizh_in_file(way_to_file, key_w, mult=1):      ###процесс зашифровки файла Вижинером
    f = open(way_to_file, 'rb')
    n = 256
    bs = f.read()
    key_w = key_w.lower()
    crypt_bs = []
    index_of_key = 0
    for bit in bs:
        key = ord(key_w[index_of_key % len(key_w)])
        crypt_bs.append((bit + key*mult) % n)
        index_of_key += 1
    f.close()
    f = open(way_to_file, 'wb')
    f.write(bytes(crypt_bs))
    f.close()


def vernam_in_txt_ru(txt, key_txt):            ###процесс зашифровки рус текста Вернамом
    if len(txt) == len(key_txt):
        vizh_in_txt_ru(txt, key_txt)


def vernam_in_txt_en(txt, key_txt):            ###процесс зашифровки англ текста Вернамом
    if len(txt) == len(key_txt):
        vizh_in_txt_en(txt, key_txt)


def zesar_out_txt_en(txt, key):   ##процесс расшифровки англ текста Цезарем
    return zesar_in_txt_en(txt, -key)


def zesar_out_txt_en_auto(txt):   ###процесс авторасшифровки англ текста Цезарем
    c = Counter(txt)
    key = ord(c.most_common(1)[0][0]) - ord('e')
    return zesar_in_txt_en(txt, -key)


def zesar_out_txt_ru(txt, key):           ###процесс расшифровки рус текста Цезарем
    return zesar_in_txt_ru(txt, -key)


def zesar_out_txt_ru_auto(txt):           ###процесс авторасшифровки рус текста Цезарем
    c = Counter(txt)
    key = ord(c.most_common(1)[0][0]) - ord('о')
    return zesar_in_txt_ru(txt, -key)


def zesar_out_file(way_to_file, key):        ###процесс расшифровки файла Цезарем
    zesar_in_file(way_to_file, -key)


def vizh_out_txt_en(txt, key_w):          ###процесс расшифровки англ текста Вижинером
    return vizh_in_txt_en(txt, key_w, -1)


def vizh_out_txt_ru(txt, key_w):        ###процесс расшифровки рус текста Вижинером
    return vizh_in_txt_ru(txt, key_w, -1)


def vizh_out_file(way_to_file, key_w):           ###процесс расшифровки файла Вижинером
    vizh_in_file(way_to_file, key_w, -1)


def vernam_out_txt_en(txt, key_txt):            ###процесс расшифровки англ текста Вернамом
    if len(txt) == len(key_txt):
        vizh_in_txt_en(txt, key_txt, mult=-1)


def vernam_out_txt_ru(txt, key_txt):            ###процесс расшифровки рус текста Вернамом
    if len(txt) == len(key_txt):
        vizh_in_txt_ru(txt, key_txt, mult=-1)


def final():                     ###Конечная
    end_output()
    end_in = input()
    if end_in == '1':
        choose_mode()
        final()
    if end_in == '2':
        pass


def end_way_to_file_in(decrypt=False):      ###для файлового ввода запрос с проверками на корректности пути до файла
    print('Введите путь к файлу:')
    way_to_file = input()
    try:
        f = open(way_to_file, 'rb+')
        f.close()
        code_file_choice(way_to_file, decrypt)
    except PermissionError:
        print('Нет доступа')
        end_way_to_file_in(decrypt)
    except FileNotFoundError:
        print("Файл не найден")
        end_way_to_file_in(decrypt)
    except OSError:
        print('Странные штуки, давайте что-то другое')
        end_way_to_file_in(decrypt)


def zesar_code_file_end(way_to_file, key, decrypt=False):               ###для файлового ввода за/расшифровка файла Цезарем и замена
    if decrypt:
        zesar_out_file(way_to_file, key)
        print('Расшифровка прошла успешно')
    else:
        zesar_in_file(way_to_file, key)
        print('Шифрование завершено')


def zesar_key_files(way_to_file, decrypt=False):                         ###для файлового ввода проверка ключа
    key_output()
    key = input()
    try:
        key = int(key)
        zesar_code_file_end(way_to_file, key, decrypt)
    except ValueError:
        print('Некорректный ключ')
        zesar_key_files(way_to_file, decrypt)


def vizh_code_file_end(way_to_file, decrypt=False):                ###для файлового ввода за/расшифровка файла Вижинером и замена
    key_output()
    key = input()
    if decrypt:
        vizh_out_file(way_to_file, key)
        print('Расшифровка прошла успешно')
    else:
        vizh_in_file(way_to_file, key)
        print('Шифрование завершено')


def code_file_choice(way_to_file, decrypt=False):                  ###для файлового ввода выбор за/расшифровки
    output_files()
    code_files_in = input()
    if code_files_in == '1':
        zesar_key_files(way_to_file, decrypt)
    elif code_files_in == '2':
        vizh_code_file_end(way_to_file, decrypt)
    else:
        print('Некорректный ввод')
        code_file_choice(way_to_file, decrypt)


def start_output():                                     ###старт общий
    print('Выберите тип шифрования:')
    print('1. Шифровка текста')
    print('2. Шифровка файла')
    print('3. Расшифровка текста')
    print('4. Расшифровка файла')


def output_files():                                    ###старт для файла
    print('Выберите шифрование:')
    print('1. Шифр Цезаря')
    print('2. Шифр Виженера')


def end_output_file():                                ###просьба ввести путь к файлу
    print('Введите путь к файлу:')


def output_txt():                                   ###старт для текста
    print('Выберите шифрование:')
    print('1. Шифр Цезаря')
    print('2. Шифр Виженера')
    print('3. Шифр Вернама')


def key_output():                                    ###ввод ключа
    print('Введите ключ:')


def end_output():                                    ###конец работы
    print('Ещё что-то?')
    print('1. Шифровать!')
    print('2. Выход')
