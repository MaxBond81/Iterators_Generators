
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.cursor = -1
        return self


    def __next__(self):
        flat_list = []
        for item_list in self.list_of_list:
            if isinstance(item_list, list):
                flat_list.extend(flatten(item_list))
            else:
                flat_list.append(item_list)
        self.cursor += 1
        if self.cursor == len(flat_list):
            raise StopIteration
        return flat_list[self.cursor]

def flatten(list_lists):
    if list_lists == []:
        return list_lists
    if isinstance(list_lists[0], list):
        return (flatten(list_lists[0]) + flatten(list_lists[1:]))
    return (list_lists[:1] + flatten(list_lists[1:]))



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