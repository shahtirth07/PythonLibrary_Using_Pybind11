<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="assets/styles.css">
</head>
<body>

<h1>🌟 C++ Cleaning Library with PyBind11: High-Performance Data Cleaning 🌟</h1>

<div class="section">
  <h2>🔧 PyBind11 and Ctypes</h2>
  <p>
    <strong>What are Pybind11 and Ctypes?</strong>
  </p>
  <p>
    <strong>Pybind11:</strong> Imagine you're building a LEGO robot, and you want to connect it to a remote control. Pybind11 is like a fancy LEGO adapter that fits perfectly with your robot (C++ code) and remote control (Python). It makes them work together easily and smoothly.
  </p>
  <p>
    <strong>Ctypes:</strong> This is like a basic glue or tape that helps stick two things together. It works well for simple tasks but isn’t as fancy as the LEGO adapter. It works best if your robot (code) is already simple and doesn’t need a lot of extra features.
  </p>
  
  <p>
    <strong>How easy are they to use?</strong>
  </p>
  <p>
    <strong>Pybind11:</strong> You need to follow some instructions and build the adapter (compile your C++ code), but once it’s done, it works perfectly and feels like magic.
  </p>
  <p>
    <strong>Ctypes:</strong> No building is required! You just load the robot’s remote control commands (library) and tell it what to do. It’s fast to set up but doesn’t work well if the robot is too complicated.
  </p>
  
  <p>
    <strong>When are they useful?</strong>
  </p>
  <ul>
    <li>
      <strong>Pybind11:</strong> If your robot has lots of parts, like arms, sensors, and wheels, and you need all of them to work with the remote control, Pybind11 is your best choice. It’s perfect for connecting big, complex robots.
    </li>
    <li>
      <strong>Ctypes:</strong> If your robot is just a simple car that moves forward or backward, ctypes is enough. It’s quick and does the job for small tasks.
    </li>
  </ul>
  
  <p>
    <strong>How fast are they?</strong>
  </p>
  <ul>
    <li>
      <strong>Pybind11:</strong> It’s very fast because it’s specially designed to fit the robot perfectly. But it takes some time to set up.
    </li>
    <li>
      <strong>Ctypes:</strong> It’s a bit slower because the glue (ctypes) isn’t as strong as the adapter (Pybind11). For big or heavy robots, the glue might not hold well.
    </li>
  </ul>
  
  <p>
    <strong>Examples:</strong>
  </p>
  <ul>
    <li>
      <strong>Pybind11 (Fancy LEGO Adapter):</strong> You make an adapter to connect your robot to Python.
      <br>
      Example:
      <ul>
        <li>Robot: A robot arm that draws pictures.</li>
        <li>Remote Control: Python code to tell it to draw a circle.</li>
      </ul>
    </li>
    <li>
      <strong>Ctypes (Basic Glue):</strong> You call simple commands directly to control your robot.
      <br>
      Example:
      <ul>
        <li>Robot: A toy car that moves forward.</li>
        <li>Remote Control: Python code to tell it to move 5 steps.</li>
      </ul>
    </li>
  </ul>
  
  <p>
    <strong>Which one should you choose?</strong>
  </p>
  <ul>
    <li>
      Choose <strong>Pybind11</strong> if:
      <ul>
        <li>Your robot (code) is very complicated, like one with lots of moving parts (C++ classes or advanced math).</li>
        <li>You want your Python remote control to feel like it’s part of the robot.</li>
      </ul>
    </li>
    <li>
      Choose <strong>Ctypes</strong> if:
      <ul>
        <li>Your robot (code) is simple and doesn’t need much control.</li>
        <li>You just want a quick and easy way to connect.</li>
      </ul>
    </li>
  </ul>
</div>

<hr>

<div class="section">
  <h2>🚀 About the Project</h2>
  <p>
    <strong>PythonLibrary_Using_PyBind11</strong> is a Python package that leverages the speed of <strong>C++</strong> to accelerate common data-cleaning tasks. With optimized performance, it is expected 2-3x faster execution times compared to Pandas/Numpy, making it a game-changer for computational workflows.
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
        <th>Python Library Time (s)</th>
        <th>C++ Time (s)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Trim Spaces</td>
        <td>0.003315</td>
        <td>0.000065</td>
      </tr>
      <tr>
        <td>Count Nulls</td>
        <td>0.002970</td>
        <td>0.007952</td>
      </tr>
      <tr>
        <td>Cosine Similarity</td>
        <td>0.000479</td>
        <td>0.001057</td>
      </tr>
      <tr>
        <td>Convert to Lowercase</td>
        <td>0.000002</td>
        <td>0.000072</td>
      </tr>
    </tbody>
  </table>
  <p>
    The results demonstrate that <strong>C++</strong> can achieve significant performance benefits for certain tasks, while for others, Python's optimized libraries like Pandas and NumPy remain competitive or faster. Use cases where C++ shines involve tasks requiring raw computational power or processing large datasets.
  </p>
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

