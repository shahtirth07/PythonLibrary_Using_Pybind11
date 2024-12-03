import ctypes
import os

# Load the shared library
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../libcleaning.so'))
cleaning = ctypes.CDLL(lib_path)

# Define function prototypes
cleaning.trim_spaces.argtypes = [ctypes.c_char_p]
cleaning.trim_spaces.restype = None

cleaning.count_nulls.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
cleaning.count_nulls.restype = ctypes.c_int

def trim_spaces_py(string: str) -> str:
    buffer = ctypes.create_string_buffer(string.encode('utf-8'))
    cleaning.trim_spaces(buffer)
    return buffer.value.decode('utf-8')

def count_nulls_py(arr):
    arr_type = ctypes.c_int * len(arr)
    return cleaning.count_nulls(arr_type(*arr), len(arr))
