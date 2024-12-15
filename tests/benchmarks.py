import numpy as np
import pandas as pd
import time
import data_cleaning
import ctypes

def benchmark_trim_spaces():
    # Generate a large dataset of strings with leading/trailing spaces
    test_strings = [f"   String {i} with spaces   " for i in range(100000)]
    buffer = bytearray("".join(test_strings), 'utf-8')

    # Benchmark C++ function
    start_cpp = time.time()
    cpp_trimmed = data_cleaning.trim_spaces(buffer)
    end_cpp = time.time()

    # Benchmark Python equivalent using Pandas
    start_pd = time.time()
    trimmed = pd.Series(test_strings).str.strip()
    end_pd = time.time()

    print(f"Trim Spaces (C++): Time: {end_cpp - start_cpp:.6f} seconds")
    print(f"Trim Spaces (Pandas): Time: {end_pd - start_pd:.6f} seconds")

def benchmark_count_nulls():
    # Generate a large array with random zeros and ones
    test_array = np.random.randint(0, 2, size=10000000, dtype=np.int32)

    # Benchmark C++ function
    start_cpp = time.time()
    result_cpp = data_cleaning.count_nulls(test_array)
    end_cpp = time.time()

    # Benchmark Python equivalent using NumPy
    start_np = time.time()
    result_np = np.sum(test_array == 0)
    end_np = time.time()

    print(f"Count Nulls (C++): {result_cpp} | Time: {end_cpp - start_cpp:.6f} seconds")
    print(f"Count Nulls (NumPy): {result_np} | Time: {end_np - start_np:.6f} seconds")

def benchmark_cosine_similarity():
    # Generate large random vectors
    vector_a = np.random.random(1000000).astype(np.float64)
    vector_b = np.random.random(1000000).astype(np.float64)

    # Benchmark C++ function
    start_cpp = time.time()
    result_cpp = data_cleaning.cosine_similarity(vector_a, vector_b)
    end_cpp = time.time()

    # Benchmark Python equivalent using NumPy
    start_np = time.time()
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    result_np = dot_product / (norm_a * norm_b) if norm_a > 0 and norm_b > 0 else 0
    end_np = time.time()

    print(f"Cosine Similarity (C++): {result_cpp:.6f} | Time: {end_cpp - start_cpp:.6f} seconds")
    print(f"Cosine Similarity (NumPy): {result_np:.6f} | Time: {end_np - start_np:.6f} seconds")

def benchmark_to_lowercase():
    # Generate a large dataset of strings
    test_strings = ["THIS IS A TEST STRING FOR LOWERCASE BENCHMARKING!"] * 1000000
    buffer = bytearray("".join(test_strings), 'utf-8')

    # Benchmark C++ function
    start_cpp = time.time()
    cpp_lc = data_cleaning.to_lowercase(buffer)
    end_cpp = time.time()

    # Benchmark Python equivalent using str.lower()
    start_py = time.time()
    result_py = [s.lower() for s in test_strings]
    end_py = time.time()

    print(f"Lowercase (C++): Time: {end_cpp - start_cpp:.6f} seconds")
    print(f"Lowercase (Python): Time: {end_py - start_py:.6f} seconds")

if __name__ == "__main__":
    print("Testing and Benchmarking Data Cleaning Functions on Large Datasets:")
    print("\n--- Trim Spaces ---")
    benchmark_trim_spaces()
    print("\n--- Count Nulls ---")
    benchmark_count_nulls()
    print("\n--- Cosine Similarity ---")
    benchmark_cosine_similarity()
    print("\n--- To Lowercase ---")
    benchmark_to_lowercase()
