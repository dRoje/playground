from hash_table import HashTable


def test_hash_table():
    table = HashTable(size=5)
    table.update(key="Tim", value=10)
    table.update(key="Jim", value=9)
    table.update(key="Mia", value=21)

    print(table)

    assert table.get("Jim") == 9
    assert table.get("Mia") == 21
    assert table.get("Tim") == 10

    table.update(key="Jim", value=21)

    assert table.get("Jim") == 21

    table.delete("Jim")
    assert not table.get("Jim")

    table.delete("Tim")
    table.delete("Mia")
