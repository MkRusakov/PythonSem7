def show():
    with open ("Contacts.txt", 'r', encoding = 'utf-8') as data:
        info = data.read
        print(info)
