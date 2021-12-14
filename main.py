from contact_book import Book

b = Book('new_file')

while True:
    operation = input('Выберите операцию:\na - добавить запись\nd - удалить запись\ns - показать запись\ne - выход\n')
    if operation == 'a':
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        mail = input('Введите почту: ')
        phone = input('Введите телефон: ')
        work = input('Введите место работы: ')
        b.add(name, surname, mail, phone, work)
    elif operation == 'd':
        phone = input('Введите телефон: ')
        b.delete(phone)
    elif operation =='s':
        b.show()
    elif operation =='e':
        b.write_file()
        exit()
    else:
        print('Некорректный ввод')