# 1 Открыть файл
# 2 Сохранить файл
# 3 Показать все контакты
# 4 Добавить контакт
# 5 Найти контакт
# 6 Изменить контакт
# 7 Удалить контакт
# 8 Выход

#path='phonetable.txt'
#data=open(path,'w')
#for line in data:
#    print(line)
#data.close()

def open_read_file(path):
    with open(path,'r') as file:
        main_list=file.readlines()
        main_list_str=[x.rstrip().split(':') for x in main_list]
    return main_list_str

def open_write_file (path,list_file):
    with open(path,'w') as file:
        file.writelines([':'.join('x')+'\n' for x in list_file])

def show_list(show_list_data):
    print([':'.join('x')+'\n' for x in show_list_data], end='\n')

def find_contact(phone_number):
    print("Введите фамилию: ")
    surname=input('')
    print("Введите имя: ")
    name=input('')
    print(x[2].split(':') for x in phone_number if x[0]== surname and x[1]==name)

