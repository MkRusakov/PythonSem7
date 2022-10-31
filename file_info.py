from create_info import create
contact = create()
def scv():
    file = 'Contacts.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{contact[0]};{contact[1]};{contact[2]};{contact[3]}\n')

def txt():
    file = 'Contacts.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {contact[0]}\n\nИмя: {contact[1]}\n\nНомер телефона: {contact[2]}\n\nОписание: {contact[3]}\n\n\n')