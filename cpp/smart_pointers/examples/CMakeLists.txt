cmake_minimum_required(VERSION 3.10)
project(examples)

set(CMAKE_CXX_STANDARD 11)

list(APPEND CMAKE_CXX_FLAGS "-Wall -Wextra -fsanitize=address -fno-omit-frame-pointer")

add_executable(shared shared.cpp)
add_executable(shared_optimized shared_optimized.cpp)
add_executable(unique unique.cpp)
add_executable(unique_optimized unique_optimized.cpp)

add_executable(raii raii.cpp)
add_executable(ownership ownership.cpp)
add_executable(less_new_less_leak less_new_less_leak.cpp)