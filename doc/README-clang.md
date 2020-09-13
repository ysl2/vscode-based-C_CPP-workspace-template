这是clang/clang++的配置方式，相应的工作区文件在[这里](../clang_clang++) 

通过这种方式，你将可以完成：

* 单文件的编译、运行、调试

你将无法完成：

* 多文件的编译、运行、调试
* 控制台对中文字符集的支持

---

## 前置条件

需要环境：

* LLVM（请务必安装到默认位置`C:/Program Files/`，并加入系统环境变量）
* MinGW（将MinGW文件夹中的所有内容合并到LLVM的目录下）

需要vscode插件：

* C/C++
* Code Runner
* Clang Command Adapter

---

## C或C++语言适配

> **下面两种方案你只能二选一，因为二者有冲突** 

### 1. C++程序的配置

如果你需要编写C++程序（文件后缀为`.cpp`），你什么都不用改，可以直接使用。前提是你完全按照上面的步骤做了。

### 2. C程序的配置

如果你需要写C语言程序（文件后缀为`.c`），你需要：

* 将`c_cpp_properties.json`文件中的`"compilerPath"`字段后面的路径改成你的`LLVM`对应的`gcc.exe`文件所在的目录（需要精确到`/gcc.exe`）
* 将`tasks.json`文件中的`"command"`字段后面的`"clang++"`改为`"clang"`，`"args"`字段中的`"-std=c++14"`改为`"-std=c11"`

---

## 自定义代码格式化风格（可选）

在`settings.json`文件中的`"C_Cpp.clang_format_fallbackStyle"`字段后面，按照自己的需要进行修改

如果需要默认风格，请将此字段注释掉或删除

更改代码风格入门：

* （科学上网）https://stackoverflow.com/questions/46111834/format-curly-braces-on-same-line-in-c-vscode 
* （科学上网）https://medium.com/@zamhuang/vscode-%E5%A6%82%E4%BD%95%E5%9C%A8-vscode-%E4%B8%8A%E8%87%AA%E5%AE%9A%E7%BE%A9-c-%E7%9A%84-coding-style-c8eb199c57ce 

---

## 注意事项

* 工作区和文件的路径不能含有中文
* `clean_workspace_exe.bat`用于清除你不想要的`.exe`文件

---


## 参考

* https://www.zhihu.com/question/30315894/answer/154979413

