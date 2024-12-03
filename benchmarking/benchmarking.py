import pandas as pd
import time
from cleaning_package import trim_spaces_py, count_nulls_py

# Sample data for benchmarking
data = ["   hello   ", " world ", "   data cleaning "]
nums = [0, 1, 0, 3, 4, 0, 5, 6, 0]

# Benchmark trimming spaces with Pandas
def benchmark_pandas_trim():
    df = pd.DataFrame(data, columns=['text'])
    start = time.time()
    df['text'] = df['text'].str.strip()
    elapsed = time.time() - start
    print(f"Pandas trim time: {elapsed:.6f} seconds")
    return df['text'].tolist()

# Benchmark trimming spaces with C++ function
def benchmark_cpp_trim():
    start = time.time()
    trimmed = [trim_spaces_py(x) for x in data]
    elapsed = time.time() - start
    print(f"C++ trim time: {elapsed:.6f} seconds")
    return trimmed

# Benchmark counting nulls with Pandas
def benchmark_pandas_count_nulls():
    start = time.time()
    null_count = (pd.Series(nums) == 0).sum()
    elapsed = time.time() - start
    print(f"Pandas count nulls time: {elapsed:.6f} seconds")
    return null_count

# Benchmark counting nulls with C++ function
def benchmark_cpp_count_nulls():
    start = time.time()
    null_count = count_nulls_py(nums)
    elapsed = time.time() - start
    print(f"C++ count nulls time: {elapsed:.6f} seconds")
    return null_count

if __name__ == "__main__":
    print("Benchmarking Pandas vs C++:")
    
    # Benchmark trim_spaces
    pandas_trimmed = benchmark_pandas_trim()
    cpp_trimmed = benchmark_cpp_trim()
    print("Pandas result:", pandas_trimmed)
    print("C++ result:", cpp_trimmed)
    
    # Benchmark count_nulls
    pandas_nulls = benchmark_pandas_count_nulls()
    cpp_nulls = benchmark_cpp_count_nulls()
    print("Pandas null count:", pandas_nulls)
    print("C++ null count:", cpp_nulls)
