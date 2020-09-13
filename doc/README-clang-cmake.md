这是在clang/clang++下通过Cmake同时编译多文件工程的配置方式，相应的工作区文件在[这里](../cmake_with_clang_chang++) 

通过这种方式，你将可以完成：

* 单文件的编译、运行
* 多文件工程的同时编译、运行、调试

你将无法完成：

* 单文件的调试
* 控制台对中文字符集的支持

---

## 前置条件

需要环境：

* LLVM（请务必安装到默认位置`C:/Program Files/`，并加入系统环境变量）
* MinGW（将MinGW文件夹中的所有内容合并到LLVM的目录下，然后把`C:\Program Files\LLVM\bin`目录下的`mingw32-make.exe`文件改为`make.exe`）
* CMake（请安装到默认位置`C:/Program Files/`，并加入系统环境变量）

需要vscode插件：

* C/C++
* Code Runner
* Clang Command Adapter
* CMake
* CMake Tools

---

## C或C++语言适配

> **下面两种方案你只能二选一，因为二者有冲突** 

### 1. C++程序的配置

如果你需要编写C++程序（文件后缀为`.cpp`），你什么都不用改，可以直接使用。前提是你完全按照上面的步骤做了。

### 2. C程序的配置

如果你需要写C语言程序（文件后缀为`.c`），你需要：

* 将`c_cpp_properties.json`文件中的`"compilerPath"`字段后面的路径改成你的`LLVM`对应的`gcc.exe`文件所在的目录（需要精确到`/gcc.exe`）
* 将`CMakeLists.txt`文件中的`set(CMAKE_CXX_COMPILER "clang++")`改为`set(CMAKE_CXX_COMPILER "clang")`，并把它下一行的`set (CMAKE_CXX_FLAGS "-g -Wall -static-libgcc --target=x86_64-w64-mingw -std=c++14")`中的`-std=c++14`改为`-std=c11`

---

## 自定义代码格式化风格（可选）

在`settings.json`文件中的`"C_Cpp.clang_format_fallbackStyle"`字段后面，按照自己的需要进行修改

如果需要默认风格（括号换行），请将此字段注释掉

更改代码风格入门：

* （科学上网）https://stackoverflow.com/questions/46111834/format-curly-braces-on-same-line-in-c-vscode 
* （科学上网）https://medium.com/@zamhuang/vscode-%E5%A6%82%E4%BD%95%E5%9C%A8-vscode-%E4%B8%8A%E8%87%AA%E5%AE%9A%E7%BE%A9-c-%E7%9A%84-coding-style-c8eb199c57ce 

---

## 注意事项

* 工作区和文件的路径不能含有中文
* 所有你自己写的头文件都需要放在`include`文件夹里。否则需要你自行更改`CMakeLists.txt`文件的设置

---

## 使用方法

以下文件夹/文件属于工作区部分，**不可删除** 

| 范围                 | 名称                      | 说明                             |
| -------------------- | ------------------------- | -------------------------------- |
| 文件夹及文件夹中内容 | `.vscode`                 | vscode工作区配置文件夹           |
| 文件夹               | `include`                 | 用于存放你自己写的头文件的文件夹 |
| 文件                 | `CMakeLists.txt`          | 用于构建工程                     |
| 文件                 | `clean_workspace_exe.bat` | 用于清除构建后生成的.exe文件     |

以下文件是示例文件，**允许删除**，但是现在先不要删，等你阅读完本文档，再删除。

| 范围 | 名称             |
| ---- | ---------------- |
| 文件 | `include/swap.h` |
| 文件 | `include/test.h` |
| 文件 | `/main.cpp`      |
| 文件 | `/swap.cpp`      |
| 文件 | `/test.cpp`      |
| 文件 | `/start.cpp`     |

你需要知道的快捷键：

|                                   |                              |
| --------------------------------- | ---------------------------- |
| 仅编译（`build`）文件（但不执行） | `ctrl + shift + B`           |
| 编译 + 执行                       | `ctrl + F5`                  |
| 编译 + 调试                       | `F5`（前提是你已经打好断点） |

### 1.单文件的编译、运行

示例文件中，`start.cpp`是单文件。

打开文件，取消注释，点击右键，选择`Run Code`，即可运行。

### 2.多文件的同时编译、运行、调试

> 在进行下面的步骤之前，你需要**重新注释掉`start.cpp`中的内容**。原因是`main,cpp`中也有`main()`函数，两个`main()`函数会造成冲突

示例文件中，`main.cpp`是多文件的入口，它包括了`swap()`和`test()`两个函数，分别对应`swap.cpp`和`test.cpp`，而这两个文件又分别在`include`文件夹中含有自己的头文件`swap.h`和`test.h`

#### 打开VSCode

当你打开VSCode时，`CMake`插件会自动配置（即`Configure`，生成`MakeFile`），但是不会编译。

同时，由于CMake插件的自动配置，会产生`build`文件夹和`Bin`文件夹。`build`文件夹是CMake的构建产物存放的位置，`Bin`是用于存放编译之后生成的`.exe`可执行文件的文件夹。`build`和`Bin`都可以删除，但是**不建议删除**。原因是需要再次`Configure`和`build`，比较麻烦。

如果你想运行或调试程序，你需要先按下图：手动`build`，然后你可以选择`ctrl + F5`执行或`F5`调试。注意这里有一点问题：第一次打开时，如果你`build`后`ctrl + F5`执行，可能会出现一堆黄字报错，然后再`ctrl + F5`执行，才会正确执行。

> 打开左侧的CMake插件栏，上方有`Configure All Projects`和`Build All Projects`，

<img src="F:\vscode_based_C_CPP_workspace_template\doc\img\Snipaste_2020-09-13_16-02-21.png" style="zoom:40%;" />

#### 重新编写文件，或者对文件/文件夹做出改动后

和上图一样，先`Configure`再`Build`，然后`ctrl + F5`执行或者打好断点按`F5`调试。实际上，当你对文件改动时，CMake会检测到文件变化并自动`Configure`，而你只需执行编译和执行的步骤即可。

---

## 参考

* https://blog.csdn.net/weixin_44049923/article/details/103619882
* https://www.zhihu.com/question/30315894/answer/154979413

