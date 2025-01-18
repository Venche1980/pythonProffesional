class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = 0  # индекс текущего подсписка
        self.current_item = 0  # индекс текущего элемента в подсписке

    def __iter__(self):
        return self
    def __next__(self):

        if self.current_list >= len(self.list_of_list):
            raise StopIteration

        current_sublist = self.list_of_list[self.current_list]

        if self.current_item >= len(current_sublist):
            self.current_list += 1
            self.current_item = 0
            return self.__next__()

        # Получаем текущий элемент
        item = current_sublist[self.current_item]
        self.current_item += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()