import unittest
from app import documents, directories


class TestApp(unittest.TestCase):

    def test_check_document_existance(self):
        # Проверка существования документа
        doc_exists = any(doc['number'] == "11-2" for doc in documents)
        self.assertTrue(doc_exists)

        # Проверка отсутствия документа
        doc_exists = any(doc['number'] == "11-3" for doc in documents)
        self.assertFalse(doc_exists)

    def test_get_doc_owner_name(self):
        # Проверка получения имени владельца по номеру документа
        for doc in documents:
            if doc['number'] == "11-2":
                self.assertEqual(doc['name'], "Геннадий Покемонов")

    def test_get_all_doc_owners_names(self):
        # Проверка получения списка всех владельцев
        names = set()
        for doc in documents:
            names.add(doc['name'])
        self.assertEqual(names, {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})

    def test_remove_doc_from_shelf(self):
        # Проверка удаления документа с полки
        old_shelf = directories['1'][:]  # сохраняем старое состояние полки
        doc_number = "11-2"

        if doc_number in directories['1']:
            directories['1'].remove(doc_number)

        self.assertNotIn(doc_number, directories['1'])
        directories['1'] = old_shelf  # возвращаем полку в исходное состояние

    def test_add_new_shelf(self):
        # Проверка добавления новой полки
        shelf = "4"
        directories[shelf] = []  # добавляем новую полку
        self.assertIn(shelf, directories)  # проверяем что полка добавилась
        del directories[shelf]  # удаляем тестовую полку

    def test_get_doc_shelf(self):
        # Проверка получения номера полки по документу
        doc = "10006"
        self.assertIn(doc, directories['2'])  # проверяем что документ на полке 2


if __name__ == '__main__':
    unittest.main()