<h1>Performance Comparison: Python Libraries vs C++ Implementation</h1>
    <p>
        When comparing the performance of Python libraries like <strong>NumPy</strong> or <strong>Pandas</strong> with custom C++ implementations, 
        Python libraries often demonstrate faster performance for specific tasks. This is due to the following reasons:
    </p>
    <ul>
        <li><strong>Optimized Libraries:</strong> NumPy and Pandas are built on highly optimized, low-level libraries such as BLAS, LAPACK, and Intel MKL, which are finely tuned for vectorized operations.</li>
        <li><strong>Parallelization:</strong> These libraries leverage parallel processing and hardware acceleration, such as SIMD (Single Instruction, Multiple Data) or GPU support, out of the box.</li>
        <li><strong>Memory Layout:</strong> NumPy arrays are optimized for memory alignment and efficient cache utilization, which contributes to their superior performance.</li>
    </ul>

    
<h1>Building and Optimizing the C++ Codebase</h1>
    <p>To improve the performance of your C++ codebase, you can enable compiler optimizations. These optimizations can significantly enhance runtime performance by enabling advanced instruction-level optimizations and hardware-specific tuning. Follow the steps below:</p>

<h2>Compiler Optimization Flags</h2>
<ul>
    <li><strong>-O2:</strong> Enables a broad set of optimizations that improve runtime performance without significantly increasing compilation time.</li>
    <li><strong>-O3:</strong> Enables all optimizations in <code>-O2</code> and adds more aggressive ones, such as loop unrolling and vectorization.</li>
    <li><strong>-march=native:</strong> Generates code optimized for the architecture of the host machine, leveraging specific hardware capabilities.</li>
</ul>
<h2>Steps to Compile with Optimization Flags</h2>
  <ol>
      <li>
          <p>Make sure you have <strong>g++</strong> or a similar compiler installed on your system.</p>
          <p>To check your compiler version, run:</p>
          <pre><code>g++ --version</code></pre>
      </li>
      <li>
          <p>Compile your C++ code with optimization flags. For example:</p>
          <pre><code>g++ -O3 -march=native -fopenmp -o data_cleaning.so data_cleaning.cpp -shared -fPIC `python3 -m pybind11 --includes`</code></pre>
          <p>This command does the following:</p>
          <ul>
              <li>Enables <code>-O3</code> optimizations for maximum performance.</li>
              <li>Uses <code>-march=native</code> to optimize for the host CPU architecture.</li>
              <li>Includes <code>-fopenmp</code> to enable OpenMP parallelization.</li>
              <li>Generates a shared object file (<code>data_cleaning.so</code>) for Python bindings.</li>
          </ul>
      </li>
      <li>
          <p>Test the compiled code by importing it into Python and running benchmarks.</p>
          <pre><code>
import data_cleaning
# Example: Test cosine similarity function
result = data_cleaning.cosine_similarity([1, 2, 3], [4, 5, 6])
print(result)
            </code></pre>
        </li>
    </ol>

<h2>Notes on Optimization</h2>
<ul>
    <li>Even with <code>-O3</code> and <code>-march=native</code>, the performance may still not match that of Python libraries like NumPy. This is because these libraries are built on highly optimized, low-level libraries like BLAS and LAPACK.</li>
    <li>For even greater performance, consider integrating BLAS/LAPACK directly into your C++ code or using libraries like <a href="https://eigen.tuxfamily.org/dox/" target="_blank">Eigen</a>.</li>
</ul>

<h2>Conclusion</h2>
<p>
        Adding compiler optimization flags like <code>-O2</code>, <code>-O3</code>, and <code>-march=native</code> can significantly improve performance for computationally intensive tasks. 
        However, for large-scale numerical operations, leveraging highly optimized libraries or hardware acceleration may provide the best results.
</p>
<hr>

<div class="section">
  <h2>📞 Contact</h2>
  <p>For questions or suggestions, feel free to reach out:</p>
  <ul>
    <li><strong>Email:</strong> <a href="mailto:tshah@csuchico.edu">tshah@csuchico.edu</a></li>
  </ul>
</div>

</body>
</html>
