from cleaning_package import trim_spaces_py, count_nulls_py

def test_trim_spaces():
    assert trim_spaces_py("   hello   ") == "hello"

def test_count_nulls():
    assert count_nulls_py([0, 1, 0, 3, 4, 0]) == 3
