from tkinter import filedialog
from other import unhandled_exception_handler, change_warning
import sys

# Register the function as the handler for unhandled exceptions
sys.excepthook = unhandled_exception_handler

# Чтение базы данных

DATABASE = {}
with open("Data.txt", "r", encoding='windows-1251', errors='ignore') as f:
    for line in f:
        try:
            key, value = line.split("]--------------->[")
            DATABASE["[" + (key.lstrip("["))] = value.rstrip("]\n") + "]"

            # Если в строчке 2 и более пары ключ-значение,
            # возникает исключение для корректного их разделения

        except ValueError:
            temp_line = line.split("][")
            for block in temp_line:
                key, value = block.split("]--------------->[")
                DATABASE["[" + (key.lstrip("["))] = value.rstrip("]\n") + "]"


# Выбор действий: 1) Форматирование текста 2) Изменение базы 3) Выход из программы

working = True
while working:
    while True:
        try:
            choice = int(input("1) Отформатировать текст\n"
                               "2) Скорректировать базу замен\n"
                               "3) Выйти из программы\n"))
            if choice not in [1, 2, 3]:
                raise ValueError()
            break
        except ValueError:
            print("Ожидается \"1\", \"2\" или \"3\"")

    # 1) Форматирование текста

    if choice == 1:

        filepath = filedialog.askopenfilename()
        with open(filepath, "r", encoding='windows-1251') as file:
            variable = file.read()
            previous_variable = variable
            DATABASE = sorted(DATABASE.items(), key=lambda x: len(x[0]), reverse=True)
            DATABASE = dict(DATABASE)

            # Бегает по тексту пока не убедиться, что больше нечего менять

            while True:
                for k, v in DATABASE.items():
                    variable = variable.replace(k.lstrip("["), v.rstrip("]\n"))
                if previous_variable == variable:
                    break
                else:
                    previous_variable = variable

        with open(filepath, "w", encoding='windows-1251') as file:
            file.writelines(variable)
        print("Готово")

    # 2) Изменение базы

    elif choice == 2:
        while True:
            try:
                choice = int(input("1) Добавить замену\n"
                                   "2) Убрать замену\n"
                                   "3) Посмотреть список замен\n"
                                   "4) Удалить все замены из БД\n"
                                   "5) Вернуться на уровень выше\n"
                                   "6) Завершить работу программы\n"))
                if choice not in [1, 2, 3, 4, 5, 6]:
                    raise ValueError()
                else:

                    if choice == 1:
                        print(change_warning)
                        temp_key = input("Введите, что будет заменяться: ")
                        temp_value = input("Введите на что будет заменяться: ")
                        DATABASE.update([("[" + temp_key, temp_value + "]")])
                    elif choice == 2:
                        DATABASE.pop("[" + input("Введите, что больше не будет заменяться: "))
                    elif choice == 3:
                        i = 1
                        for k, v in DATABASE.items():
                            print(f'{i}) {k}] заменяется на [{v}\n')
                            i += 1
                    elif choice == 4:
                        DATABASE.clear()
                        print("База очищена")
                    elif choice == 5:
                        break
                    else:
                        working = False
                        break

            except ValueError:
                print("Ожидается \"1\", \"2\", \"3\", \"4\", \"5\" или \"6\"")

    # 3) Выход из программы

    elif choice == 3:
        break

# Записываем данные в базу данных

with open("Data.txt", "w", encoding='windows-1251') as file:
    for key, value in DATABASE.items():
        file.write(f'{key}]--------------->[{value}\n')

input("Нажмите Enter для закрытия окна\n")
