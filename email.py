from datetime import datetime
import math
from pprint import pprint
import re


email1 = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

email2 = {
    'subject': ' Weekd plans ',
    'from': 'katya_yan@yandex. ',
    'to': 'frid@mail. ',
    'body': "\tHey!\nLet's go hiking this weekd.\nBring snacks!\n'"
}

email3 = {
    'subject': 'Reminder: Meeting',
    'from': 'ceo@corporation.com ',
    'to': ' team_lead@outlook.com ',
    'body': ' '
}

email4 = {
    'subject': ' ',
    'from': ' alex@business.net ',
    'to': ' hr@company. ',
    'body': 'Hi HR,\nPlease find attached my updated CV.\nThanks!'
}

email5 = {
    'subject': 'Project collaboration',
    'from': ' partner@organization.org ',
    'to': 'lead_dev@icloud.com ',
    'body': 'Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam'
}

# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

# pprint(email1)


# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_date = datetime.now().strftime('%Y-%m-%d')
email1['date'] = send_date

# pprint(email1, width=120)


# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

emails = [email1, email2, email3, email4, email5]

for item in emails:
    item['from'] = item['from'].strip().lower()  
    item['to'] = item['to'].strip().lower()

# print(emails)


# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email1['from'].split('@')[0]
# print('login: ', login)
domain = email1['from'].split('@')[1]
# print('domain: ', domain)


# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

# использовал модуль re для регулярных выражений
email1["short_body"] = email1["body"].replace('\t', ' ').replace('\n', ' ').replace('  ', ' ')[0:10] + '...'
# print('email1["short_body"]: ', email1["short_body"])


# 6. Списки доменов: создайте список личных доменов и список корпоративных доменов

personal_domains = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# print('person_domains: ', person_domains)
# print('person_domains: ', len(person_domains))
company_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
# print('company_domains: ', company_domains)
# print('company_domains: ', len(company_domains))
# print('-----------------')
personal_domains = set(person_domains)
# print('person_domains: ', person_domains)
# print('person_domains: ', len(person_domains))
company_domains = set(company_domains)
# print('company_domains: ', company_domains)
# print('company_domains: ', len(company_domains))


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.

duplicates = company_domains & person_domains

# print(f"Есть пересечение: {duplicates}" if duplicates else "Пересечения нет")


# 8.  Проверьте «корпоративность» отправителя: создайте булеву переменную is_corporate, равную результату проверки вхождения домена отправителя в список корпоративных доменов.

is_corporate = email1['from'].split('@')[1] in company_domains
# print(is_corporate)


# 9. Соберите «чистый» текст сообщения без табов и переводов строк: замените "\t" и "\n" на пробел.
# Сохраните в email["clean_body"].

# использовал модуль re для регулярных выражений
email1["clean_body"] = re.sub(r"\s+", " ", email1["body"])
# print('email["clean_body"]: ', email1["clean_body"])


# 10. Сформируйте текст отправленного письма многострочной f-строкой и сохраните в email["sent_text"]:
# Кому: {получатель}, от {отправитель} Тема: {тема письма}, дата {дата} {чистый текст сообщения}

email1["sent_text"] = f"Кому: {email1['to']}, от {email1['from']} Тема: {email1['subject']}, дата {email1['date']} {email1['clean_body']}"


# 11. Рассчитайте количество страниц печати для email["sent_text"], если на 1 страницу помещается 500 символов.
# Сохраните результат в переменную pages. Значение должно быть округленно в большую сторону.

pages = math.ceil(len(email1["sent_text"])//500)
# print('len(email1["sent_text"]): ', len(email1["sent_text"]))
# print('pages: ', pages)


# 12. Проверьте пустоту темы и тела письма: создайте переменные is_subject_empty, is_body_empty в котором будет хранится что тема письма содержит данные.

is_subject_empty = bool(email1['subject'])
# print('is_subject_empty: ', is_subject_empty)

is_body_empty = bool(email1['body'])
# print('is_body_empty: ', is_body_empty)
    

# 13. Создайте «маску» e-mail отправителя: первые 2 символа логина + "***@" + домен.
# Запишите в email["masked_from"].

email1['masked_from'] = login[0:2] + '***@' + domain
# print("email1['masked_from']: ", email1['masked_from'])


# 14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".

domains_to_remove = {'list.ru', 'bk.ru'}

for domain in domains_to_remove:
    if domain in personal_domains:
        personal_domains.remove(domain)


# pprint(email1, width=300)
