#cmake版本
cmake_minimum_required (VERSION 3.0)

project(${PROJ_NAME})

# 如果你需要用g++编译器，就把第1个取消注释，并把2和3注释掉
# 如果你需要用clang++编译器，就把第1个取消注释，把第2和第3个注释掉

# 1
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")
# 2
set(CMAKE_CXX_COMPILER "clang++")
# 3
set (CMAKE_CXX_FLAGS  "-g -Wall -static-libgcc --target=x86_64-w64-mingw -std=c++14")
# 注：CMAKE_C_FLAGS：编译C文件时的选项，如-g；也可以通过add_definitions添加编译选项

# 判断build type是debug还是release
#指定输出路径
if(${BUILD_TYPE} MATCHES "debug")
    set(CMAKE_BUILD_TYPE "Debug")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin/debug)
else()
    set(CMAKE_BUILD_TYPE "Release")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ../bin/release)
endif()

# 添加头文件包含路径
INCLUDE_DIRECTORIES(${PROJECT_SOURCE_DIR}/src/include1
                    ${PROJECT_SOURCE_DIR}/src/include2)

# 添加cpp文件
aux_source_directory(${PROJECT_SOURCE_DIR}/src DIRSRCS)
aux_source_directory(${PROJECT_SOURCE_DIR}/src/include1 DIRSRCS)
aux_source_directory(${PROJECT_SOURCE_DIR}/src/include2 DIRSRCS)

# 指定生成目标
add_executable(${PROJECT_NAME} ${DIRSRCS})
