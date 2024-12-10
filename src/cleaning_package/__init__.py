import ctypes
import os

# Load the shared library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libcleaning.so'))
cleaning = ctypes.CDLL(lib_path)

# Define prototypes
cleaning.trim_spaces.argtypes = [ctypes.c_char_p]
cleaning.trim_spaces.restype = None

cleaning.count_nulls.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
cleaning.count_nulls.restype = ctypes.c_int

cleaning.to_lowercase.argtypes = [ctypes.c_char_p]
cleaning.to_lowercase.restype = None

cleaning.replace_char.argtypes = [ctypes.c_char_p, ctypes.c_char, ctypes.c_char]
cleaning.replace_char.restype = None

# Python wrappers
def trim_spaces_py(string: str) -> str:
    buffer = ctypes.create_string_buffer(string.encode('utf-8'))
    cleaning.trim_spaces(buffer)
    return buffer.value.decode('utf-8')

def count_nulls_py(arr):
    arr_type = ctypes.c_int * len(arr)
    return cleaning.count_nulls(arr_type(*arr), len(arr))

def to_lowercase_py(string: str) -> str:
    buffer = ctypes.create_string_buffer(string.encode('utf-8'))
    cleaning.to_lowercase(buffer)
    return buffer.value.decode('utf-8')

def replace_char_py(string: str, old: str, new: str) -> str:
    buffer = ctypes.create_string_buffer(string.encode('utf-8'))
    cleaning.replace_char(buffer, old.encode('utf-8'), new.encode('utf-8'))
    return buffer.value.decode('utf-8')

from ctypes import CDLL, POINTER, c_double, c_int

# Load the shared library
lib = CDLL('./my_cleaning_package/cleaning.so')
lib.cosine_similarity.argtypes = [POINTER(c_double), POINTER(c_double), c_int]
lib.cosine_similarity.restype = c_double

def cosine_similarity_py(vector_a, vector_b):
    size = len(vector_a)
    if size != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    vec_a = (c_double * size)(*vector_a)
    vec_b = (c_double * size)(*vector_b)
    return lib.cosine_similarity(vec_a, vec_b, size)
