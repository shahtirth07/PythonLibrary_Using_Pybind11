#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stdexcept>

using namespace std;

// Trim spaces from both ends
void trim_spaces(char *str)
{
    string s(str);
    size_t start = s.find_first_not_of(' ');
    size_t end = s.find_last_not_of(' ');
    string trimmed = (start == string::npos) ? "" : s.substr(start, end - start + 1);
    strcpy(str, trimmed.c_str());
}

// Count nulls (0s) in an array
int count_nulls(int *arr, int size)
{
    int count = 0;
    for (int i = 0; i < size; ++i)
    {
        if (arr[i] == 0)
            count++;
    }
    return count;
}

// Convert string to lowercase
void to_lowercase(char *str)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        str[i] = tolower(str[i]);
    }
}

// Function to compute the dot product of two vectors
double dotProduct(const std::vector<double> &vec_a, const std::vector<double> &vec_b)
{
    double dot = 0.0;
    for (size_t i = 0; i < vec_a.size(); ++i)
    {
        dot += vec_a[i] * vec_b[i];
    }
    return dot;
}

// Function to compute the magnitude (Euclidean norm) of a vector
double magnitude(const std::vector<double> &vec)
{
    double sum = 0.0;
    for (double val : vec)
    {
        sum += val * val;
    }
    return std::sqrt(sum);
}

// Function to compute cosine similarity between two vectors
double cosineSimilarity(const std::vector<double> &vec_a, const std::vector<double> &vec_b)
{
    // Ensure the vectors have the same size
    if (vec_a.size() != vec_b.size())
    {
        throw std::invalid_argument("Vectors must be of the same size.");
    }

    // Compute the dot product and magnitudes
    double dot = dotProduct(vec_a, vec_b);
    double mag_a = magnitude(vec_a);
    double mag_b = magnitude(vec_b);

    // Avoid division by zero
    if (mag_a == 0.0 || mag_b == 0.0)
    {
        return 0.0; // Return 0 similarity if either vector is zero
    }

    // Compute cosine similarity
    return dot / (mag_a * mag_b);
}
