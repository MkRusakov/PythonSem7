def create():
    contact = []
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    number = input("Введите номер телефона: ")
    info = input("Введите описание: ")
    contact.append(surname)
    contact.append(name)
    contact.append(number)
    contact.append(info)
    return contact

