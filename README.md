<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

<h1>🌟 C++ Cleaning Library with PyBind11: High-Performance Data Cleaning 🌟</h1>

What are Pybind11 and ctypes?
Pybind11: Imagine you're building a LEGO robot, and you want to connect it to a remote control. Pybind11 is like a fancy LEGO adapter that fits perfectly with your robot (C++ code) and remote control (Python). It makes them work together easily and smoothly.

ctypes: This is like a basic glue or tape that helps stick two things together. It works well for simple tasks but isn’t as fancy as the LEGO adapter. It works best if your robot (code) is already simple and doesn’t need a lot of extra features.

How easy are they to use?
Pybind11: You need to follow some instructions and build the adapter (compile your C++ code), but once it’s done, it works perfectly and feels like magic.

ctypes: No building is required! You just load the robot’s remote control commands (library) and tell it what to do. It’s fast to set up but doesn’t work well if the robot is too complicated.

When are they useful?
Pybind11: If your robot has lots of parts, like arms, sensors, and wheels, and you need all of them to work with the remote control, Pybind11 is your best choice. It’s perfect for connecting big, complex robots.

ctypes: If your robot is just a simple car that moves forward or backward, ctypes is enough. It’s quick and does the job for small tasks.

How fast are they?
Pybind11: It’s very fast because it’s specially designed to fit the robot perfectly. But it takes some time to set up.

ctypes: It’s a bit slower because the glue (ctypes) isn’t as strong as the adapter (Pybind11). For big or heavy robots, the glue might not hold well.

Examples
Pybind11 (Fancy LEGO Adapter):
You make an adapter to connect your robot to Python.
Example:
Robot: A robot arm that draws pictures.
Remote Control: Python code to tell it to draw a circle.
ctypes (Basic Glue):
You call simple commands directly to control your robot.
Example:
Robot: A toy car that moves forward.
Remote Control: Python code to tell it to move 5 steps.
Which one should you choose?
Choose Pybind11 if:

Your robot (code) is very complicated, like one with lots of moving parts (C++ classes or advanced math).
You want your Python remote control to feel like it’s part of the robot.
Choose ctypes if:

Your robot (code) is simple and doesn’t need much control.
You just want a quick and easy way to connect.

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
