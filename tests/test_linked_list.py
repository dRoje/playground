from linked_list import LinkedList


def test_linked_list():
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(4)
    linked_list.prepend(0)
    linked_list.prepend(0)

    print(linked_list)
    assert linked_list.to_list() == [0, 0, 1, 2, 2, 3, 4, 4]

    linked_list.delete_value(2)
    assert linked_list.to_list() == [0, 0, 1, 3, 4, 4]

    linked_list.delete_value(0)
    assert linked_list.to_list() == [1, 3, 4, 4]

    linked_list.delete_value(4)
    assert linked_list.to_list() == [1, 3]

    linked_list.delete_value(1)
    assert linked_list.to_list() == [3]

    linked_list.delete_value(3)
    assert not linked_list.to_list()
