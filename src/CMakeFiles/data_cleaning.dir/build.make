# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src"

# Include any dependencies generated for this target.
include CMakeFiles/data_cleaning.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/data_cleaning.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/data_cleaning.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/data_cleaning.dir/flags.make

CMakeFiles/data_cleaning.dir/bindings.cpp.o: CMakeFiles/data_cleaning.dir/flags.make
CMakeFiles/data_cleaning.dir/bindings.cpp.o: bindings.cpp
CMakeFiles/data_cleaning.dir/bindings.cpp.o: CMakeFiles/data_cleaning.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/data_cleaning.dir/bindings.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/data_cleaning.dir/bindings.cpp.o -MF CMakeFiles/data_cleaning.dir/bindings.cpp.o.d -o CMakeFiles/data_cleaning.dir/bindings.cpp.o -c "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/bindings.cpp"

CMakeFiles/data_cleaning.dir/bindings.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/data_cleaning.dir/bindings.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/bindings.cpp" > CMakeFiles/data_cleaning.dir/bindings.cpp.i

CMakeFiles/data_cleaning.dir/bindings.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/data_cleaning.dir/bindings.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/bindings.cpp" -o CMakeFiles/data_cleaning.dir/bindings.cpp.s

CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o: CMakeFiles/data_cleaning.dir/flags.make
CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o: data_cleaning.cpp
CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o: CMakeFiles/data_cleaning.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o -MF CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o.d -o CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o -c "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/data_cleaning.cpp"

CMakeFiles/data_cleaning.dir/data_cleaning.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/data_cleaning.dir/data_cleaning.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/data_cleaning.cpp" > CMakeFiles/data_cleaning.dir/data_cleaning.cpp.i

CMakeFiles/data_cleaning.dir/data_cleaning.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/data_cleaning.dir/data_cleaning.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/data_cleaning.cpp" -o CMakeFiles/data_cleaning.dir/data_cleaning.cpp.s

# Object files for target data_cleaning
data_cleaning_OBJECTS = \
"CMakeFiles/data_cleaning.dir/bindings.cpp.o" \
"CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o"

# External object files for target data_cleaning
data_cleaning_EXTERNAL_OBJECTS =

data_cleaning.cpython-310-x86_64-linux-gnu.so: CMakeFiles/data_cleaning.dir/bindings.cpp.o
data_cleaning.cpython-310-x86_64-linux-gnu.so: CMakeFiles/data_cleaning.dir/data_cleaning.cpp.o
data_cleaning.cpython-310-x86_64-linux-gnu.so: CMakeFiles/data_cleaning.dir/build.make
data_cleaning.cpython-310-x86_64-linux-gnu.so: CMakeFiles/data_cleaning.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared module data_cleaning.cpython-310-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/data_cleaning.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/data_cleaning.dir/build: data_cleaning.cpython-310-x86_64-linux-gnu.so
.PHONY : CMakeFiles/data_cleaning.dir/build

CMakeFiles/data_cleaning.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/data_cleaning.dir/cmake_clean.cmake
.PHONY : CMakeFiles/data_cleaning.dir/clean

CMakeFiles/data_cleaning.dir/depend:
	cd "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning" "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning" "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src" "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src" "/mnt/c/Users/tshah/OneDrive - California State University Chico/Desktop/data_cleaning/src/CMakeFiles/data_cleaning.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/data_cleaning.dir/depend

