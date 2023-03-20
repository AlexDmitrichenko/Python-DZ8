def menu():
    while True:
        userChoice = input('''Главное меню\n1. Найти контакт\n2. Добавить контакт\n3. Изменить контакт
4. Удалить контакт\n5. Показать все контакты\n6. Выйти\nВыберите пункт меню: ''')
        print()
        if userChoice == '1':
            contactList = readFileToDict(phonebook)
            findNumber(contactList)
        elif userChoice == '2':
            addPhoneNumber(phonebook)
        elif userChoice == '3':
            changePhoneNumber(phonebook)
        elif userChoice == '4':
            deleteContact(phonebook)
        elif userChoice == '5':
            showPhonebook(phonebook)
        elif userChoice == '6':
            print('До свидания!')
            break
        else:
            print('Выбрана неверная команда!')
            print()
            continue


menu()
