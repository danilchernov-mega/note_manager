username = "Данил"
title = "Grade 1"
content = "Сделать домашнее задание"
status = "статус заметки"
created_date = "09-01-2025"
issue_date = "09-02-2025"

temp_created_date = created_date[:-5:]
temp_issue_date = issue_date[:-5:]

print('Вы ввели следующие данные: ')
print('Имя пользователя: ', username)
print('Название заметки: ', title)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания: ', temp_created_date)
print('Дата истечения: ', temp_issue_date)
