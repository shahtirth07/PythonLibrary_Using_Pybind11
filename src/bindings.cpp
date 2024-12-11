#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cmath>
#include <stdexcept>

extern "C" void trim_spaces(char *str);
extern "C" int count_nulls(int *arr, int size);
extern "C" void to_lowercase(char *str);
extern "C" void replace_char(char *str, char old_char, char new_char);

namespace py = pybind11;

// Function to calculate cosine similarity
double cosine_similarity(const double *A, const double *B, int size)
{
    double dot_product = 0.0;
    double norm_a = 0.0;
    double norm_b = 0.0;

    for (int i = 0; i < size; ++i)
    {
        dot_product += A[i] * B[i];
        norm_a += A[i] * A[i];
        norm_b += B[i] * B[i];
    }

    norm_a = std::sqrt(norm_a);
    norm_b = std::sqrt(norm_b);

    return (norm_a > 0 && norm_b > 0) ? (dot_product / (norm_a * norm_b)) : 0.0;
}

PYBIND11_MODULE(data_cleaning, m)
{
    m.doc() = "Data cleaning utilities implemented in C++";

    // Binding the trim_spaces function
    m.def("trim_spaces", [](const std::string &input) -> std::string
          {
              std::string result = input; // Copy input
              char *data = result.data(); // Get mutable char* pointer
              trim_spaces(data);
              return result; // Return the modified string
          });

    // Binding the count_nulls function
    m.def("count_nulls", [](py::array_t<int> input)
          {
              auto buffer = input.request();
              int *data = static_cast<int *>(buffer.ptr);
              return count_nulls(data, buffer.size); });

    // Binding the to_lowercase function
    m.def("to_lowercase", [](const std::string &input) -> std::string
          {
              std::string result = input; // Copy input
              char *data = result.data(); // Get mutable char* pointer
              to_lowercase(data);
              return result; // Return the modified string
          });

    // Binding the cosine_similarity function
    m.def("cosine_similarity", [](py::array_t<double> A, py::array_t<double> B)
          {
              auto buffer_a = A.request();
              auto buffer_b = B.request();

              if (buffer_a.size != buffer_b.size) {
                  throw std::runtime_error("Input vectors must have the same size.");
              }

              const double *data_a = static_cast<double *>(buffer_a.ptr);
              const double *data_b = static_cast<double *>(buffer_b.ptr);

              return cosine_similarity(data_a, data_b, static_cast<int>(buffer_a.size)); });
}
