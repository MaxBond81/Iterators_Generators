import types

def flat_generator(list_of_list):
    flat_list = []
    for item_list in list_of_list:
        if isinstance(item_list, list):
            flat_list.extend(flatten(item_list))
        else:
            flat_list.append(item_list)
    for item in flat_list:
        yield item

def flatten(list_lists):
    if list_lists == []:
        return list_lists
    if isinstance(list_lists[0], list):
        return (flatten(list_lists[0]) + flatten(list_lists[1:]))
    return (list_lists[:1] + flatten(list_lists[1:]))

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
