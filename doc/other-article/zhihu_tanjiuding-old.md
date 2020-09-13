作者：谭九鼎

链接：https://www.zhihu.com/question/30315894/answer/154979413

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## 0. 前言

本文面向初学者，但是**不适合还在学写Hello World级别的初学者**。阅读本文能在一定程度上了解程序编译的知识，以及使用VS Code的知识。

本文大部分内容都可从VS Code官方文档：[C++ programming with Visual Studio Code](http://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/languages/cpp) 以及各个扩展的文档中获得，并且他们还会进行更新（本文也进行过几次重大更新）。如果你想更深入了解，可以去看。其实本文基本上是由不断地尝试得出来的，如果有错误可以指出。

我的环境：64位Windows 10。32位Win在某些地方需要修改，不过本文没有提；Linux下也有许多不同，仅供参考。

最终效果：**实时显示编译阶段的错误**、格式化代码、进行单文件的编译与调试。

## 1. 环境的准备

VSC的官网、下载、安装，我就不多说了。VSC只是一个**编辑器**(editor)，不是IDE(集成开发环境)，不含**编译器**(compiler)和许多其它功能，所以编译器要自己装好。

其实MinGW和MinGW-w64只是名字像，它们是两个不同的项目。为了方便，本文中的MinGW指的其实都是MinGW-w64。MinGW本身已经很久没有更新了，故**不推荐**。下载以下两个程序（都要）：

- [LLVM Download Page](http://link.zhihu.com/?target=http%3A//releases.llvm.org/download.html) 在此页面下载Clang。选 Pre-Built Binaries 中的 Windows (64-bit)，**不需要下.sig文件**
- [MinGW-w64 - for 32 and 64 bit Windows](http://link.zhihu.com/?target=https%3A//sourceforge.net/projects/mingw-w64/files/) 在此页面下载 MinGW-w64，往下稍微翻一下，选最新版本中的`x86_64-posix-seh`。最好**不要用** *Download Latest Version*，这个是在线安装包，有可能因为国内的“网络环境”下载失败。如果浏览器还是下载失败就换迅雷下，还失败，那就使用能访问Google的那种方法下。

安装Clang：添加环境变量时，选 *Add LLVM to the system PATH for all users*（即第二项，不过第三项也差不多）；路径我填的是 *C:\LLVM*，也可以保持默认或者自己改。

安装MinGW-w64：下下来的是一个7z的压缩包，随便解压到哪，把东西全部复制（或者直接剪切）到Clang的文件夹里去（除非你有自己的想法），它们会无冲突合并，然后就可以把它删了：

[![img](https://camo.githubusercontent.com/87af8bbbe636b7a7acffe1322a9fd39788897741/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d64643834366332363039313631633132303234343435313436663261343037355f622e6a7067)](https://camo.githubusercontent.com/87af8bbbe636b7a7acffe1322a9fd39788897741/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d64643834366332363039313631633132303234343435313436663261343037355f622e6a7067)[![img](https://camo.githubusercontent.com/7e82732f048785e7bd584febe1a324125c9ac9b8/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d64643834366332363039313631633132303234343435313436663261343037355f68642e6a7067)](https://camo.githubusercontent.com/7e82732f048785e7bd584febe1a324125c9ac9b8/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d64643834366332363039313631633132303234343435313436663261343037355f68642e6a7067)

### 验证

运行cmd，输clang或gcc，应该会提示 *no input files* 而不是“不是内部命令或外部命令”或者“无法将“clang”项识别为 cmdlet、函数、脚本文件或可运行程序的名称”，见下图。如果是“不是内部命令或外部命令”，说明clang.exe在的文件夹（我图里的是 *C:\LLVM\bin*）没有在环境变量中，要加到Path里才行。如果加了还是这样，重启。

输`clang -v`或`gcc -v`可以显示出各自的版本。如果显示出来的版本与你刚下的不同/更老，说明Path里原本有老版本的编译器，可能是安装其它IDE时装上的。则需要去掉原来的。

这两项验证**一定要符合**。如果你不知道怎么修改环境变量可以自己百度或者b站搜“环境变量”看视频（大多不是C的但是区别不大）。

[![img](https://camo.githubusercontent.com/50b7e2eebf0a2f571a52dec4c5522db5d8f53f0b/68747470733a2f2f706963342e7a68696d672e636f6d2f76322d30396633626134373662646564653138653961396162333661653864373166335f622e6a7067)](https://camo.githubusercontent.com/50b7e2eebf0a2f571a52dec4c5522db5d8f53f0b/68747470733a2f2f706963342e7a68696d672e636f6d2f76322d30396633626134373662646564653138653961396162333661653864373166335f622e6a7067)[![img](https://camo.githubusercontent.com/358d8d0440a473c40ed588f2f522af55c15e4ca1/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d30396633626134373662646564653138653961396162333661653864373166335f68642e6a7067)](https://camo.githubusercontent.com/358d8d0440a473c40ed588f2f522af55c15e4ca1/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d30396633626134373662646564653138653961396162333661653864373166335f68642e6a7067)

[![img](https://camo.githubusercontent.com/b1a1b3a1056d376a3317263546ba1131d7b55212/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d65313462623933303739633433623364613138313531323335336666663465355f622e6a7067)](https://camo.githubusercontent.com/b1a1b3a1056d376a3317263546ba1131d7b55212/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d65313462623933303739633433623364613138313531323335336666663465355f622e6a7067)[![img](https://camo.githubusercontent.com/00303a99b7eca55fd9f793fb96319ba40155f185/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d65313462623933303739633433623364613138313531323335336666663465355f68642e6a7067)](https://camo.githubusercontent.com/00303a99b7eca55fd9f793fb96319ba40155f185/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d65313462623933303739633433623364613138313531323335336666663465355f68642e6a7067)输入gcc -v的最后一行输出，版本要和你自己下的对应，要有x86_64和seh；sjlj是以前的，图懒得改了

### 安装扩展(extension)

必装：

- C/C++：又名 cpptools，提供Debug和Format功能
- C/C++ Clang Command Adapter：提供静态检测（Lint）功能
- Code Runner：右键即可编译运行单文件，很方便；但无法Dubug

其他可选扩展：

- Bracket Pair Colorizer：彩虹花括号
- Include Autocomplete：提供头文件名字的补全，不过用处不大；而且其实现在cpptools已经自带这个功能了，但本文不使用它的补全
- C/C++ Snippets：Snippets即重用代码块，效果自己百度；这个扩展安装量虽高，不过个人感觉用处实在不大，你也可以选择其他的Snippets扩展甚至自己定义
- One Dark Pro：大概是VS Code安装量最高的主题
- vscode-clangd：这个和Adapter二选一，出得比Adapter晚，下载量也低，但却是llvm官方出的。出现问题时可以换着试试
- Clang-Format：只有想自定义代码风格时才装，比如大括号不换行。需要另外学习如何使用

不建议/不需要装的扩展：

- GBKtoUTF8：把GBK编码的文档转换成UTF8编码的。此扩展可能有严重的bug。
- C++ Intellisense：用的是gtags，本文第一个版本的选择。效果非常非常一般。

### FAQ

- Q: 为什么要装Clang? A: 错误提示更友好。以及：[Clang 比 GCC 好在哪里？](https://www.zhihu.com/question/20235742)
- Q: Clang怎么读？ A: 正确答案是/ˈklæŋ/，即c发"可"的音；不过实际还是以双方都理解为基础，比如平常把SQL说成circle也是能理解的
- Q: 为什么既要装Clang又要装MinGW? A: Clang没有stdio.h等头文件。至于为什么没有，我就不知道了；也许就是下一点的原因
- Q: MSVC integration install failed / unable to find a Visual Studio installation... A: Win下的Clang默认用的是MSVC的后端。如果完全按照本文接下来的操作，**不用管这个提示**
- 可选阅读：[[原创\][科普]MinGW vs MinGW-W64及其它](http://link.zhihu.com/?target=http%3A//tieba.baidu.com/p/3186234212)、[What is difference between sjlj vs dwarf vs seh?](http://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/15670169/what-is-difference-between-sjlj-vs-dwarf-vs-seh)

## 2. 配置四个.json文件

先创建一个你打算存放代码的文件夹（称作工作区），**路径不能含有中文和引号**，最好不要有空格。C和C++需要分别建立不同的工作区，除非你懂得下面json文件的某些选项，则可以做到一个工作区使用不同的build task。

打开VSC，**选打开文件夹**，不要选“添加工作区文件夹”，理由见上一句。点新建文件夹，名称为 *.vscode*。这样操作的原因是Windows的Explorer不允许创建的文件夹第一个字符是点（但据说1809的下一个大版本支持了）。然后创建 launch.json，tasks.json，settings.json，c_cpp_properties.json**放到.vscode文件夹下**，效果图：

[![img](https://camo.githubusercontent.com/d025c4cefd11b7549803e0cc7b457b1eeb24b31a/68747470733a2f2f706963342e7a68696d672e636f6d2f76322d66323538323536616534326230346533306139393666383661333637366161335f622e6a7067)](https://camo.githubusercontent.com/d025c4cefd11b7549803e0cc7b457b1eeb24b31a/68747470733a2f2f706963342e7a68696d672e636f6d2f76322d66323538323536616534326230346533306139393666383661333637366161335f622e6a7067)[![img](https://camo.githubusercontent.com/870cab73a24f28fa7159ab4b7bac6c23eae558f9/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d66323538323536616534326230346533306139393666383661333637366161335f68642e6a7067)](https://camo.githubusercontent.com/870cab73a24f28fa7159ab4b7bac6c23eae558f9/68747470733a2f2f706963342e7a68696d672e636f6d2f38302f76322d66323538323536616534326230346533306139393666383661333637366161335f68642e6a7067)

[![img](https://camo.githubusercontent.com/4f40dddd9c53ef58857ef653dad50bceecf251c6/68747470733a2f2f706963312e7a68696d672e636f6d2f76322d35323666343638383861646666653562313635663236323434643139336365385f622e6a7067)](https://camo.githubusercontent.com/4f40dddd9c53ef58857ef653dad50bceecf251c6/68747470733a2f2f706963312e7a68696d672e636f6d2f76322d35323666343638383861646666653562313635663236323434643139336365385f622e6a7067)[![img](https://camo.githubusercontent.com/1792d8b4b5a5bc194415534917dfbf74119d05de/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d35323666343638383861646666653562313635663236323434643139336365385f68642e6a7067)](https://camo.githubusercontent.com/1792d8b4b5a5bc194415534917dfbf74119d05de/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d35323666343638383861646666653562313635663236323434643139336365385f68642e6a7067)

复制以下代码出来后，知乎会自动在前面加上几行保留所有权利的字，实际使用的时候肯定要删了的。每个小节的开头都有选项说明。特别提示：默认F5只能编译C，**如果你要调试C++，必需改tasks.json**，具体参见小节说明。

### launch.json代码

*stopAtEntry*和*externalConsole*可根据自己喜好修改；cwd可以是程序运行时的相对路径，如有需要可以改为*${fileDirname}*（感谢

[@xhx](http://www.zhihu.com/people/dd30faca74afd3e29376d2226d44475d)

）；现在的LLVM带有lldb-vscode这个程序，但我没试过能不能用。其他无需更改。type和request不变色是正常现象。

```
// https://github.com/Microsoft/vscode-cpptools/blob/master/launch.md
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch", // 配置名称，将会在启动配置的下拉菜单中显示
            "type": "cppdbg", // 配置类型，这里只能为cppdbg
            "request": "launch", // 请求配置类型，可以为launch（启动）或attach（附加）
            "program": "${fileDirname}/${fileBasenameNoExtension}.exe", // 将要进行调试的程序的路径
            "args": [], // 程序调试时传递给程序的命令行参数，一般设为空即可
            "stopAtEntry": false, // 设为true时程序将暂停在程序入口处，相当于在main上打断点
            "cwd": "${workspaceFolder}", // 调试程序时的工作目录，此为工作区文件夹；改成${fileDirname}可变为文件所在目录
            "environment": [], // 环境变量
            "externalConsole": true, // 为true时使用单独的cmd窗口，与其它IDE一致；18年10月后设为false可调用VSC内置终端
            "internalConsoleOptions": "neverOpen", // 如果不设为neverOpen，调试时会跳到“调试控制台”选项卡，你应该不需要对gdb手动输命令吧？
            "MIMode": "gdb", // 指定连接的调试器，可以为gdb或lldb。但我没试过lldb
            "miDebuggerPath": "gdb.exe", // 调试器路径，Windows下后缀不能省略，Linux下则不要
            "setupCommands": [ // 用处未知，模板如此
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": false
                }
            ],
            "preLaunchTask": "Compile" // 调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
        }
    ]
}
```

### tasks.json代码

如果是编写C++，编译器需改成clang++；如果想用MinGW就分别是gcc和g++，但注意把--target那条删去。

如果不想要额外警告，把-Wall那一条删去。

reveal可根据自己喜好修改，即使设为never，也只是编译时不跳转到“终端”而已，手动点进去还是可以看到，我个人设为never。

参数的作用我加了注释，还看不懂，百度gcc使用教程。

```
// https://code.visualstudio.com/docs/editor/tasks
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Compile", // 任务名称，与launch.json的preLaunchTask相对应
            "command": "clang", // 要使用的编译器，C++用clang++；如果编译失败，改成gcc或g++试试，还有问题那就是你自己的代码有错误
            "args": [
                "${file}",
                "-o", // 指定输出文件名，不加该参数则默认输出a.exe，Linux下默认a.out
                "${fileDirname}/${fileBasenameNoExtension}.exe",
                "-g", // 生成和调试有关的信息
                "-Wall", // 开启额外警告
                "-static-libgcc", // 静态链接libgcc
                "--target=x86_64-w64-mingw", // clang的默认target为msvc，不加这一条就会找不到头文件；Linux下去掉这一条
                "-std=c11" // C++最新标准为c++17，或根据自己的需要进行修改
            ], // 编译命令参数
            "type": "process", // process是vsc把预定义变量和转义解析后直接全部传给command；shell相当于先打开shell再输入命令，所以args还会经过shell再解析一遍
            "group": {
                "kind": "build",
                "isDefault": true // 设为false可做到一个tasks.json配置多个编译指令，需要自己修改本文件，我这里不多提
            },
            "presentation": {
                "echo": true,
                "reveal": "always", // 在“终端”中显示编译信息的策略，可以为always，silent，never。具体参见VSC的文档
                "focus": false, // 设为true后可以使执行task时焦点聚集在终端，但对编译c和c++来说，设为true没有意义
                "panel": "shared" // 不同的文件的编译信息共享一个终端面板
            }
            // "problemMatcher":"$gcc" // 如果你不使用clang，去掉前面的注释符，并在上一条之后加个逗号。照着我的教程做的不需要改（也可以把这行删去)
        }
    ]
}
```

### settings.json代码

把这个文件里的东西放到“用户设置”里也可以覆盖全局设置，自己进行选择。

Code Runner的命令行和某些选项可以根据自己的需要在此处修改，用法还是参见此扩展的文档和百度gcc使用教程。**Win7**需要改用注释掉的命令行，或者把`terminal.integrated.shell.windows`改为PowerShell。

如果你要使用其他地方的头文件和库文件，需要要往clang.cflags和clang.cxxflags里加`-I`、`-l`和`-L`，用法百度gcc使用教程。

clang的补全，在我过去的测试过程中会让VSC非常卡，但是现在好像没有这个问题了。如果你卡，就把clang的补全关掉，用cpptools的（不需要我指明分别是哪两个吧？）。

Linux下记得去掉code runner和flags的--target，共四个。

感谢

[@Wellin Boss](http://www.zhihu.com/people/e011194994d3415968b3886ade2b588c)

提到的snippetSuggestions。

```
{
    "files.defaultLanguage": "c", // ctrl+N新建文件后默认的语言
    "editor.formatOnType": true, // 输入时就进行格式化，默认触发字符较少，分号可以触发
    "editor.snippetSuggestions": "top", // snippets代码优先显示补全

    "code-runner.runInTerminal": true, // 设置成false会在“输出”中输出，无法输入
    "code-runner.executorMap": {
        "c": "cd $dir && clang '$fileName' -o '$fileNameWithoutExt.exe' -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c11 && &'$dir$fileNameWithoutExt'",
        "cpp": "cd $dir && clang++ '$fileName' -o '$fileNameWithoutExt.exe' -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c++17 && &'$dir$fileNameWithoutExt'"
        // "c": "cd $dir && clang $fileName -o $fileNameWithoutExt.exe -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c11 && $dir$fileNameWithoutExt",
        // "cpp": "cd $dir && clang++ $fileName -o $fileNameWithoutExt.exe -Wall -g -O2 -static-libgcc --target=x86_64-w64-mingw -std=c++17 && $dir$fileNameWithoutExt"
    }, // 控制code runner命令；未注释的仅适用于PowerShell（Win10默认），注释掉的适用于cmd（win7默认）
    "code-runner.saveFileBeforeRun": true, // run code前保存
    "code-runner.preserveFocus": true, // 若为false，run code后光标会聚焦到终端上。如果需要频繁输入数据可设为false
    "code-runner.clearPreviousOutput": false, // 每次run code前清空属于code runner的终端消息
    "code-runner.ignoreSelection": true, // 默认为false，效果是鼠标选中一块代码后可以单独执行，但C是编译型语言，不适合这样用

    "C_Cpp.clang_format_sortIncludes": true, // 格式化时调整include的顺序（按字母排序）
    "C_Cpp.intelliSenseEngine": "Default", // 可以为Default或Tag Parser，后者较老，功能较简单。具体差别参考cpptools扩展文档
    "C_Cpp.errorSquiggles": "Disabled", // 因为有clang的lint，所以关掉
    "C_Cpp.autocomplete": "Disabled", // 因为有clang的补全，所以关掉

    "clang.cflags": [ // 控制c语言静态检测的参数
        "--target=x86_64-w64-mingw",
        "-std=c11",
        "-Wall"
    ],
    "clang.cxxflags": [ // 控制c++静态检测时的参数
        "--target=x86_64-w64-mingw",
        "-std=c++17",
        "-Wall"
    ],
    "clang.completion.enable":true // 效果比cpptools要好
}
```

### c_cpp_properties.json代码

如果你确定不需要使用别人的库，则现在的版本不需要创建这个文件了，扩展会自动使用默认的设置。

如果你自己编写了头文件又不在workspaceFolder下，或是使用别人的库，路径就要加到includePath和browse里（不过还有别的操作要做，见下一大点的多文件编译）。如果需要递归包含，末尾加`/**`

此文件内容来自于[Microsoft/vscode-cpptools](http://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/blob/master/Documentation/LanguageServer/MinGW.md)；这个json不允许有注释（其实按照标准本来就不能有）。

如果没有合并Clang和MinGW，则该文件中的compilerPath**必需**修改成MinGW的**完整**路径，精确到gcc.exe，否则会提示找不到头文件；Linux下是/usr/bin/gcc。

Windows下的目录分隔符为反斜杠，原本应使用两个反斜杠来转义，但直接用斜杠在VS Code中也接受。

> When you set the`compilerPath`property and change`intelliSenseMode`to`clang-x64`(or`gcc-x64`in version 0.18.0 and higher), you no longer need to copy the system include path or defines to`includePath`,`browse.path`, or`defines`to enable IntelliSense to work properly.

```
{
    "configurations": [
        {
            "name": "MinGW",
            "intelliSenseMode": "gcc-x64",
            "compilerPath": "C:/LLVM/bin/gcc.exe",
            "includePath": [
                "${workspaceFolder}"
            ],
            "defines": [],
            "browse": {
                "path": [
                    "${workspaceFolder}"
                ],
                "limitSymbolsToIncludedHeaders": true,
                "databaseFilename": ""
            },
            "cStandard": "c11",
            "cppStandard": "c++17"
        }
    ],
    "version": 4
}
```

为什么要往json里写这么多的东西？因为VSC本身并没有对C语言特别优待，对其他许多语言也是这样。以$开头的是VSC预定义的变量，具体参见：[Variables Reference](http://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/editor/variables-reference)，比如$file在实际运行时会替换成当前打开的文件名。

## 3. 写代码，编译，调试

新建文件后就可以写代码了，c语言源代码后缀是.c，c++是.cpp或.C或.cxx（这也要我教吗……）。代码文件在保存工作区内都可以，可以自己建立文件夹，**不必**放到.vscode文件夹里，**不要含有中文和引号**，最好不要有空格；主要是许多符号是有效的shell语法，不然试试用rm删除一个叫做-rf的文件？

按Alt+Shift+F（或者右键菜单）可以格式化代码。出现Intellisense的时候按tab可以补全代码。

停止输入一小段时间（一秒）后就会有Lint，扩展会给一些建议性的warning（比如声明了变量但不使用），自己清楚就行。如果觉得不爽，也有方法不让它提示，比如去掉-Wall就会少一些。如果还想去掉更多的警告，自己找怎么做，我提示一下：-Wno-...。找好参数后加到clang.cflags、clang.cxxflags和tasks.json的args里。

按ctrl+shift+B单纯编译，按F5为运行并调试（运行前会自动编译）；本来ctrl+F5为运行但不调试，但是在cpptools暂不支持，还是会调试。Follow: [How to launch an application without debugging? · Issue #1201 · Microsoft/vscode-cpptools](http://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/issues/1201)

在写程序初期，我强烈建议**不要把f5当作编译来使用**，因为有的bug只会产生警告，不会阻止编译，但这些东西越早期解决越好。编译信息会在底下的“终端”面板里，如果代码有错误，点进去可以看clang报的信息，但因为有Lint了，所以可以轻松很多。

加断点在列号前面点一下就行，如果想从一开始就停下来，可以加在main函数那里，或者*launch.json*中设置*"stopAtEntry": true*。按f11可以一步一步进行，箭头所指的那行代码就是**下一步要运行的代码**。左边有个调试栏，可以看到变量的值,自动栏没有的可以手动添加表达式；把鼠标放到变量上可以看到变量的值，但是只能识别简单的表达式；栈帧对于观察递归很有用；在某些时候还可以抓取“异常”。

快捷键：[vscode: Visual Studio Code 常用快捷键](http://link.zhihu.com/?target=http%3A//www.cnblogs.com/bindong/p/6045957.html)。英文文档中当然有快捷键的信息，还有Cheet Sheet可以看，而且英文文档会更新。这个单独列出来还是给初学者吧。

中文乱码见第六点。**其它错误先看底下的“某些可能出现的错误”以及看评论区**。

### Code Runner

如果你不需要调试，可以直接右键选run code，或者点右上角的播放按钮。如果在终端里运行，可以输入数据，但是少了显示时间的功能；在“输出”中则上面两项相反。

用它还可以在非工作区内编译运行程序，但executorMap记得放到全局设置里。在终端中按ctrl + c可以终止程序运行。

如果按照我的配置，task和code runner还有一点不同的是working directory。前者是你打开的文件夹，后者是文件所在的文件夹。当然它们也都可以自己修改。

**其实Code Runner只是代替你手动输命令**，功能并不强，算是适用场景不同吧。不要以为run code跑个Hello World很简单，Code Runner就很强，前面那么多配置都是垃圾了。

另外，楼下的答主韩骏就是此插件作者，有事统统找他（滑稽）。

### 多文件编译

如果你想进行少量的多文件编译，C语言直接用`gcc 源文件1.c 源文件2.c 头文件1.h`这样就好，C++类似，其余选项百度gcc怎么用。 如果需要多次编译可以写一个批处理。

如果你想进行大量的多文件编译，请学习如何写makefile或使用cmake。

如果你想使用别人的库，比如ffmpeg，可能需要在命令中指定`-I`、`-l`（小写的L）、`-L`。具体阅读那个库的文档。

这些情况下可以考虑单独建一个工作区，不要和单文件编译的共用；还可能需要需要修改那几个JSON来配置Intellisense。

其实不新建工程(Project)、只是单文件就能调试，是不利于以后使用和理解大型IDE的。不过初学也不用掌握那么多，不要觉得建工程很麻烦、不建工程就能编译很强就是了。

总之这个VSC无关，用其它IDE或是手动编译还是会遇到差不多的问题。自行解决。

### 保存文件夹

如果你用VSC还做别的事（比如写前端），或者有不止一个工作区，可以创建一个快捷方式（右键新建），把工作区路径作为参数传给VSC主程序，还可以加个图标。这操作不难，记得打双引号就行。1.18有了一个窗口多个工作区的功能，“文件”菜单里也有“保存工作区”这个功能，但是我没试过。

[![img](https://camo.githubusercontent.com/7327ffdd05fb5a8447ca210755555fb48d8a7a7d/68747470733a2f2f706963312e7a68696d672e636f6d2f76322d65663864613062666437663565303363666439656430333534633763313965635f622e6a7067)](https://camo.githubusercontent.com/7327ffdd05fb5a8447ca210755555fb48d8a7a7d/68747470733a2f2f706963312e7a68696d672e636f6d2f76322d65663864613062666437663565303363666439656430333534633763313965635f622e6a7067)[![img](https://camo.githubusercontent.com/147ba2732dcd2fde0590242a62e3161b29320d11/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d65663864613062666437663565303363666439656430333534633763313965635f68642e6a7067)](https://camo.githubusercontent.com/147ba2732dcd2fde0590242a62e3161b29320d11/68747470733a2f2f706963312e7a68696d672e636f6d2f38302f76322d65663864613062666437663565303363666439656430333534633763313965635f68642e6a7067)

### 清理临时文件

按照这样配置，长期编译代码下来肯定有一大堆的exe，还可能分散在不同的文件夹里。

可以考虑修改一下json文件，把生成文件的目录指定到一个专门放exe的文件夹里；如果不会，百度gcc使用教程以及看我的json里的注释。或者资源管理器右上角搜索*.exe然后手动删除。

也可也写个bat，放到工作区里，要用的时候右键Run Code：

```
del *.exe /q /s
del tempCodeRunnerFile.c /q /s
del a.out /q /s
del *.o /q /s
```

### 某些可能出现的错误

- 如果你只写了个hello world，不加任何断点，**按f5以后黑框框一闪而过是正常现象**。想让程序暂停运行可以在末尾加上一个或两个getchar();，不明白为什么有时要用两个？去问你们C语言老师；或用system("pause")，或加断点
- 如果你要进行调试，不要开优化。gcc用-Og还可以保留一些调试信息，但clang用了以后就不能用gdb调试了。即使如此我还是在某一次写代码的时候遇到了无法跳入函数的问题，而VS可以跳入
- 重命名文件后，原来已有的Lint还会在问题栏里；修改了文件后断点可能会失效。以及还存在一些其他的像这样的小bug，一般关掉VSC再开就行
- preLaunchTask“Compile”已终止，退出代码为 1：编译有error并且你用的是F5运行的就会有这个提示；如果你点仍然调试，**就会调试上一次编译成功的文件**。其实所有的编译失败都会触发这个错误，出错的返回值是1难道不是常识？所以仅仅告诉我出现了这个提示**根本没用**，因为它的意思就是出错了，没有人能看出原因。这也是为什么我要强烈建议不要把F5当作编译来使用，按F5出了问题，我根本看不出是编译期有问题还是调试期有问题，或是你自己的代码有问题
- 终端将被任务重用，按任意键关闭：听过“按任意键继续”吗？这句话就是这个意思。**这句话比上面那个退出代码为1还要没用**，它根本就不包含任何有效信息，无论成功还是出错都会显示它。所以不要再问这句话“怎么办”了，先学学如何提问
- 无法打开...，找不到文件(file:///build/glibc-OTsEL5/glibc-2.27/...)：我在Linux下遇到了这个问题，下一个glibc放到指定位置就行，`wget http://ftp.gnu.org/gnu/glibc/glibc-2.27.tar.xz`，剩下的就不要问我了。或者参见这个：[Disable "Unable to open file" during debug · Issue #811 · Microsoft/vscode-cpptools](http://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/issues/811%23issuecomment-376658727)
- `libmingw32.a(lib64_libmingw32_a-crt0_c.o):crt0_c.c:(.text.startup+0x2e): undefined reference to 'WinMain'`：这是你自己的代码有问题，没写main函数，或者把main写成了mian
- undefined reference to xxx ... linker command failed：调用了未声明的函数。可能是函数名打错了，或者没有include头文件。总之是你自己的代码有错误。
- ld: cannot open output file ... permission denied：原程序仍在运行（比如死循环），无法被覆盖，任务管理器结束那个进程即可
- MinGW下，监视（Watch）窗口里用strcmp，会导致gdb崩溃退出，原因不明。linux下正常
- 如果还有问题，可以试试改成gcc/g++编译。比如现在`#include `会报`'float.h' file not found`，改成g++后就好了。我觉得这应该是库的bug，反正我是不知道怎么解决

## 4. 其他设置

我的一些其他的设置，用在全局settings.json里，根据自己的情况调整，不需要全部照着我的写。**写完一个以后要打逗号。**

现在的VSC用的是可视化的设置界面，其实原本是手动编辑且出现两列设置的。点击右上角那个花括号就能手动编辑。

```
"editor.fontFamily": "等距更纱黑体 SC", // 控制编辑器字体
"workbench.colorTheme": "One Dark Pro", // 主题
"files.trimTrailingWhitespace": true, // 保存时，删除每一行末尾的空格
"files.insertFinalNewline": true, // 保存后文件最末尾加一行空格
"workbench.colorCustomizations": {
        "activityBar.foreground": "#39C5BB" // 自定义颜色
    },
"git.enabled": false, // 如果你不用git，可以考虑关闭它
"git.ignoreMissingGitWarning": true, // 同上
"editor.minimap.enabled": false, // 我个人不用minimap，就是右边那个东西
"editor.dragAndDrop": false, // 选中文字后，可以拖动它们调整位置。我是不需要
"files.autoGuessEncoding": false, // 启用后，会在打开文件时尝试猜测字符集编码。我关闭的理由见6
"[c]": {
    // "files.encoding": "gbk" // 这样的格式可以对指定后缀的文件应用设置，如果你实在想用gbk，就这样设置吧。cpp同理。
},
"window.zoomLevel": 0.2, // 整体放大
"workbench.settings.useSplitJSON": true, // 恢复手动编辑时的两列设置
```

更纱黑体是楼下B神做的字体，特点是标点好看（误）：[be5invis/Sarasa-Gothic](http://link.zhihu.com/?target=https%3A//github.com/be5invis/Sarasa-Gothic)

Consolas虽然是Windows自带字体中还算行的，但它只有英文字体；微软雅黑虽然是非衬线字体，但它不是等距的，这一点非常不适合编程，等线也不等距；中易宋体……告辞。不下新的字体，其他两大系统我不清楚，Windows下简直没有编程可用的字体。Consolas加雅黑嘛，也还行吧，不过能用更好的干嘛不用呢。

## 6. 关于中文和乱码

VS Code输出中文会出现乱码，很多人都遇到过。这是因为VS Code内部用的是utf-8编码，cmd/PowerShell是gbk编码。直接编译，会把“你好”输出成“浣犲ソ”。Linux就没有这个问题。其它一些测试见：[谭九鼎：C语言与中文的一些测试 (Win, UTF8源码)](https://zhuanlan.zhihu.com/p/71778196)

一种解决方法是用gcc，编译时用*-fexec-charset=GBK*这个参数，生成的程序就是GBK编码的*。*但是本文默认用的clang的execution-charset supports only UTF-8。如果你确定需要写中文，可以自己进行修改。但是Lint仍然可以用clang的。

如果是打开已有的以GBK编码的文件，VS Code默认会以UTF-8编码打开（除非你设置了猜测编码），这样编辑器内的中文就会乱码，不过对于初学C的同学来说，写的代码一般只有注释是中文。此时要点右下角的GBK，选“通过编码重新打开”，选UTF-8即可。GBKtoUTF8这个扩展，理论上如果VSC检测出的是GBK编码的，它就会自动做“以UTF-8格式保存”这个操作；如果VSC没有检测出是GBK编码，它就什么也不会做。但是貌似它有bug，会把当前文件复制一遍插入到光标处，见[VS code 很好用，但是有个恶心的bug，大家谨慎！大神帮解决一下](http://link.zhihu.com/?target=https%3A//tieba.baidu.com/p/5695616350)，所以不推荐使用。

如果你没有注意到一个GBK编码的文件被VSC以UTF-8的编码打开了，又进行了保存，按照我的测试，这文件里的中文应该是找不回来了。这个还是比较危险的。而且如果打开了编码猜测，VSC又猜错了的话……所以我是关闭编码自动猜测的。中文特别少的时候猜错几率很大。

这样做了以后，在含有中文的路径下可以编译，但是仍然不能调试，所以还是把代码放到**不含中文的路径**中吧。这个貌似是gdb的bug，但是优先级极低：[[gdb\] cannot not open source file with Chinese/Unicode characters in path when debugging · Issue #602 · microsoft/vscode-cpptools](http://link.zhihu.com/?target=https%3A//github.com/microsoft/vscode-cpptools/issues/602)

如果把代码文件发给其他用Windows的人，最好转成gbk，否则别人用记事本打开有可能会乱码（不过貌似1709改进了记事本的编码猜测，1803的下一个版本连LF都支持了）。

## 7. 找不到头文件的错误

[![img](https://camo.githubusercontent.com/f8465b253740413a35b2de6e5c57706974941a0a/68747470733a2f2f706963332e7a68696d672e636f6d2f76322d38373730353862653432303865366233363438613164613663656336323035655f622e6a7067)](https://camo.githubusercontent.com/f8465b253740413a35b2de6e5c57706974941a0a/68747470733a2f2f706963332e7a68696d672e636f6d2f76322d38373730353862653432303865366233363438613164613663656336323035655f622e6a7067)[![img](https://camo.githubusercontent.com/bc670c432afca94e540f10475e23f8aa09b9fa2c/68747470733a2f2f706963332e7a68696d672e636f6d2f38302f76322d38373730353862653432303865366233363438613164613663656336323035655f68642e6a7067)](https://camo.githubusercontent.com/bc670c432afca94e540f10475e23f8aa09b9fa2c/68747470733a2f2f706963332e7a68696d672e636f6d2f38302f76322d38373730353862653432303865366233363438613164613663656336323035655f68642e6a7067)

有几位同学遇到了路径设置正确，编译也通过，但是“问题"面板里出现找不到头文件的error。我也遇到过。这个error是cpptools报的。可能的解决方法是把你需要的头文件的路径加到c_cpp_properties.json中，或者你的compilerPath没有设置正确。如果还是解决不了，反正不影响编译，就当做没看到算了。如果你遇到了又解决了可以留言告诉大家。如果是非工作区选c语言或者c++，出现这个错误很正常，因为不满足前提：路径设置正确（没有c_cpp_properties.json）。

**还有一种可能，看评论区BladLust同学的回复。**

另一种问题：

[![img](https://camo.githubusercontent.com/23de4b5094abfbd6f1d0f90ad0641a351f4546c1/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d61376531353738616331643530626362613963636333393836616536303761645f622e6a7067)](https://camo.githubusercontent.com/23de4b5094abfbd6f1d0f90ad0641a351f4546c1/68747470733a2f2f706963322e7a68696d672e636f6d2f76322d61376531353738616331643530626362613963636333393836616536303761645f622e6a7067)[![img](https://camo.githubusercontent.com/d901a21d280127b7d17e7f7a9f57252ccc35594c/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d61376531353738616331643530626362613963636333393836616536303761645f68642e6a7067)](https://camo.githubusercontent.com/d901a21d280127b7d17e7f7a9f57252ccc35594c/68747470733a2f2f706963322e7a68696d672e636f6d2f38302f76322d61376531353738616331643530626362613963636333393836616536303761645f68642e6a7067)

如果是这个错误，这是因为clang的默认target为msvc，需要加--target=x86_64-w64-mingw这个参数才行。这个默认target貌似是写死在源代码里的，反正我找了一圈是没找到正常修改办法，下载clang的源代码，自己改掉，再编译clang本身，也许可以解决。或者装Windows sdk而不使用mingw，这样就符合默认target了，参考第九点。当然最简单的办法就是用gcc。

## 8. 其他

- json是一种数据交换格式，~~大部分是JavaScript的子集~~现在强行变成完全子集了，数据冗余度小。VSC和各个扩展会读取json中的条目，来决定某些功能的行为。这么多条目哪里来的呢？这其实和API差不多。扩展开发者会把允许修改的选项“告诉”VSC，各个扩展的安装页面都有写，VSC又有intellisense，所以其实很容易写。如果是单纯使用json，我觉得就算从来没有见过，边看边猜也能写个大概。又因为扩展开源，你甚至可以去扩展的github页面和开发者聊天。
- Windows 10，默认输入法只有一个微软拼音，按一次shift就能进行中英转换，而为了保持兼容，按ctrl加空格也能进行中英转换，而这个快捷键正是强制触发Intellisense的快捷键。所以，我强烈建议手动添加“英语”语言输入法，写非前端代码时切换到纯英文输入法（win+空格）。这样也可以解决某些游戏需要用到shift键但是同样快捷键冲突的问题。具体操作可以自己百度，也可以看我写的这篇有点复杂的文章：[谭九鼎：Windows 切换显示语言与添加纯英文输入法](https://zhuanlan.zhihu.com/p/62890493)。
- tasks.json中的"problemMatcher":"$gcc"会解析终端中的错误提示，因为已经有Clang的Lint了，就不需要这个；如果用了Clang Command Adapter又打开这个，则会出现双重错误提示。本来1.11就说可以写$gcc的，但当时其实并不支持，现在早就能用了。不过如果要用非预设版本，就需要自己写了。
- 此配置无法使用Bash for Windows或WSL，因为bash中的反斜杠会被识别为换行。cpptools现为launch.json提供了一个*Bash on Windows Launch*的snippets，但是我没有试过如何使用。

## 9. 其他工具链的选择

- 使用MinGW编译但仍用Clang提供Lint：tasks.json的命令行自己改一改，code runner的命令行在settings.json里，自己改。这样可以在终端中输出不乱码，参考第六点。缺点：编译用的不是Clang，编译速度相对慢。Lint可能提示的警告不全，比如Clang给出的"did you mean ..."提示，Lint就可能捕获不到
- MinGW-w64 + 官方扩展：不使用Clang。除了上面做的，tasks.json里problemMatcher打开；settings.json里的东西自己改一改。缺点：Windows下的Lint效果真的真的很差，Linux稍微好一点。感觉相比上一个方案没有优点？
- Windows SDK + 官方扩展：VS Installer选VC++工具集和一个完整的SDK（默认勾上的那个就是）即可。扩展用cpptools，c_cpp_properties.json可以自动化配置（ctrl+shift+p, edit configurations）；另外两个json也要改，VS的编译器是cl，参数也要改；调试器也许可以用VS的。不过这样我觉得也许还不如直接用VS，而且我没试过
- 如果以上都看不懂，可以试试这个配置好的（不过人家的配置方法和我的不一样）：[【VSCode】Windows下VSCode便携式c/c++环境](http://link.zhihu.com/?target=https%3A//blog.csdn.net/c_duoduo/article/details/52083494)
- 如果不想用VSC写了，可以看看这篇问题：[毫无编程基础的小白准备学习C语言，用VC6还是VS2015？](https://www.zhihu.com/question/40929777)
- codeblocks现在还活着，配置一番（虽然同样有点折腾）也可用。Clion界面美观，功能应该也挺强，不过只有英文，刚上手用起来可能有点困难，学生可以免费申请key，否则收费

## 10. 我编写代码的体验

体积上，合并后的llvm文件夹占1.6g，vsc 0.2g，加上一些扩展。如果只是用来写C，体积占用并不算小。内存占用，如果VSC不出bug，还是比较少的（0.5g左右）。

VSC的第一优势也许是好看？虽然不是专门为C/C++设计的，但它真的还有许多其它优点。光Lint这一点就比wintc、cfree、dev c++强了很多了，更别提dev c++自己的Debug功能就有bug，还极其容易碰到。

我还有一点想对学生党说：能自己百度到这篇文章，努力去看懂、动手配置，已经比贴吧无数伸手党和等着老师在qq群里发IDE的人强了很多了。另外如果有能力，我还是建议你们读读VSC的文档：[Documentation for Visual Studio Code](http://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs)，并不复杂，体验一下英语的实际应用也不错哦。