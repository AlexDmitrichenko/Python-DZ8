# phonebook = []
# path = 'phone.txt'

# def menu():
#     while True:
#         userChoice = input('''Главное меню\n1. Открыть файл\n2. Сохранить файл\n3. Добавить контакт
# 4. Показать все контакты\n5. Изменить контакт\n6. Выйти\nВыберите пункт меню: ''')
#         print()
#         if userChoice == '1':
#             openFile()
#         # elif userChoice == '2':
#         #     addPhoneNumber(phonebook)
#         # elif userChoice == '3':
#         #     changePhoneNumber(phonebook)
#         elif userChoice == '4':
#             showPhonebook()
#         # elif userChoice == '5':
#         #     showPhonebook(phonebook)
#         # elif userChoice == '6':
#         #     print('До свидания!')
#         #     break
#         else:
#             print('Выбрана неверная команда!')
#             print()
#             continue

# def openFile():
#     with open(path, 'r', encoding="UTF-8") as file:
#         data = file.readline()
#     for row in data:
#         contact = row.strip().strip(';')
#     #     contact = {'name': contact[0], 'phone': contact[1],'comment': contact[2]}
#         phonebook.append(contact)

# def showPhonebook(phonebook: list):
#     if not phonebook:
#         print('Телефонный справочник пуст')
#         return False
#     for index, contact in enumerate(phonebook, 1):
#         print(f"{index}. {contact.get('name')}:<20" 
#             f"{contact.get('phone')}:<20"
#             f"{contact.get('comment')}:<20")
# menu()

phonebook = 'file.txt'

def phonebookRead():
    with open(phonebook, encoding='UTF-8') as file:
        print(file.read())

def contactAdd():
    inFio = input('Введите Фамилию и Имя через пробел: ')
    inPh = input('Введите телефон и комментарий через пробел: ')
    with open(phonebook, 'a', encoding='UTF-8') as file:
        file.write(f'{inFio} | {inPh}\n')

def contactSearch():
    with open(phonebook, encoding='UTF-8') as file:
        search = input('Введите ФИ или телефон для поиска ')
        fileSearch = file.read().split('\n')
        searchedContactsIndex = list()
        flag = True
        for i in fileSearch:
            if search.lower() in i.lower():
                searchedContactsIndex.append(fileSearch.index(i))
                print(f'{fileSearch.index(i+1)} {i}')
                flag = False
        if flag:
            print('Контакт не найден!')
        return searchedContactsIndex
    
def findСontact():
    searchedContacts = contactSearch()
    changedIndex = searchedContacts[0]
    if len(searchedContacts) != 1:
        print("Укажите номер контакта из списка выше, для продолждения работы")
        changedIndex = int(input())
    return changedIndex

def changeContact():
    changedIndex = findСontact()
    with open(phonebook, 'r', encoding='UTF-8') as file:
        fileSearch = file.read().split('\n')
        contactAsList = fileSearch[changedIndex].split()
    while True:
        print('Введите 0 для замены фамилии, 1 - имени, 2 - телефона, 4- комментария,\n'
              '5 - всё ок, сохранить')
        mode = int(input())
        if mode == 0:
            contactAsList[mode] = input('Фамилия: ')
        elif mode == 1:
            contactAsList[mode] = input('Имя: ')
        elif mode == 2:
            contactAsList[mode] = input('Телефон: ')
        elif mode == 4:
            contactAsList[mode] = input('Комментарий: ')
        # elif mode == 5:
            break
    fileSearch[changedIndex] = ''
    for i in contactAsList:
        fileSearch[changedIndex] += f'{i} '
    rewritePhonebook(fileSearch)

def deleteContact():
    changedIndex = findСontact()
    with open(phonebook, 'r', encoding='UTF-8') as file:
        fileSearch = file.read().split('\n')
    fileSearch.pop(changedIndex)
    rewritePhonebook(fileSearch)
    print('Контакт удален')

def rewritePhonebook(contacts: list):
    contactsTxt = ''
    for i in range(len(contacts)-1):
        contactsTxt += f'{contacts[i]}\n'
    with open(phonebook, 'w', encoding='UTF-8') as file:
        file.write(contactsTxt)

def main():
    while True:
        print('Главное меню\n'
              '1 - Добавить контакт в справочник\n'
              '2 - Показать все контакты\n'
              '3 - Найти контакт в справочнике\n'
              '4 - Изменить контакт\n'
              '5 - Удалить контакт\n'
              '6 - Выйти\n'
              'Выберите пункт меню: ')
        mode = input()
        if mode == '1':
            contactAdd()
        elif mode == '2':
            phonebookRead()
        elif mode == '3':
            contactSearch()
        elif mode == '4':
            changeContact()
        elif mode == '5':
            deleteContact()
        elif mode == '6':
            print('До свидания!')
            break

if __name__ == '__main__': 
    main()



