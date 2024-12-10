import pytest
from cleaning_package import trim_spaces_py, count_nulls_py, to_lowercase_py, replace_char_py, cosine_similarity_py

def test_trim_spaces():
    assert trim_spaces_py("  hello  ") == "hello"
    assert trim_spaces_py(" world") == "world"
    assert trim_spaces_py("") == ""

def test_count_nulls():
    assert count_nulls_py([0, 1, 0, 3, 0]) == 3
    assert count_nulls_py([1, 2, 3, 4]) == 0
    assert count_nulls_py([]) == 0

def test_to_lowercase():
    assert to_lowercase_py("Hello") == "hello"
    assert to_lowercase_py("WORLD") == "world"
    assert to_lowercase_py("123") == "123"

def test_replace_char():
    assert replace_char_py("banana", 'a', 'o') == "bonono"
    assert replace_char_py("hello world", ' ', '-') == "hello-world"
    assert replace_char_py("test", 'x', 'y') == "test"  # No replacement

def test_cosine_similarity():
    vec_a = [1.0, 2.0, 3.0]
    vec_b = [4.0, 5.0, 6.0]
    result = cosine_similarity_py(vec_a, vec_b)
    expected = 0.9746318461970762  # Precomputed value
    assert abs(result - expected) < 1e-6, f"Expected {expected}, got {result}"
