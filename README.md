# 基于VSCode的C/C++单文件与多文件编译执行调试环境的搭建

## 前言

所有内容都是我借鉴博客或者文章，加上自己的一点点修改做的，在Windows平台下进行多次测试，并且把每个仓库的功能和无法实现的部分，以及配置和使用方法全部在相应的`README`中做出了说明。

我已经配置好了绝大部分内容，只需要你安装一下需要的环境加上一点简单的配置即可，基本上算是开箱即用了。

## 目录

本仓库提供了四种配置方案，这四种方案互相冲突，请根据需要选择一种使用：

| 文件夹                | 说明                                                         | 使用方法                               |
| --------------------- | ------------------------------------------------------------ | -------------------------------------- |
| `gcc_g++`             | 以`gcc/g++`作为编译器的工作区模板                            | [README](./doc/README-gcc.md)          |
| `clang_clang++`       | 以`clang/clang++`作为编译器的工作区模板                      | [README](./doc/README-clang.md)        |
| `cmake_clang_clang++` | 以`clang/clang++`作为编译器，通过`CMake`同时构建多个文件的工作区模板 | [README](./doc/README-clang-cmake.md)  |
| `cmakepygccgpp`       | 以`gcc/g++`或`clang/clang++`作为编译器（二选一），通过`python`脚本调用`CMake`同时构建多个文件的工作区模板 | [README](./doc/README-cmake-py-gcc.md) |
| `global`              | 我的全局配置文件，与VSCode的界面设置相关，这个不是必须要用的 | [README](./doc/README-global.md)       |

四种方案的优劣点如下：

| 文件夹                | 可以做到（或优点）                                  | 无法做到（或缺点）                                       | 配置难度 |
| --------------------- | --------------------------------------------------- | -------------------------------------------------------- | -------- |
| `gcc_g++`             | 文件单个编译运行调试，控制台支持中文                | 多文件工程同时编译调试和运行                             | ★☆☆☆☆    |
| `clang_clang++`       | 文件单个编译运行调试，代码提示和性能比`gcc/g++`更好 | 多文件工程同时编译调试和运行。控制台中文乱码（这个无解） | ★★★☆☆    |
| `cmake_clang_clang++` | 多文件工程同时编译调试和运行，单文件编译和运行      | 单文件调试，控制台中文乱码。                             | ★★★★☆    |
| `cmakepygccgpp`       | 多文件工程同时编译调试和运行。架构清晰              | 单文件编译、调试、运行                                   | ★★☆☆☆    |

个人推荐：

* `clang_clang++`（如果你经常编译单文件）
* `cmakepygccgpp` （如果你经常同时编译多文件工程）

## 后记

弄好多文件同时编译对我来说实在有点难，所以目前仍无法在`cmake_clang_clang++`工作区里调试单个文件。如果你知道如何配置，或者可以完善其他功能（比如对于`cmake_clang_clang++`工作区目前只能在`include`文件夹里放自己的头文件），请issue或pull request。

这个仓库对于想要用VSCode写C/C++的新手朋友们（比如我）来说，是够用的，当你学会怎么搞之后，你都可以自己写配置文件了，肯定就不需要这个仓库了。总之，祝编程愉快。

## 参考

* https://www.zhihu.com/question/30315894/answer/154979413
* https://www.cnblogs.com/esllovesn/p/10012653.html
* https://blog.csdn.net/weixin_44049923/article/details/103619882 
* https://github.com/hysonger/VSCode-CPP-Template
* https://microsoft.github.io/language-server-protocol/implementors/servers/ （官方文档 -> 对于不同语言的的配置方案）