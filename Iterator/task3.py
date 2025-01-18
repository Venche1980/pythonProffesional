class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = []  # стек для хранения позиций и списков
        self.current = []  # текущий обрабатываемый список

    def __iter__(self):
        self.stack = [(self.list_of_list, 0)]
        return self

    def __next__(self):
        while self.stack:
            current_list, current_pos = self.stack[-1]

            if current_pos >= len(current_list):
                self.stack.pop()
                continue

            item = current_list[current_pos]

            self.stack[-1] = (current_list, current_pos + 1)

            if isinstance(item, list):
                if item:
                    self.stack.append((item, 0))
                continue

            return item

        raise StopIteration

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()