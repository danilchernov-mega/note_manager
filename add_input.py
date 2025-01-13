firs_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
# username = firs_name + last_name
title = input("Введите заголовок вашей заметки: ")
content = input('Придумайте описание вашей заметки: ')
status = input('Введите статус заметки (Например: "Выполняется" или Выполнена"): ')
created_date = input('Введите дату создания в формате "дд-мм-гггг": ')
issue_date = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')

temp_created_date = created_date[:-5:]
temp_issue_date = issue_date[:-5:]

print('Добрый день: ', firs_name, last_name)
print('Название заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания: ', temp_created_date)
print('Дата истечения: ', temp_issue_date)
