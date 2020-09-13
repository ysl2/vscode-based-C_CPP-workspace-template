#cmake版本
cmake_minimum_required(VERSION 3.0.0)
project(MYPROJECT VERSION 0.1.0)

include(CTest)
enable_testing()

set(CMAKE_CXX_COMPILER "clang++")
set (CMAKE_CXX_FLAGS  "-g -Wall -static-libgcc --target=x86_64-w64-mingw -std=c++14")
#增加头文件目录（该目录下只有头文件），如果一个目录下有头文件也有源文件，则需要增加模块目录，而不用增加头文件目录
include_directories(${PROJECT_SOURCE_DIR}/include)

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 指定生成目标
add_executable(DIR_SRCS ${DIR_SRCS})
#指定输出路径为项目文件夹下的Bin目录
set(EXECUTABLE_OUTPUT_PATH  ${PROJECT_SOURCE_DIR}/Bin)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)

