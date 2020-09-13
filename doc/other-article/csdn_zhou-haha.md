原作者：https://blog.csdn.net/weixin_44049923/article/details/103619882

---

# VScode配置C/C++编程总结（GCC+Clang+CMake）

VScode配置C/C++编程总结（GCC+Clang+CMake）
自己存下档纪念一下2019.12.18

## Visual Studio Code

VScode全称Visual Studio Code，是微软开发的一款轻量代码编辑器（宇宙第一代码编辑器！！），支持多个平台，Windows、Linux、OS X。功能强大，支持多种语言，还有很多非常棒的插件，具体不在多说。
上图
![官网图片](https://img-blog.csdnimg.cn/20191219184505703.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDA0OTkyMw==,size_16,color_FFFFFF,t_70)
官网：[https://code.visualstudio.com](https://code.visualstudio.com/)
中文语言包：软件插件有

### 初接触VScode

刚刚开始知道这个软件还是上课的时候，听到老师讲，然后马上就下载了来试一下
（之前也有接触过**VS2019**，不过用的少，用的**Dev**）后来学**Java**，用的就更少了。偶然听到这个，心血来潮就想试一下。
软件安装很简单，和普通软件一样，比其他**IDE**安装的时候还要容易点。
听说这个能支持多种语言，于是我直接就拿着我最近刚用Eclipse做好的项目丢进去跑了一下，开头总是艰辛的，微软的软件用起来还是有点操作的，不过还好，很快搞定了，Java十分简单，装个插件，其他全部他自己帮你完成，很快**运行-调试-成功**！不过出现了中文乱码（GBK和UTF-8的问题）
一个项目跑下来，给我的整体感觉就是，太便捷了，运行和调试直接就在**main**的旁边，不记得快捷键都能用。页面很美观，而且有个很棒的功能就是可以**分屏同时编辑**同一个文件！！
当然这些都不足以成为我选择它的原因，最重要的原因是太**轻便**了（原谅我想不到什么词来形容），对比eclipse和VS，打开速度飞快，**占用内存小**，而且支持多种语言，**页面美观**……

### 配置C/C++环境

为了使用VScode，我也开始学习如何使用，Java不用怎么配置，插件一装就能编程，很方便。
但是C和C++就不是这样子了，没办法，课程需要
有人问我那为什么不用其他编译器，说白了，我就是馋它身子 （`内存小，速度快，美观`）

**C++环境配置（MinGW64）**
不懂就问，万能的百度，什么都有。果不其然，收到一堆关于如何配置环境的，我随便点了一个别人的博客，照着博客一路做下去，最后测试，GG没用，一堆看不懂的提示。之后又找，这次学乖了，找最新日期的，免得版本什么的不兼容，再试了一次，还是不行，终于再一次搜索中我看到，查阅**官网**。最后照着官网的做，终于成功了。在这里给大家提个醒，配置环境，软件使用，**官方文档**才是最有用的
![不学无术](https://img-blog.csdnimg.cn/20191219193901821.jpg#pic_center)
官方教程：[Get Started with C++ and Mingw-w64 in Visual Studio Code](https://code.visualstudio.com/docs/cpp/config-mingw)
我这里也简单总结一下配置过程
必要工具：**MinGW64**，VScode插件：**C/C++**。注意一定是有64的，没有64的是旧版本，听说已经不在更新，MinGW也可以，不过64更好用。
地址：[source](https://sourceforge.net/projects/mingw-w64/files/)
注意选择离线版本（我国“网络”问题），我选择的是最新的**MinGW-W64 GCC-8.1.0** `x86_64-posix-seh`版本
（本人win10-64位，32位也是下这个64的）里面**posix**和**win32**的区别就是取决你是否要跨平台使用（网上大佬这么讲），**sjlj**和**seh**的区别的话建议百度，是异常处理方式的问题。这里有个几个大佬的参考可以看看
MinGW和MinGW64：
[[科普\]MinGW vs MinGW-W64及其它 - foo__hack](https://www.cnblogs.com/foohack/p/3877276.html)
sjlj和seh的区别：
[What is difference between sjlj vs dwarf vs seh?](http://www.it1352.com/457150.html)
[MingGW64 下载多个版本区别 - 夜鸥 PCYO](https://www.pcyo.cn/linux/20181212/216.html)

继续配置，下载下来的离线包解压到电脑，我选择解压到D盘根目录，即 `D:/mingw64`，装好把环境加到系统去，系统-属性-高级系统设置-环境变量-系统变量里的Path，编辑，添加，输入mingw64/bin的目录，我的就是 `D:\mingw64\bin`，弄好powershell或者cmd输gcc -v测试一下
**MinGW**是干什么的呢，简单来讲，VScode只是一个编辑器，没有编译的功能，这个就是一个**编译器**，我们集成GCC到VScode里面去

**VScode里配置过程，重点，最麻烦也是这里**

按照官网的教程走，软件外面新建一个文件夹作为工作区，用VScode打开它，创建一个`.cpp`文件，随便输内容，比如最简单的`helloworld.cpp`

```cpp
/*helloworld.cpp*/
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello world!" << endl;
    system("pause down");
}
12345678
```

保存好之后在工作区内新建一个`.vscode`文件夹
Ctrl+shift+P后输入C/C++去到编辑设置，照着教程修改，`compilerPath`改成你目录下的`/mingw64/bin/g++.exe`C语言的话就是`gcc.exe`

这步不理他也可以，只是为了方便自动生成`c_cpp_properties.json`文件而已

然后在.`vscode`文件夹创建三个文件，建议后面步骤照着官网来，我之前照着别人的文件复制过去总有一些问题，或者过时的内容，导致无法使用。这里我也给出我的代码，一些在官网的内容上修改了一下，总而言之就是更好用了
`tasks.json`，解释一下，这个是（task）任务配置，我理解的话，这个就是编译过程配置
实际过程相当于在cmd或者powershell直接输命令`g++ -g 源代码.cpp -o 文件名.exe`-o是输出的意思

```javascript
{
    "version": "2.0.0",
    "tasks": [
      {
        "label": "build",
        "type": "shell",
        "command": "g++",
        "args": ["-g", "${file}",  "-o","${fileBasenameNoExtension}.exe"],
        "group": {
          "kind": "build",
          "isDefault": true
        }
      }
    ]
  }
```

`launch.json`这个是调试配置，也就是用**gdb**来调试`program` 按照`args`参数执行命令

```javascript
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
      {
        "name": "(gdb) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceFolder}/${fileBasenameNoExtension}.exe",//要调试的文件
        "args": [],//参数设置，默认不理
        "stopAtEntry": false,//true入口暂停，main一开始就暂停，改为false
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": true,//外部控制台显示，false则显示在VScode里
        "MIMode": "gdb",
        "miDebuggerPath": "D:/mingw64/bin/gdb.exe",//调试使用,自己用的时候路径要改
        "setupCommands": [
          {
            "description": "Enable pretty-printing for gdb",
            "text": "-enable-pretty-printing",
            "ignoreFailures": true
          }
        ],
        "preLaunchTask": "build" // 调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
      }
    ]
  }
```

`c_cpp_properties.json`插件设置，VScode自己生成的就可以了，只用把`compilerPath`改了就能用

```javascript
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "windowsSdkVersion": "10.0.17763.0",
            "compilerPath": "D:\\mingw64\\bin\\g++.exe",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "gcc-x64"
        }
    ],
    "version": 4
}
```

有些教程可能还叫你设置`settings.json`，那个可设可不设，如果有的话记得相关参数名称要和自己三个文件对应。
这三个文件配置好之后，基本的C/C++环境也算配置成功了，至少基础的功能实现肯定没问题
Ctrl+shift+B执行*build*任务（`task.json`里的label，可自定义）,这就是调用GCC完成编译的过程

>  Executing task: g++ -g e:\Coding\VScodeC++\projects\helloworld\helloworld.cpp -o helloworld.exe <
>
> 终端将被任务重用，按任意键关闭。

编译好可以看到文件夹下已经生成了对应文件名的可执行文件`.exe`，这时候可以在软件外打开测试，也可以进行调试，按`F5`进行调试，效果一样，配置完成。

这里小总结一下就是，配置这个按照官网教程配置绝对是最好的，网上的教程说不准什么时候就过时了，或者软件更新了，插件更新了，都有可能造成配置失败，英文像我一样不好的建议开两个网页一个原文一个翻译着看，会理解更深。

---

## clang和多功能插件

用了一段时间的VScode后，我也开始让自己coding的过程更加愉快，于是就捕获了一堆插件

- **C/C++** // 编译的基本插件
- **CodeRunner**// 能直接单文件编译的插件，几乎不用配置
- **Bracket Pair Colorizer 2**// 彩虹花括号，谁用都说好
- **TabNine**// 代码自动补全工具，C/C++自带，不过带上这个也不错
- **OneDarkPro**// 下面都是一些主题，图标，CSS那个我用来改主题用
- **MonokaiPro**
- **background-cover**
- **Custom CSS and JS Loader**
- **SynthWave '84**
  学会了代码格式化，*不学无术的泪水*（不好意思，计算机专业读了一年才知道有这种东西），头文件的编写，调试断点的使用，堆栈会看一点，知道GCC的一些语法，配置需要，弄着弄着就学到了。当然还有现在主要在上的课程——数据结构，基本书上的都学完了，最近刚刚做了一个平衡二叉树的接口，之后看看用无向图做课设看看，*要考试了！！QAQ*
  *2019.12.21继续写*
  VScode的一些操作基本学会了之后，我就开始延伸了，一天偶然在知乎上看到一篇文章
  [Clang 比 GCC 好在哪里？](https://www.zhihu.com/question/20235742)
  然后就开始准备配置clang
  [Visual Studio Code 如何编写运行 C、C++ 程序？](https://www.zhihu.com/question/30315894)
  上面一个知乎的回答写的很详细，亲测基本没问题，不过在有些地方我配置不好自己修改了一下
  不过还是自己总结一下步骤
  1.**MinGW64**，这个只用来提供库文件，clang自己没有
  2.下载**clang**，[LLVM Download Page](http://releases.llvm.org/download.html)，我下的是 **Pre-Built Binaries** 中的 **Windows (64-bit)**，一样离线下载，安装的时候·`path`加进去，没有加安装后自己改，我的默认是`C:\Program Files\LLVM\bin`，装好clang -v测试
  3.**C/C++ Clang Command Adapter**插件安装，这里和知乎那个不同，那个插件我用的有点点问题，静态检测找不到头文件，要用那个的话只能把插件的错误提示不用，用**C/C++** 自带那个
  4.然后还是同样配置四个文件，之前配三个，这个有些设置，所以`settings.json`也要设置

`launch.json`调试文件基本和之前没有任何差别，以示区分我改了编译的label

```javascript
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
      {
        "name": "(gdb) Launch",
        "type": "cppdbg",
        "request": "launch",
        "program": "${workspaceFolder}/${fileBasenameNoExtension}.exe",
        "args": [],
        "stopAtEntry": false,
        "cwd": "${workspaceFolder}",
        "environment": [],
        "externalConsole": true,
        "MIMode": "gdb",
        "miDebuggerPath": "D:\\mingw64\\bin\\gdb.exe",
        "setupCommands": [
          {
            "description": "Enable pretty-printing for gdb",
            "text": "-enable-pretty-printing",
            "ignoreFailures": true
          }
        ],
        "preLaunchTask": "Compile" // 调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
      }
    ]
  }
```
```json
tasks.json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Compile",
      "type": "shell",
      "command": "clang++",
      "args": [
        "-g",
        "${file}",
        "-o",
        "${fileBasenameNoExtension}.exe",
        "-I",
        "${workspaceFolder}/include", // 我有自己编写的头文件在./include文件夹下，所以包含
        "-g", // 生成和调试有关的信息
        "-Wall", // 开启额外警告
        "-static-libgcc", // 静态链接libgcc，一般都会加上
        "--target=x86_64-w64-mingw", // clang的默认target为msvc，不加这一条就会找不到头文件；用gcc或者Linux则掉这一条
        "-std=c++17", // C++最新标准为c++17，或根据自己的需要进行修改
      ],
      "group": {
        "kind": "build",
        "isDefault": true //ctrl+shift+B快捷键开启 
      },
      "presentation": {
        "echo": true,
        "reveal": "always", // 执行任务时是否跳转到终端面板，可以为always，silent，never。具体参见VSC的文档
        "focus": false, // 设为true后可以使执行task时焦点聚集在终端，但对编译C/C++来说，设为true没有意义
        "panel": "shared" // 不同的文件的编译信息共享一个终端面板
    },
    }
  ]
}
```
```json
c_cpp_properties.json
{
    "configurations": [
        {
            "name": "Win32",
            "includePath": [
                "${workspaceFolder}",
                "${workspaceFolder}/**",
                "${workspaceFolder}/include/**"
            
            ],
            "browse": {
                "path": [
                    "${workspaceFolder}",
                    "${workspaceFolder}/**",
                    "${workspaceFolder}/include/**"
                
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            },
            "defines": [
                "_DEBUG",
                "UNICODE",
                "_UNICODE"
            ],
            "windowsSdkVersion": "10.0.17763.0",
            "compilerPath": "D:/mingw64/bin/g++.exe",
            "cStandard": "c11",
            "cppStandard": "c++17",
            "intelliSenseMode": "clang-x64"
        }
    ],
    "version": 4
}
```
```json
settings.json
{
    "files.associations": {
        "vector": "cpp",
        "iostream": "cpp",
        "cstdio": "cpp",
        "new": "cpp",
        "queue": "cpp",
        "array": "cpp",
        "*.tcc": "cpp",
        "deque": "cpp",
        "string": "cpp",
        "unordered_map": "cpp",
        "memory_resource": "cpp",
        "optional": "cpp",
        "string_view": "cpp",
        "algorithm": "cpp",
        "memory": "cpp",
        "initializer_list": "cpp",
        "type_traits": "cpp",
        "utility": "cpp",
        "ostream": "cpp"
    },
    "C_Cpp.clang_format_sortIncludes": true, // 格式化时调整include的顺序（按字母排序）
    "clang.cflags": [ // 控制c语言静态检测的参数
        "--target=x86_64-w64-mingw",
        "-I",
        "./include/**",
        "-std=c11",
        "-Wall"
    ],
    "clang.cxxflags": [ // 控制c++静态检测时的参数
        "--target=x86_64-w64-mingw", // clang另一个插件无法更改这个，所以头文件找不到报错
        "-I",
        "./include/**",  // 自己写头文件的时候这里要改，包含进去，不然静态检测会检测不到头文件
        "-std=c++17",
        "-Wall"
    ],
    "clang.completion.enable": true
}
```

* 这里补充一点，我前几天配置最新标准还是C++17，不过最新的已经是C++20了，这里对应改一下就好，记得C/C++插件要更新，不然不支持C++20，如果改了用不了那改回17

这样配置好就能正常使用了，有部分设置个性化自行选择修改。比如调试和编译分开，下面是我编译的显示

> Executing task: clang++ -g e:\Coding\VScodeC++\projects\testclang\main.cpp -o main.exe -I E:\Coding\VScodeC++\projects\testclang/include -g -Wall -static-libgcc --target=x86_64-w64-mingw -std=c++17 <
>
> 终端将被任务重用，按任意键关闭。

这里还补充讲一下**CodeRunnder** clang的设置（默认GCC可以直接运行），其实就是设置固定命令参数，以下参考上面**知乎回答**

```javascript
    "code-runner.runInTerminal": true, // 设置成false会在“输出”中输出，无法输入
    "code-runner.executorMap": {
        "c": "cd $dir && clang '$fileName' -o '$fileNameWithoutExt.exe' -I './include/' -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c11 && &'$dir$fileNameWithoutExt'",
        "cpp": "cd $dir && clang++ '$fileName' -o '$fileNameWithoutExt.exe' -I './include/' -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c++17 && &'$dir$fileNameWithoutExt'"
        // "c": "cd $dir && clang $fileName -o $fileNameWithoutExt.exe -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c11 && $dir$fileNameWithoutExt",
        // "cpp": "cd $dir && clang++ $fileName -o $fileNameWithoutExt.exe -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c++17 && $dir$fileNameWithoutExt"
    }, // 控制Code Runner命令；未注释的仅适用于PowerShell（Win10默认），文件名中有空格也可以编译运行；注释掉的适用于cmd（win7默认），也适用于PS，文件名中有空格时无法运行
    "code-runner.saveFileBeforeRun": true, // run code前保存
    "code-runner.preserveFocus": true, // 若为false，run code后光标会聚焦到终端上。如果需要频繁输入数据可设为false
    "code-runner.clearPreviousOutput": false, // 每次run code前清空属于code runner的终端消息，默认false
    "code-runner.ignoreSelection": true, // 默认为false，效果是鼠标选中一块代码后可以单独执行，但C是编译型语言，不适合这样用
```

## CMake

配置clang，被头文件的事情整的头晕眼花，总是提示报错，有自己的头文件，项目文件夹里还有多个子目录的，自己每次都去改配置就很难受，于是我也听说了一个叫**CMake**的东西，说实话对这个东西我其实到现在还不是那么理解，原理就是按照CMakeLists.txt来对你的项目进行编译调试，和一些编译器会生成的**makefile**差不多，但是**CMake**更强大，对不起，CMake我都不会，菜醒
[CMake 入门实战](https://www.hahack.com/codes/cmake/#) 这里有一篇介绍CMake如何使用的，我觉得还算容易看懂的，建议先看看。

同样的，总结我的安装过程
1.**MinGW64**下载安装，和之前一样
2.**CMake**最新版下载安装 https://cmake.org/download/安装的时候一样添加环境，忘记勾选之后添加，我的是`C:\Program Files\CMake\bin`,cmake -version测试
3.VScode装插件，**CMake**和**CMake Tools**
*其实装好上面两个插件之后，他就会自动配置生成，这样其实就能用了，不过还是配置一下*
如果有问题，把MinGW64目录下的“mingw32-make.exe”重命名为"make.exe，正常来说也要这样好一点
4.自动生成的时候要选工具链Kit，，如果没有Ctrl+shift+P输入`CMake:Select a Kit`，默认会出现你的GCC，可以直接选择，选好就直接能用，如果多目录，我测试重新生成就好了，如果自己写的头文件找不到就要改一下配置了。我因为改用clang++来编译，所以配置改了一点

原理我也很难讲得很清楚，直接贴代码
`CMakeLists.txt`

```javascript
#cmake版本
cmake_minimum_required(VERSION 3.0.0)
project(AVLTree-zhouhl VERSION 0.1.0)

include(CTest)
enable_testing()

set(CMAKE_CXX_COMPILER "clang++")
set (CMAKE_CXX_FLAGS  "-g -Wall -static-libgcc --target=x86_64-w64-mingw -std=c++17")
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

```

其他配置文件和只用GCC差不多，只有tasks改了，所以我也一起发出来

`tasks.json`

```javascript
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Compile",
      "type": "shell",
      "command": "cmake --build ${workspaceFolder}\\build --config Debug --target all -- -j 10", // cmake指令
      "args": [

      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "echo": true,
        "reveal": "always", // 执行任务时是否跳转到终端面板，可以为always，silent，never。具体参见VSC的文档
        "focus": false, // 设为true后可以使执行task时焦点聚集在终端，但对编译C/C++来说，设为true没有意义
        "panel": "shared" // 不同的文件的编译信息共享一个终端面板
    },
    }
  ]
}

```

---

到这里基本上我用VScode配置C++环境用GCC+Clang+CMake的总结就到这里，如果C的话只要对应改一下g++为gcc，clang++改成clang就行。总体来讲，配置好之后还是挺方便的，不过CMake有点时候时候还是相对复杂（太高级了），我总结的话，就是配置这些东西，最好都去学一下相关语法，这样配置起来才知道是什么东西，至于那种万用模板，我是没找到了，如果有大佬找到了，私信给一份，不胜感激！

这篇博客吧，是我的第一篇博客，也没啥，其实算是对自己一个学习的总结吧，也是以防之后自己又要配环境不会配。这篇文章我还附上了链接，有别人的博客，有官方的解释，也有知乎的回答等等，对我的帮助都很大，感谢这些作者。
最后，如果你看到这篇文章，并且对你有帮助的话，那十分荣幸，以上都是我自己测试成功的，不敢说是教程，但是照着来应该能正常使用了。不说了不说了，要复习了。