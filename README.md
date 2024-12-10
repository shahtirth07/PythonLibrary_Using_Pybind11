<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- <title>MATH608_PROJECT</title> -->
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1 style="text-align: center; color: #4CAF50;">🌟 MATH608_PROJECT: High-Performance Data Cleaning 🌟</h1>


<hr>

<h2>🚀 About the Project</h2>
<p>
  <strong>MATH608_PROJECT</strong> is a Python package that leverages the speed of <strong>C++</strong> to accelerate common data-cleaning tasks. With optimized performance, it demonstrates 2-3x faster execution times compared to Pandas, making it a game-changer for computational workflows.
</p>

<hr>

<h2>⚙️ Features</h2>
<ul>
  <li>Trim spaces, count nulls, convert to lowercase, replace characters, and compute cosine similarity.</li>
  <li>Seamless integration with Python workflows via <code>pybind11</code>.</li>
  <li>Includes a benchmarking script to showcase performance gains.</li>
</ul>

<hr>

<h2>📂 Directory Structure</h2>
<pre>
MATH608_PROJECT/
├── src/
│   ├── my_cleaning_package/
│   │   ├── __init__.py
│   │   └── cleaning.cpp       # C++ code for data cleaning
│   └── setup.py               # Package setup script
├── tests/
│   └── test_cleaning.py       # Unit tests for the package
├── benchmarks/
│   └── benchmark.py           # Benchmarking script
└── README.md                  # Project documentation
</pre>

<hr>

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

<hr>

<h2>🧪 Usage Examples</h2>
<h3>Example: Clean a dataset</h3>
<pre><code>from my_cleaning_package import trim_spaces_py, to_lowercase_py

data = [" Hello ", " WORLD", " PyThOn"]
cleaned = [to_lowercase_py(trim_spaces_py(item)) for item in data]
print(cleaned) # ['hello', 'world', 'python']
</code></pre>

<hr>

<h2>📊 Benchmark Results</h2>
<table border="1" style="width: 100%; border-collapse: collapse; text-align: center;">
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
      <td>0.002</td>
      <td>0.0008</td>
      <td>2.5x</td>
    </tr>
    <tr>
      <td>Count Nulls</td>
      <td>0.0015</td>
      <td>0.0005</td>
      <td>3x</td>
    </tr>
    <tr>
      <td>Convert to Lowercase</td>
      <td>0.003</td>
      <td>0.001</td>
      <td>3x</td>
    </tr>
    <tr>
      <td>Replace Characters</td>
      <td>0.0025</td>
      <td>0.0007</td>
      <td>3.6x</td>
    </tr>
    <tr>
      <td>Cosine Similarity</td>
      <td>0.045</td>
      <td>0.018</td>
      <td>2.5x</td>
    </tr>
  </tbody>
</table>

<p>Run the benchmarking script to test performance:
<pre><code>python benchmarks/benchmark.py</code></pre>
</p>

<hr>

<h2>🎮 Interactive Demo</h2>
<p>
  <button style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px;"
          onclick="alert('Interactive buttons don’t work on GitHub! Run the Python script locally.')">
    🚀 Try Me Locally!
  </button>
</p>

<hr>

<h2>🧑‍💻 Contributing</h2>
<p>We welcome contributions! Please:</p>
<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch:
    <pre><code>git checkout -b feature/your-feature-name</code></pre>
  </li>
  <li>Commit your changes and open a pull request.</li>
</ol>

<hr>

<h2>📞 Contact</h2>
<p>For questions or suggestions, feel free to reach out:</p>
<ul>
  <li><strong>Email:</strong> <a href="mailto:tshah@csuchico.edu">tshah@csuchico.edu</a></li>
</ul>

</body>
</html>
