cmake_minimum_required(VERSION 3.12)
project(data_cleaning)

find_package(pybind11 REQUIRED)

add_library(data_cleaning MODULE
    ./src/data_cleaning.cpp  # Include your source file(s)
)

target_link_libraries(data_cleaning PRIVATE pybind11::module)
