

> 本配置以https://github.com/hysonger/VSCode-CPP-Template为模板，根据我自己的实际情况做出修改，并修正了原作者`build.py`文件中的一处bug
>
> 在此十分感谢原作者，他选择用python脚本执行cmake，大幅度地摆脱了vscode对于插件的依赖性

这是在gcc/g++下通过python脚本调用Cmake同时编译多文件工程的配置方式，相应的配置文件在[这里](../cmake_py_gcc_g++) 

具体使用方法，请查阅原作者的github仓库

以下是我自己的补充内容：

---

## 前置条件

需要环境：

* MinGW（务必安装到默认位置`C:/Program Files/`）

需要vscode插件：

* C/C++
* CMake

另外：

* 原作者提到的`Include Autocomplete`插件可以不安装
* **如果安装了`Clang Command Adapter`，需要禁用或删除** 

---

## C或C++语言适配

> **下面两种方案你只能二选一，因为二者有冲突** 

### 1. C++程序的配置

如果你需要编写C++程序（文件后缀为`.cpp`），你只需：

* 将`c_cpp_properties.json`文件中的`"compilerPath"`字段后面的路径改成你的`MinGW`对应的`g++.exe`所在目录（需要精确到`/g++.exe`），如果上一步中你安装到了推荐的默认位置，则不需要这一步骤。

### 2. C程序的配置

* 由于时间原因，我没有尝试，你可以根据gcc/g++方式编译的[README](./README-gcc.md)和[配置文件](../gcc_g++)自行修改

---

## 自定义代码格式化风格（可选）

在`settings.json`文件中的`"C_Cpp.clang_format_fallbackStyle"`字段后面，按照自己的需要进行修改

如果需要默认风格，请将此字段注释掉或删除

更改代码风格入门：

* （科学上网）https://stackoverflow.com/questions/46111834/format-curly-braces-on-same-line-in-c-vscode 
* （科学上网）https://medium.com/@zamhuang/vscode-%E5%A6%82%E4%BD%95%E5%9C%A8-vscode-%E4%B8%8A%E8%87%AA%E5%AE%9A%E7%BE%A9-c-%E7%9A%84-coding-style-c8eb199c57ce 

---

## 注意事项

* 工作区文件夹（也就是目前的`cmakepygccgpp`）不能含有下划线（因为`build.py`中含有正则表达式，可能导致不匹配的问题）
* 工作区和文件的路径不能含有中文
* `clean_workspace_exe.bat`用于清除你不想要的`.exe`文件

---

## 使用方法：

`ctrl + shift + P`，输入`tasks`，选择`Run Task`，然后根据原作者的说明，选择你需要执行的task。

包括以下`task`：

![tasks](./img/Snipaste_2020-09-13_21-12-22.png)

如果你需要调试，直接打好断点，按`F5`即可

---


## 参考

* https://github.com/hysonger/VSCode-CPP-Template
