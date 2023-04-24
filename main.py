from tkinter import filedialog

DATABASE = {}
with open("Data.txt", "r", encoding='UTF-8', errors='ignore') as f:
    for line in f:
        key, value = line.split("|--------------->|")
        DATABASE[key] = value
        print(line, end="")


# Выбор действий

while True:
    try:
        choice = int(input("1) Хочу отформатировать текст\n2) Хочу скорректировать базу для замен\n"))
        if choice not in [1, 2]:
            raise ValueError()
        break
    except ValueError:
        print("Ожидается \"1\" или \"2\"")

# 1) Форматирование текста

if choice == 1:

    filepath = filedialog.askopenfilename()
    with open(filepath, "r", encoding='UTF-8') as file:
        variable = file.read()
        for k, v in DATABASE.items():
            variable = variable.replace(k, str(v).rstrip("\n"))
    with open(filepath, "w", encoding='UTF-8') as file:
        file.writelines(variable)
    print("Готово")


# 2) Изменение базы

if choice == 2:
    while True:
        try:
            choice = int(input("1) Хочу добавить замену\n2) Хочу убрать замену\n3) Хочу посмотреть список замен\n4) Хочу удалить все замены из БД\n5) Выйти\n"))
            if choice not in [1, 2, 3, 4, 5]:
                raise ValueError()
            else:

                if choice == 1:
                    temp_key = input("Введите, что будет заменяться: ")
                    temp_value = input("Введите на что будет заменяться: ")
                    DATABASE.update([(temp_key, temp_value + "\n")])
                elif choice == 2:
                    DATABASE.pop(input("Введите, что больше не будет заменяться: "))
                elif choice == 3:
                    for k, v in DATABASE.items():
                        print(f'"{k}" заменяется на "{v}"\n')
                elif choice == 4:
                    DATABASE.clear()
                    print("База очищена")
                else:
                    break
        except ValueError:
            print("Ожидается \"1\", \"2\", \"3\", \"4\" или \"5\"")


with open("Data.txt", "w", encoding='UTF-8') as file:
    for key, value in DATABASE.items():
        file.write(f'{key}|--------------->|{value}')

input()
