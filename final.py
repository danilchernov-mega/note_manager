firs_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
title1 = input("Введите заголовок №1 вашей заметки: ")
title2 = input("Введите заголовок №2 вашей заметки: ")
title3 = input("Введите заголовок №3 вашей заметки: ")
content = input('Придумайте описание вашей заметки: ')
status = input('Введите статус заметки (Например: "Выполняется" или Выполнена"): ')
created_date = input('Введите дату создания в формате "дд-мм-гггг": ')
issue_date = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')

temp_created_date = created_date[:-5:]
temp_issue_date = issue_date[:-5:]

note = [
    [firs_name, last_name], content, status, created_date, issue_date, [title1, title2, title3]
]

print("Ваши даанные: ", note)
