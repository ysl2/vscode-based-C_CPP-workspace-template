cmake_minimum_required (VERSION 3.0)

project(${PROJ_NAME})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# 判断build type是debug还是release
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
add_executable(${PROJECT_NAME} ${DIRSRCS})