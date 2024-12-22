from collections import defaultdict
import csv
import re

def normalize_phone(phone):
    if not phone:
        return ""
    # Приведение телефона к формату +7(XXX)XXX-XX-XX доб.XXXX
    pattern = re.compile(r"(\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*доб\.\s*(\d+))?")
    return pattern.sub(r"+7(\2)\3-\4-\5 доб.\7", phone).strip(" доб.")


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# 1. Приведение ФИО к правильному формату
normalized_contacts = []
for contact in contacts_list[1:]:  # Пропускаем заголовок
    # Объединяем и разделяем ФИО на составляющие
    full_name = " ".join(contact[:3]).split()
    lastname = full_name[0] if len(full_name) > 0 else ""
    firstname = full_name[1] if len(full_name) > 1 else ""
    surname = full_name[2] if len(full_name) > 2 else ""
    # Нормализуем телефон
    phone = normalize_phone(contact[5])
    # Собираем контакт обратно
    normalized_contacts.append([
        lastname, firstname, surname, contact[3], contact[4], phone, contact[6]
    ])

# Объединение дублирующихся записей
merged_contacts = defaultdict(lambda: ["", "", "", "", "", "", ""])
for contact in normalized_contacts:
    # Ключ: Фамилия и Имя (без учета отчества)
    key = (contact[0], contact[1])
    for i in range(len(contact)):
        if contact[i] and not merged_contacts[key][i]:  # Добавляем данные только если поле пустое
            merged_contacts[key][i] = contact[i]

# Преобразование в итоговый список
final_contacts = []
for key, values in merged_contacts.items():
    # Добавляем фамилию, имя и оставшиеся поля
    final_contacts.append([key[0], key[1], values[2], values[3], values[4], values[5], values[6]])
final_contacts.insert(0, contacts_list[0])  # Добавляем заголовок обратно

# Сохраняем данные в новый CSV файл
with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=",")
    datawriter.writerows(final_contacts)


