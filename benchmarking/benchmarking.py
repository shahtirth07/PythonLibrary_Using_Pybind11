import pandas as pd
import time
import numpy as np

from cleaning_package import (
    trim_spaces_py, count_nulls_py, to_lowercase_py, replace_char_py, cosine_similarity_py
)

# Sample data
data = ["   hello   ", "  world", " data cleaning ", "   trim  spaces "]
nums = [0, 1, 0, 2, 3, 0, 4, 0]
text_data = ["Hello", "WORLD", "PyThOn", "C++"]
replace_data = "banana"

vec_a = np.array([1.0, 2.0, 3.0] * 10000)
vec_b = np.array([4.0, 5.0, 6.0] * 10000)

# Helper function for benchmarking
def benchmark(func, *args, name=""):
    start = time.time()
    result = func(*args)
    elapsed = time.time() - start
    print(f"{name} time: {elapsed:.6f} seconds")
    return result

# Benchmark trimming spaces with Pandas
def pandas_trim_spaces():
    df = pd.DataFrame(data, columns=['text'])
    return df['text'].str.strip().tolist()

# Benchmark converting to lowercase with Pandas
def pandas_to_lowercase():
    df = pd.DataFrame(text_data, columns=['text'])
    return df['text'].str.lower().tolist()

# Benchmark cosine similarity with Pandas/NumPy
def pandas_cosine_similarity(vector_a, vector_b):
    """
    Compute cosine similarity between two vectors using NumPy.
    """
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0  # Handle edge cases for zero-length vectors
    return dot_product / (norm_a * norm_b)

# Run benchmarks
if __name__ == "__main__":
    print("Benchmarking C++ vs Pandas/Python:")

    # 1. Trim spaces
    print("\nTrimming spaces:")
    benchmark(lambda: pandas_trim_spaces(), name="Pandas trim")
    benchmark(lambda: [trim_spaces_py(x) for x in data], name="C++ trim")

    # 2. Count nulls
    print("\nCounting nulls:")
    benchmark(lambda: (pd.Series(nums) == 0).sum(), name="Pandas count nulls")
    benchmark(lambda: count_nulls_py(nums), name="C++ count nulls")

    # 3. Convert to lowercase
    print("\nConverting to lowercase:")
    benchmark(lambda: pandas_to_lowercase(), name="Pandas to_lowercase")
    benchmark(lambda: [to_lowercase_py(x) for x in text_data], name="C++ to_lowercase")

    # 4. Replace characters
    print("\nReplacing characters:")
    benchmark(lambda: replace_data.replace('a', 'o'), name="Python replace_char")
    benchmark(lambda: replace_char_py(replace_data, 'a', 'o'), name="C++ replace_char")

    # 5. Cosine similarity
    print("\nCosine similarity:")
    benchmark(lambda: pandas_cosine_similarity(vec_a, vec_b), name="Pandas cosine_similarity")
    benchmark(lambda: cosine_similarity_py(vec_a.tolist(), vec_b.tolist()), name="C++ cosine_similarity")
