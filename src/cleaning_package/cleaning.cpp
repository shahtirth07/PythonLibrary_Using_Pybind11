#include <string>
#include <vector>
#include <cstring>
#include <iostream>

// Function to trim spaces from a string
extern "C" void trim_spaces(char *str)
{
    std::string s(str);
    size_t start = s.find_first_not_of(' ');
    size_t end = s.find_last_not_of(' ');
    std::string trimmed = (start == std::string::npos) ? "" : s.substr(start, end - start + 1);
    std::strcpy(str, trimmed.c_str());
}

// Function to count nulls (0s) in an integer array
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
