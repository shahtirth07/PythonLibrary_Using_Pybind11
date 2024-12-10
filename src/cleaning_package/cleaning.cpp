#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <iostream>

// Trim spaces from both ends
extern "C" void trim_spaces(char *str)
{
    std::string s(str);
    size_t start = s.find_first_not_of(' ');
    size_t end = s.find_last_not_of(' ');
    std::string trimmed = (start == std::string::npos) ? "" : s.substr(start, end - start + 1);
    std::strcpy(str, trimmed.c_str());
}

// cosine similarity
// Count nulls (0s) in an array
extern "C" int count_nulls(int *arr, int size)
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
extern "C" void to_lowercase(char *str)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        str[i] = std::tolower(str[i]);
    }
}

// Replace a character in a string with another
extern "C" void replace_char(char *str, char old_char, char new_char)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == old_char)
        {
            str[i] = new_char;
        }
    }
}

extern "C" double cosine_similarity(const double* A, const double* B, int size) {
    double dot_product = 0.0;
    double norm_a = 0.0;
    double norm_b = 0.0;

    for (int i = 0; i < size; ++i) {
        dot_product += A[i] * B[i];
        norm_a += A[i] * A[i];
        norm_b += B[i] * B[i];
    }

    norm_a = std::sqrt(norm_a);
    norm_b = std::sqrt(norm_b);

    return (norm_a > 0 && norm_b > 0) ? (dot_product / (norm_a * norm_b)) : 0.0;
}
