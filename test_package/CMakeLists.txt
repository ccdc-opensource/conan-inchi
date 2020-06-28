cmake_minimum_required(VERSION 3.10.0)
project(test_package CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(test_package ${CONAN_LIBS})
