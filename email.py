from datetime import datetime
from pprint import pprint
import re


# 1. Создайте словарь email, содержащий следующие поля:
# "subject" (тема письма), "from" (адрес отправителя), "to" (адрес получателя), "body" (текст письма).

email= {}

email['subject'] = 'Quarterly Report'
email['from'] = 'Alice.Cooper@Company'
email['to'] = 'bob_smith@Gmail.com'
email['body'] = 'Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice'

# pprint(email)


# 2. Добавьте дату отправки: создайте переменную send_date как текущую дату в формате YYYY-MM-DD и запишите её в email["date"].

send_date = datetime.now().strftime('%Y-%m-%d')
email['date'] = send_date

# pprint(email)


# 3. Нормализуйте e-mail адреса отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
# Запишите обратно в email["from"] и email["to"].

email1 = {
    'subject': 'Quarterly Report',
    'from': 'Alice.Cooper@Company. ',
    'to': ' bob_smith@Gmail.com ',
    'body': 'Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice'
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

emails = [email1, email2, email3, email4, email5]

for item in emails:
    item['from'] = item['from'].strip().lower()  
    item['to'] = item['to'].strip().lower()

# print(emails)


# 4. Извлеките логин и домен отправителя в две переменные login и domain.

login = email['from'].split('@')[0]
# print('login: ', login)
domain = email['from'].split('@')[1]
# print('domain: ', domain)


# 5. Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
# Сохраните в новый ключ словаря: email["short_body"].

# использовал модуль re для регулярных выражений
email["short_body"] = re.sub(r"\s+", " ", email["body"])
# print('email["short_body"]: ', email["short_body"])


# 6. Списки доменов: создайте список личных доменов и список корпоративных доменов

person_domains = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
# print('person_domains: ', person_domains)
# print('person_domains: ', len(person_domains))
company_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
# print('company_domains: ', company_domains)
# print('company_domains: ', len(company_domains))
# print('-----------------')
person_domains = set(person_domains)
# print('person_domains: ', person_domains)
# print('person_domains: ', len(person_domains))
company_domains = set(company_domains)
# print('company_domains: ', company_domains)
# print('company_domains: ', len(company_domains))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений:
# ни один домен не должен входить в оба списка одновременно.

duplicates = company_domains & person_domains

# print(f"Есть пересечение: {duplicates}" if duplicates else "Пересечения нет")
