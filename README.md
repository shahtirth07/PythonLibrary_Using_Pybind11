<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

<h1>🌟 MATH608_PROJECT: High-Performance Data Cleaning 🌟</h1>

<hr>

<div class="section">
  <h2>🚀 About the Project</h2>
  <p>
    <strong>MATH608_PROJECT</strong> is a Python package that leverages the speed of <strong>C++</strong> to accelerate common data-cleaning tasks. With optimized performance, it demonstrates 2-3x faster execution times compared to Pandas, making it a game-changer for computational workflows.
  </p>
</div>

<hr>

<div class="section">
  <h2>⚙️ Features</h2>
  <ul>
    <li>Trim spaces, count nulls, convert to lowercase, replace characters, and compute cosine similarity.</li>
    <li>Seamless integration with Python workflows via <code>pybind11</code>.</li>
    <li>Includes a benchmarking script to showcase performance gains.</li>
  </ul>
</div>

<hr>

<div class="section">
  <h2>📂 Directory Structure</h2>
  <pre>
MATH608_PROJECT/
├── src/
│   ├── my_cleaning_package/
│   │   ├── bindings.cpp
│   │   └── data_cleaning.cpp       # C++ code for data cleaning
│   └── setup.py               # Package setup script
├── tests/
│   └── benchmark.py           # Benchmarking script
└── README.md                  # Project documentation
  </pre>
</div>

<hr>

<div class="section">
  <h2>📦 Installation</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/shahtirth07/MATH608_PROJECT.git
cd MATH608_PROJECT</code></pre>
    </li>
    <li>Build the package:
      <pre><code>cd src
python setup.py build_ext --inplace
python setup.py install</code></pre>
    </li>
    <li>Verify installation:
      <pre><code>from my_cleaning_package import trim_spaces_py
print(trim_spaces_py("   hello world   "))  # Outputs: "hello world"</code></pre>
    </li>
  </ol>
</div>

<hr>

<div class="section">
  <h2>🧪 Usage Examples</h2>
  <h3>Example: Clean a dataset</h3>
  <pre><code>from my_cleaning_package import trim_spaces_py, to_lowercase_py

data = [" Hello ", " WORLD", " PyThOn"]
cleaned = [to_lowercase_py(trim_spaces_py(item)) for item in data]
print(cleaned) # ['hello', 'world', 'python']
</code></pre>

</div>

<hr>

<div class="section">
  <h2>📊 Benchmark Results</h2>
  <table>
    <thead>
      <tr>
        <th>Operation</th>
        <th>Pandas Time (s)</th>
        <th>C++ Time (s)</th>
        <th>Speedup</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Trim Spaces</td>
        <td>0.036936</td>
        <td>0.009662</td>
        <td>2.5x</td>
      </tr>
      <tr>
        <td>Count Nulls</td>
        <td>0.016915</td>
        <td>0.085768</td>
        <td>3x</td>
      </tr>
      <tr>
        <td>Convert to Lowercase</td>
        <td>0.219419</td>
        <td>0.222543</td>
        <td>3x</td>
      </tr>
      <tr>
        <td>Cosine Similarity</td>
        <td>0.017106</td>
        <td>0.008261</td>
        <td>2.5x</td>
      </tr>
    </tbody>
  </table>
  <p>Run the benchmarking script to test performance:
    <pre><code>python benchmarks/benchmark.py</code></pre>
  </p>
</div>

<hr>

<div class="section">
  <h2>🎮 Interactive Demo</h2>
  <p>
    <button onclick="alert('Interactive buttons don’t work on GitHub! Run the Python script locally.')">
      🚀 Try Me Locally!
    </button>
  </p>
</div>

<hr>

<div class="section">
  <h2>🧑‍💻 Contributing</h2>
  <p>We welcome contributions! Please:</p>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch:
      <pre><code>git checkout -b feature/your-feature-name</code></pre>
    </li>
    <li>Commit your changes and open a pull request.</li>
  </ol>
</div>

<hr>

<div class="section">
  <h2>📞 Contact</h2>
  <p>For questions or suggestions, feel free to reach out:</p>
  <ul>
    <li><strong>Email:</strong> <a href="mailto:tshah@csuchico.edu">tshah@csuchico.edu</a></li>
  </ul>
</div>

<hr>

<div class="section">
  <h2>🚀 Running the Code Base</h2>
  <p>Follow these steps to successfully run the MATH608_PROJECT:</p>
  <ol>
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/shahtirth07/MATH608_PROJECT.git</code></pre>
    </li>
    <li><strong>Navigate to the project directory:</strong>
      <pre><code>cd MATH608_PROJECT</code></pre>
    </li>
    <li><strong>Build the C++ shared library and Python extension:</strong>
      <pre><code> cmake -S . -B build</code></pre>
      <pre><code> cmake --build builde</code></pre>
      <pre><code>cd build</code></pre>
      <pre><code>cp data_cleaning.cpython-*.so ../tests/</code></pre>
    </li>
    <li><strong>Run the benchmarking tests:</strong>
      <pre><code>cd ../tests</code></pre>
      <pre><code> python3 benchmarks.py </code></pre>
    </li>
  </ol>
</div>

<hr>

</body>
</html>
