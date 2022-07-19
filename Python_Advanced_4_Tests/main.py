documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:
directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def get_user_name(doc: list) -> str:
    """
    принимает список документов, запрашивает номер документа и возвращает имя(value) из
    конкретного документа(словаря)
    :param doc:
    :return: value
    """
    doc_num = input('Введите номер документа: ')
    user_name = "Нет такой записи"
    for acc in doc:
        if doc_num in acc.values():
            user_name = acc["name"]
    print(user_name)
    return user_name


def get_dir(directory: dict) -> str:
    """
    принимает словарь с полками(key) и списками документов(values), запрашивает номер док-та
    и возвращает номер полки с этим документом
    :param directory:
    :return: key
    """
    doc_num = input('Введите номер документа: ')
    dir_name = "Нет такой записи"
    for dir_number, doc_numbers in directory.items():
        for number in doc_numbers:
            if number == doc_num:
                dir_name = dir_number
    print(f'Документ находится на полке {dir_name}')
    return dir_name


def get_users(doc: list) -> list:
    """
    принимает список всех документов и возвращает отформатированный список всех пользователей в базе в формате
    passport "2207 876234" "Василий Гупкин"
    :param doc:
    :return: list
    """
    users = []
    for acc in doc:
        formatted = f'{acc["type"]} "{acc["number"]}" "{acc["name"]}"'
        users.append(formatted)
    print(users)
    return users


def check_doc_in_db(doc: list, doc_number: str) -> bool:
    """
    принимает список с документами и переменную с номером документа, проверяет наличие нужного документа
    в списке доументов и возвращает тру или фолс
    :param doc:
    :param doc_number:
    :return: bool
    """
    doc_bool = False
    for acc in doc:
        if doc_number == acc['number']:
            doc_bool = True
    return doc_bool


def add_new_user(doc: list, directory: dict) -> tuple[list, dict]:
    """
    принимает список документов и полок, запрашивает пользовательский ввод и проверяет его валидность,
    если ввод прошел проверки, данные заносятся в список документов и полок, функция возвращает обновленные
    список документов и полки
    :param doc:
    :param directory:
    :return: list, dict
    """
    doc_type = input("Введите тип документа: ")
    while True:
        doc_number = input('Введите номер документа: ')
        doc_bool = check_doc_in_db(doc, doc_number)
        if not doc_bool:
            print('Номер успешно зарегистрирован')
        else:
            print('Данный номер уже в базе')
            break
        user_name = input("Введите ваше имя: ")
        while True:
            try:
                dir_name = input("Введите номер полки: ")
                if dir_name in directory.keys():
                    break
                print(f"Нет такой полки, есть такие: {tuple(directory.keys())}")
            except Exception as e:
                print(e)
        for shelf, numbers in directory.items():
            if shelf == dir_name:
                numbers.append(doc_number)
        new_acc = {"type": doc_type, "number": doc_number, "name": user_name}
        doc.append(new_acc)
        return doc, directory


def delete_acc(doc: list, directory: dict) -> tuple[list, dict]:
    doc_number_to_delete = input('Введите номер документа: ')
    if check_doc_in_db(doc, doc_number_to_delete):
        for acc in doc:
            if doc_number_to_delete == acc['number']:
                doc.remove(acc)
        for numbers in directory.values():
            if doc_number_to_delete in numbers:
                numbers.remove(doc_number_to_delete)
        print("Записи удалены")
    else:
        print('Данный документ отсутствует в базе')
    return doc, directory


def move_acc_to_new_dir(doc: list, directory: dict) -> dict:
    doc_number_to_move = input('Введите номер документа: ')
    if check_doc_in_db(doc, doc_number_to_move):
        while True:
            try:
                dir_name = input("Введите номер целевой полки: ")
                if dir_name in directory.keys():
                    break
                print(f"Нет такой полки, есть такие: {tuple(directory.keys())}")
            except Exception as e:
                print(e)
        for numbers in directory.values():
            if doc_number_to_move in numbers:
                numbers.remove(doc_number_to_move)
                directory[dir_name].append(doc_number_to_move)
    else:
        print('Данный документ отсутствует в базе')
    return directory


def add_shelf(directory: dict) -> dict:
    while True:
        try:
            dir_name = input("Введите номер новой полки: ")
            if dir_name not in directory.keys():
                directory[dir_name] = []
                print(directory)
                break
            print(f"Такие полки уже есть: {tuple(directory.keys())}")
        except Exception as e:
            print(e)
    return directory


def main(doc: list, directory: dict):
    print('Приложение "СЕКРЕТАРЬ"')
    print('p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
    print('l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий '
          'Гупкин"')
    print('s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
    print('a - (add)- команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, '
          'тип имя владельца и номер полки')
    print('d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;')
    print('m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на '
          'целевую')
    print('as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень')
    print('q - (quit) - команда, которая завершает выполнение программы')
    while True:
        user_input = input('Введите команду(p, s, l, a, d, m, as, q): ')
        if user_input == 'p':
            get_user_name(doc)
        elif user_input == 's':
            get_dir(directory)
        elif user_input == 'l':
            get_users(doc)
        elif user_input == 'a':
            add_new_user(doc, directory)
        elif user_input == 'd':
            delete_acc(doc, directory)
        elif user_input == 'm':
            move_acc_to_new_dir(doc, directory)
        elif user_input == 'as':
            add_shelf(directory)
        elif user_input == 'q':
            print('Выход из программы')
            break


if __name__ == '__main__':
    main(documents, directories)
