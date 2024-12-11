#ifndef DATA_CLEANING_H
#define DATA_CLEANING_H

#include <string>

// Function declarations
void trim_spaces(char *str);
int count_nulls(int *arr, int size);
void to_lowercase(char *str);
double cosine_similarity(const double *A, const double *B, int size);

#endif // DATA_CLEANING_H
