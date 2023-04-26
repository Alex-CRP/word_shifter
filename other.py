import traceback


### FUNCTIONS

# Define the function to handle unhandled exceptions
def unhandled_exception_handler(exc_type, exc_value, exc_traceback):
    # Open the text file in which we want to store the error message
    with open("error.txt", "a") as file:
        # Write the error message to the file
        file.write(f"\nAn unhandled {exc_type.__name__} occurred: {exc_value}\n")
        # Write the traceback information to the file
        traceback_info = "".join(traceback.format_tb(exc_traceback))
        file.write(f"Traceback:\n{traceback_info}")
        print(f"Возникла ошибка {exc_type.__name__}. Программа завершена. ")
        input("Нажмите Enter для закрытия окна\n")


### MESSAGES

change_warning = """
Обратите внимание, что программа заменяет именно последовательность символов, 
а не отдельные слова. Поэтому, если вы укажете заменять, например, последовательность "Вы", помните, 
что программа будет заменять эту череду символов вне зависимости от ее положения в тексте. Например, 
замена сработает в следующем предложении: \"Выдра вылезла наружу\"
"""
