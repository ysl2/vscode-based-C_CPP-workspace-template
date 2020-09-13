## 0. 前言

本文面向初学者，每一步都比较详细。阅读本文能学习一些命令行、程序编译和调试，以及使用VS Code的知识。如果嫌本文说的麻烦，我给个精简版的：装gcc和c/c++扩展，打开文件夹，点开源代码，F1，build and debug active file，完。

本文许多内容都可从VS Code官方文档：[C++ programming with Visual Studio Code](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/languages/cpp) 以及各个扩展的文档中获得，并且他们还会进行更新（本文也进行过几次重大更新），如果你想更深入了解，可以去看。本文也基本上是由多次尝试得出来的，如果有错误可以指出。

最终效果：实时显示编译阶段的错误、代码片段、补全、格式化、单文件的编译与调试。

## 1. 环境的准备

VSC的官网、下载、安装，我就不多说了。VSC只是一个纯文本**编辑器**(editor)，不是IDE(集成开发环境)，不含**编译器**(compiler)和许多其它功能，所以编译器要自己装好。

下载编译器：[MinGW-w64 - for 32 and 64 bit Windows](https://link.zhihu.com/?target=https%3A//sourceforge.net/projects/mingw-w64/files/) 往下稍微翻一下，选最新版本中的`x86_64-posix-seh`。最好**不要用** *Download Latest Version*，这个是在线安装包，可能因为国内的“网络环境”下载失败。如果浏览器下载失败就换迅雷下或者连手机开的热点下，还失败，那就使用能访问Google的那种方法下。

“安装”编译器：下下来的是一个7z的压缩包。如果你不会解压可以百度“压缩包怎么解压”。解压完了放到一个不容易被删的地方，层叠的可以去掉一些。看好bin文件夹的完整路径，我图里的是C:\mingw64\bin，把它加到环境变量中的PATH里去。如果你不会这一步，看本文最后面的“B. 如何添加环境变量”（可以在本页用Ctrl+F搜索）

Debian系Linux用`sudo apt update; sudo apt install build-essential`即可。

![img](https://pic4.zhimg.com/50/v2-5a148b7365261adeeb10da8b2f5e10e2_hd.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-5a148b7365261adeeb10da8b2f5e10e2_720w.jpg?source=1940ef5c)

![img](https://pic3.zhimg.com/50/v2-9113e35e8de23a0e5c30c2329ab0125f_hd.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-9113e35e8de23a0e5c30c2329ab0125f_720w.jpg?source=1940ef5c)

顺序不重要；路径可以不一样，反正保证gcc.exe在那个文件夹里就行

### 验证

按Win+R，运行cmd（不要跳这一步），输入gcc，应该会提示 *no input files* 而不是“不是内部命令或外部命令”或者“无法将 "gcc" 项识别为 cmdlet、函数、脚本文件或可运行程序的名称”。如果是“不是内部命令或外部命令”，说明gcc在的文件夹没有在环境变量的Path中，要加进去才行。如果加了还是这样，重启。如果重启了还不行，那就是你自己进行的操作有问题。

输`gcc -v`可以显示出gcc的版本。如果显示出来的版本与你刚下的**不同/更老**，说明Path里原本有老版本的编译器，可能是安装其它IDE时装上的。则需要去掉Path里原来的那一个gcc的路径。

这两项验证**一定要符合**，否则必须修改环境变量。小心**别错删**了。

![img](https://picb.zhimg.com/50/v2-09f3ba476bdede18e9a9ab36ae8d71f3_hd.jpg?source=1940ef5c)![img](https://picb.zhimg.com/80/v2-09f3ba476bdede18e9a9ab36ae8d71f3_720w.jpg?source=1940ef5c)

现在不用管clang，必定出错。clang的教程移到本文后面去了

![img](https://pic4.zhimg.com/50/v2-b63d57e63e10a991441b23ec45be86f6_hd.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-b63d57e63e10a991441b23ec45be86f6_720w.jpg?source=1940ef5c)

输入gcc -v的最后一行输出。版本要和你自己下的对应，例如64位要有x86_64和seh

### 安装扩展(extension)

- C/C++：又名 cpptools，提供Debug和Format功能
- Code Runner：右键即可编译运行单文件，很方便；但无法Debug

其他可选扩展：

- Bracket Pair Colorizer 2：彩虹花括号
- One Dark Pro：大概是VS Code安装量最高的主题

不建议/不需要装的扩展：

- GBKtoUTF8：把GBK编码的文档转换成UTF8编码的。此扩展很久没有更新了，可能有严重的bug
- C++ Intellisense：用的是gtags，本文第一个版本的选择。效果非常非常一般
- Include Autocomplete：提供头文件名字的补全，现在cpptools和vscode-clangd都已经自带这个功能了，所以不用装
- C/C++ Snippets：Snippets即重用代码块，效果自己百度；这个扩展安装量虽高，不过个人感觉用处实在不大，cpptools和clangd也自带一些；你也可以选择其他的Snippets扩展甚至自己定义

**补充知识**

- 编译器是把源代码变成可执行文件的，编辑器是你打字的软件。记事本就是一个编辑器，VSC也是编辑器。**编辑器是无法编译运行程序的**，因为那是编译器的工作
- MinGW是gcc在Windows下的移植，gcc是世界上最流行的C/C++编译器组合。但gcc这个名字也指编译C语言的那个程序，g++才是C++编译器。即gcc程序和g++程序包含在gcc套件以及MinGW里，当只说gcc时要根据语境自己区分
- 其实MinGW和MinGW-w64只是名字像，它们是两个不同的项目。为了方便，本文中的MinGW指的其实都是MinGW-w64。<del>MinGW本身已经很久没有更新了，不使用它</del>哎呀，原来MinGW是活着的，但它只能产生32位程序
- 扩展是extension，插件是plugin，VSC用的是前者这种称呼。大部分文章都是混用两者的，不严谨但是能理解就行，要学会抓主要矛盾。当然本文用的都是正确的
- 可选阅读：[[科普\][FAQ]MinGW vs MinGW-W64及其它](https://link.zhihu.com/?target=https%3A//github.com/FrankHB/pl-docs/blob/master/zh-CN/mingw-vs-mingw-v64.md)

## 2. 配置几个.json文件

创建一个你打算存放代码的文件夹，称作工作区文件夹；**路径不能含有中文和引号**，最好不要有空格，我用的是`C:\VS-Code-C`。C和C++需要分别建立不同的文件夹，除非用虚拟工作区。不要选上一节存放编译器的文件夹，源代码和编译器要分开放。

打开VSC，**选打开文件夹**；最好不要选“添加工作区文件夹”，这个就是虚拟工作区，我没用过，不保证没问题。点新建文件夹，名称为`.vscode`。不在资源管理里新建的原因是Windows的Explorer不允许创建的文件夹第一个字符是点（1903后才支持）。然后创建 launch.json，tasks.json，settings.json（**不是setting.json**） 放到**.vscode文件夹下**。效果图：

![img](https://pic3.zhimg.com/50/v2-5525fd32ffff65fab4977715ee49f067_hd.jpg?source=1940ef5c)![img](https://pic3.zhimg.com/80/v2-5525fd32ffff65fab4977715ee49f067_720w.jpg?source=1940ef5c)

一定要在.vscode里，别变成平行的了

这几个文件的内容见下。复制以下代码出来后，知乎会自动在前面加上几行保留所有权利的字，实际使用的时候肯定要删了的。有些地方可选修改，自己对照着注释看吧。注意：如果是写C++，tasks.json的一个地方必须要修改。

### launch.json代码

*externalConsole*可根据自己喜好修改；cwd可以是程序运行时的相对路径，如有需要可以改为*${fileDirname}*（感谢 

[@xhx](http://www.zhihu.com/people/dd30faca74afd3e29376d2226d44475d)

）。lldb我没用过就不多说了。type和request不变色是正常现象。

```json
// https://code.visualstudio.com/docs/cpp/launch-json-reference
{
    "version": "0.2.0",
    "configurations": [{
        "name": "(gdb) Launch", // 配置名称，将会在启动配置的下拉菜单中显示
        "type": "cppdbg", // 配置类型，cppdbg对应cpptools提供的调试功能；可以认为此处只能是cppdbg
        "request": "launch", // 请求配置类型，可以为launch（启动）或attach（附加）
        "program": "${fileDirname}/${fileBasenameNoExtension}.exe", // 将要进行调试的程序的路径
        "args": [], // 程序调试时传递给程序的命令行参数，一般设为空即可
        "stopAtEntry": false, // 设为true时程序将暂停在程序入口处，相当于在main上打断点
        "cwd": "${workspaceFolder}", // 调试程序时的工作目录，此为工作区文件夹；改成${fileDirname}可变为文件所在目录
        "environment": [], // 环境变量
        "externalConsole": true, // 使用单独的cmd窗口，与其它IDE一致；为false时使用内置终端
        "internalConsoleOptions": "neverOpen", // 如果不设为neverOpen，调试时会跳到“调试控制台”选项卡，你应该不需要对gdb手动输命令吧？
        "MIMode": "gdb", // 指定连接的调试器，可以为gdb或lldb。但我没试过lldb
        "miDebuggerPath": "gdb.exe", // 调试器路径，Windows下后缀不能省略，Linux下则不要
        "setupCommands": [
            { // 模板自带，好像可以更好地显示STL容器的内容，具体作用自行Google
                "description": "Enable pretty-printing for gdb",
                "text": "-enable-pretty-printing",
                "ignoreFailures": false
            }
        ],
        "preLaunchTask": "Compile" // 调试会话开始前执行的任务，一般为编译程序。与tasks.json的label相对应
    }]
}
```

本来2018年10月后把externalConsole设为false可以使用内置终端，但2019年10月cpptools 0.26.1引入了一个bug，导致Win下用内置终端无法输入中文，到现在0.29.0仍没有解决。我已经open了 [https://github.com/microsoft/MIEngine/pull/1025](https://link.zhihu.com/?target=https%3A//github.com/microsoft/MIEngine/pull/1025) 来fix，但是一个月过去了他们并没有review，差评。

### tasks.json代码

如果是**编写C++**，编译器需改成g++；如果不想要额外警告，把-Wall那一条删去；-std根据自己需要修改，但c++17好像有问题，最好至多用c++14；Linux下不需要加-fexec-charset。反正这些我都加了注释，还看不懂，百度gcc使用教程。

reveal控制编译时是否跳转到终端面板。可根据自己喜好修改；即使设为never，也只是不自动跳转，手动点进去还是可以看到信息。

```json
// https://code.visualstudio.com/docs/editor/tasks
{
    "version": "2.0.0",
    "tasks": [{
        "label": "Compile", // 任务名称，与launch.json的preLaunchTask相对应
        "command": "gcc",   // 要使用的编译器，C++用g++
        "args": [
            "${file}",
            "-o",    // 指定输出文件名，不加该参数则默认输出a.exe，Linux下默认a.out
            "${fileDirname}/${fileBasenameNoExtension}.exe",
            "-g",    // 生成和调试有关的信息
            "-m64", // 不知为何有时会生成16位应用而无法运行，加上此条可强制生成64位的
            "-Wall", // 开启额外警告
            "-static-libgcc",     // 静态链接libgcc，一般都会加上
            "-fexec-charset=GBK", // 生成的程序使用GBK编码，不加这条会导致Win下输出中文乱码；繁体系统改成BIG5
            // "-std=c11", // 要用的语言标准，根据自己的需要修改。c++可用c++14
        ], // 编译的命令，其实相当于VSC帮你在终端中输了这些东西
        "type": "process", // process是把预定义变量和转义解析后直接全部传给command；shell相当于先打开shell再输入命令，所以args还会经过shell再解析一遍
        "group": {
            "kind": "build",
            "isDefault": true // 不为true时ctrl shift B就要手动选择了
        },
        "presentation": {
            "echo": true,
            "reveal": "always", // 执行任务时是否跳转到终端面板，可以为always，silent，never。具体参见VSC的文档
            "focus": false,     // 设为true后可以使执行task时焦点聚集在终端，但对编译C/C++来说，设为true没有意义
            "panel": "shared"   // 不同的文件的编译信息共享一个终端面板
        },
        "problemMatcher":"$gcc" // 捕捉编译时终端里的报错信息到问题面板中，修改代码后需要重新编译才会再次触发
        // 本来有Lint，再开problemMatcher就有双重报错，但MinGW的Lint效果实在太差了；用Clang可以注释掉
    }]
}
```

### settings.json代码

把这个文件里的东西放到“用户设置”里可以覆盖全局设置，否则只在当前工作区才有效。这两点各有自己的优势。

Code Runner的命令行和某些选项可以根据自己的需要在此处修改，想自定义或者想知道是什么意思还是参见此扩展的文档和百度gcc使用教程。如果终端用的是cmd（**Win7**默认）需要改用注释掉的，或者把`terminal.integrated.shell.windows`改为PowerShell；Win10默认就是PS就不用改。

感谢 

[@Wellin Boss](http://www.zhihu.com/people/e011194994d3415968b3886ade2b588c)

 提到的snippetSuggestions；不过用top有时还是有点问题的，所以改成可选。



```json
{
    "files.defaultLanguage": "c", // ctrl+N新建文件后默认的语言
    "editor.formatOnType": true,  // 输入分号(C/C++的语句结束标识)后自动格式化当前这一行的代码
    "editor.suggest.snippetsPreventQuickSuggestions": false, // clangd的snippets有很多的跳转点，不用这个就必须手动触发Intellisense了
    "editor.acceptSuggestionOnEnter": "off", // 我个人的习惯，按回车时一定是真正的换行，只有tab才会接受Intellisense
    // "editor.snippetSuggestions": "top", // （可选）snippets显示在补全列表顶端，默认是inline

    "code-runner.runInTerminal": true, // 设置成false会在“输出”中输出，无法输入
    "code-runner.executorMap": {
        "c": "gcc '$fileName' -o '$fileNameWithoutExt.exe' -Wall -O2 -m64 -lm -static-libgcc -std=c11 -fexec-charset=GBK && &'./$fileNameWithoutExt.exe'",
        "cpp": "g++ '$fileName' -o '$fileNameWithoutExt.exe' -Wall -O2 -m64 -static-libgcc -std=c++14 -fexec-charset=GBK && &'./$fileNameWithoutExt.exe'"
        // "c": "gcc $fileName -o $fileNameWithoutExt.exe -Wall -O2 -m64 -lm -static-libgcc -std=c11 -fexec-charset=GBK && $dir$fileNameWithoutExt.exe",
        // "cpp": "g++ $fileName -o $fileNameWithoutExt.exe -Wall -O2 -m64 -static-libgcc -std=c++14 -fexec-charset=GBK && $dir$fileNameWithoutExt.exe"
    }, // 右键run code时运行的命令；未注释的仅适用于PowerShell（Win10默认）和pwsh，文件名中有空格也可以编译运行；注释掉的适用于cmd（win7默认）、PS和bash，但文件名中有空格时无法运行
    "code-runner.saveFileBeforeRun": true, // run code前保存
    "code-runner.preserveFocus": true,     // 若为false，run code后光标会聚焦到终端上。如果需要频繁输入数据可设为false
    "code-runner.clearPreviousOutput": false, // 每次run code前清空属于code runner的终端消息，默认false
    "code-runner.ignoreSelection": true,   // 默认为false，效果是鼠标选中一块代码后可以单独执行，但C是编译型语言，不适合这样用
    "code-runner.fileDirectoryAsCwd": true, // 将code runner终端的工作目录切换到文件目录再运行，对依赖cwd的程序产生影响；如果为false，executorMap要加cd $dir

    "C_Cpp.clang_format_sortIncludes": true, // 格式化时调整include的顺序（按字母排序）
}
```

### c_cpp_properties.json

如果你确定不需要使用别人的库，则现在的版本（0.18.0之后）**不需要创建这个文件**了，cpptools会自动使用默认的设置。所以本文也不再包含此文件的配置。

如果你自己编写了头文件又不在workspaceFolder下，或是使用别人的库，就需要手动创建这个文件放到`.vscode`下了。模板可以参考：[Microsoft/vscode-cpptools](https://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/blob/master/Documentation/LanguageServer/MinGW.md)。

一些曾经的经验：

- 库的路径要加到includePath和browse里
- 如果需要递归包含，末尾加`/**`。
- 这个json不允许有注释，其实按照json标准本来就不能有
- compilerPath好像必需是MinGW的完整路径，精确到gcc.exe，否则会提示找不到头文件；Linux下是/usr/bin/gcc；但我很久没有测试过了
- Windows下的目录分隔符为反斜杠，原本应使用两个反斜杠来转义，但直接用斜杠这里也接受
- 除了配置这个文件，还需要进行别的操作。一部分可以参考下文的“多文件编译”

### 补充知识

json是一种数据交换格式，<del>大部分是JavaScript的子集</del>现在变成完全子集了。在这里就是用作**配置**文件。VSC和各个扩展会读取json中的条目，来决定某些功能和行为。

这么多条目哪里来的呢？这其实和API差不多。扩展开发者会把允许修改的选项“告诉”VSC，各个扩展的安装页面都有写。作为使用者，输入的时候VSC会提示你哪些是可用的，所以其实很容易写。

为什么要往json里写这么多的东西？因为VSC本身并没有对C语言特别优待，对其他许多语言也一样。而且最关键的编译命令和VSC是没有关系的，这就是上面提到过的编辑器和编译器的事。VSC不负责、无法、不能编译C语言。

以$开头的是VSC预定义的变量，具体参见：[Variables Reference](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs/editor/variables-reference)。比如$file在实际运行时会替换成当前打开的文件名。

## 3. 写代码，编译，调试

新建文件后就可以写代码了，c语言源代码后缀是.c，c++是.cpp或.C或.cxx（这也要我教吗……）。代码文件在保存工作区内都可以，可以自己建立文件夹，**不必放到.vscode文件夹里**，但**路径里(包括文件名)不要含有中文和引号**，最好不要有空格。主要是许多符号是有效的shell语法，不然试试Linux下用rm删除一个叫做-rf的文件？没查过绝对写不出来。

按Alt+Shift+F（或者用右键菜单）可以格式化代码，修改格式化方式如大括号是否换行可看：[Format Curly Braces on Same Line in C++ VSCode](https://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/46111834/format-curly-braces-on-same-line-in-c-vscode)。出现Intellisense的时候**按tab可以补全代码**。打出snippets时会出现多个跳转点，按tab可以跳到下一个去。

停止输入一小段时间（一秒）后就会有Lint，扩展会给一些建议性的warning（比如声明了变量但不使用），自己清楚就行。如果觉得不爽，也有方法不让它提示，比如去掉-Wall就会少一些。如果还想去掉更多的警告，我提示一下：-Wno-...。找好参数后可以用`#pragma GCC diagnostic ignored`或者加到各种Flags里。总之自己研究。不过cpptools的Lint不支持设定Flags，有点坑，Follow：[Error and Warning Flags?  · Issue #2814 · microsoft/vscode-cpptools](https://link.zhihu.com/?target=https%3A//github.com/microsoft/vscode-cpptools/issues/2814)

接下来说说运行的事。首先，编译是从源代码生成可执行文件的过程。而调试其实是一种特殊的运行，是能控制程序运行，方便之后修改的一种手段。这是两个不同的阶段，可能出现编译通过但调试失败，也可能直接编译就失败，还有可能编译还没开始就失败了。如果你只说“运行失败”，别人是看不出是哪个阶段出了问题的。如果确定某个阶段通过了，那就不用管那个阶段了，就能专注于解决别的阶段的问题。

按Ctrl+Shift+B单纯编译，按F5为编译加调试；本来ctrl+F5为运行但不调试，但现在cpptools暂不支持，还是会调试。Follow: [Support "Run without debugging" · Issue #1201 · microsoft/vscode-cpptools](https://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/issues/1201)

在写程序初期，我强烈建议**不要把f5当作编译来使用**，因为有的bug只会产生警告，不会阻止编译，但这些东西越早期解决越好。编译信息会在底下的“终端”面板里，如果代码有错误，点进去可以看编译器报的信息；不过因为有Lint了，平常的错误可以马上被发现和修改，写代码就轻松很多。

加断点在列号前面点一下就行，右键可以加条件断点。如果想从一开始就停下来，可以加在main函数那里，或者*launch.json*中有个设置。开始调试后，按f11可以一步一步进行，箭头所指的那行代码就是**下一步要运行的代码**；f5是一直运行到下一个断点，右键某一行代码可以选择一直运行到指定的那一行。

左边有个调试栏，可以看到变量的值，自动栏没有的可以手动添加：在代码里选中要监视的表达式，点右键有选项可以直接添加到Watch里，复杂的才需要手打。把鼠标放到变量上可以看到变量的值，但是只能识别简单的表达式。栈帧对于观察递归很有用。栈溢出和段错误时还可以抓取“异常”，自动跳转到出错的行。

特别的，对于数组：C语言的数组经过函数传递以后会退化为指针，直接添加表达式就只能看到第一个元素。此时可以强制转换成指向固定大小的数组指针再解引：例如`int arr[10]`传进函数里后就变成了`int* arr`，在Watch里添加`*(int(*)[10])arr`，这样就能看到完整的数组了。但长度必须是写死的，自己小心越界。或者简单的程序用全局变量数组就能一直看到了。另一种只对gdb且是非void*有效的写法：`*arr@10`。

快捷键：[vscode: Visual Studio Code 常用快捷键 - 志文工作室](https://link.zhihu.com/?target=https%3A//lzw.me/a/vscode-visual-studio-code-shortcut.html)。英文文档中当然有快捷键的说明，还有Cheet Sheet可以看，而且英文文档会更新。这个单独列出来仅给初学者。

**如果遇到错误，先看底下的“某些可能出现的错误”以及看评论区**。

### Code Runner

如果你不需要调试，可以直接右键选run code，或者点右上角的播放按钮。如果在终端里运行，可以输入数据，但是少了显示时间的功能；在“输出”中则上面两项相反。

在终端中按Ctrl + C可以终止程序运行，下一次运行前必须保证当前程序已经终止了（对于task也是一样的）。如果你想要复制，选中内容后直接按一下右键就可以了；粘贴则是在未选中时按右键；这个操作仅限于Win10，ctrl+c也可以复制但可能一不小心就把程序终止了。

用它还可以在非工作区内编译运行程序，不过默认用的是gcc，除非把executorMap放到全局设置里。按照我的配置，task和Code Runner还有一点不同：working directory。前者是你打开的文件夹，后者是文件所在的文件夹。当然它们也都可以自己修改。

**其实Code Runner只是代替你手动输命令**，功能并不强，算是适用场景不同吧。不要以为run code跑个Hello World很简单，Code Runner就很强、前面那么多配置都是垃圾了。

另外，楼下的答主韩骏就是此扩展作者，有事统统找他（滑稽）。

### 多文件编译

如果你想进行少量的多文件编译，C语言直接用`gcc 源文件1.c 源文件2.c 头文件1.h`这样就好，C++用g++。默认生成a.exe，加-o可指定输出文件名，其余选项百度gcc使用教程。如果需要多次编译可以写一个批处理。 

如果你想进行大量的多文件编译，请学习如何写makefile或使用cmake。然后把tasks的命令改成调用make（或mingw32-make）等。

如果你想使用别人的库，比如ffmpeg，可能需要在命令中指定`-I`、`-l`（小写的L）、`-L`。具体参数阅读那个库的文档。还可能需要把路径添加到c_cpp_properties.json里来配置Intellisense。

这些情况下可以考虑单独建一个工作区，不要和单文件编译的共用。其实不新建工程(Project)、只是单文件就能调试，是不利于以后使用和理解大型IDE的。不过初学也不用掌握那么多，不要觉得建工程很麻烦、不建工程就能编译很强就是了。

总之这些和VSC无关，用其它IDE或是手动编译也会遇到差不多的问题，也有点复杂。本文就不多讨论这些了，自行解决。

### 保存文件夹

以后**写代码必须打开之前那个建立好的文件夹**才能写，否则所有的Intellisense都没有，只有Code Runner能用。（主要是需要那四个json，新建其它文件夹需把那几个json复制过去就也能用）

可以创建一个快捷方式（右键新建），把工作区路径作为参数传给VSC主程序，记得打双引号；还可以加个图标。1.18有了真正的虚拟工作区，可以一个窗口包含多个不在一起的文件夹，“文件”菜单里也有“保存工作区”这个功能，但是我都没试过，不保证没问题。

![img](https://pic4.zhimg.com/50/v2-ef8da0bfd7f5e03cfd9ed0354c7c19ec_hd.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-ef8da0bfd7f5e03cfd9ed0354c7c19ec_720w.jpg?source=1940ef5c)

### 清理临时文件

按照这样配置，长期编译代码下来肯定有一大堆的exe，还可能分散在不同的文件夹里。

可以考虑修改一下json文件，把生成文件的目录指定到一个专门放exe的文件夹里；如果不会，百度gcc使用教程以及看我的json里的注释。或者资源管理器右上角搜索*.exe然后手动删除。

也可也写个bat，放到工作区里，要用的时候右键Run Code：

```bat
del %~dp0*.exe /q /s
del %~dp0tempCodeRunnerFile.c /q /s
del %~dp0a.out /q /s
del %~dp0*.o /q /s
```

其中`%~dp0`会被替换成该批处理所在目录，这是为了防止有同学选错工作目录，误删根目录下的文件；code runner的设置我也调整成了先切换到文件目录，双保险。

### 添加纯英文输入法

Windows 10，默认输入法只有一个微软拼音，按一次shift就能进行中英转换；为了保持兼容，按ctrl加空格也能进行中英转换，但这个快捷键正是强制触发Intellisense的快捷键。

所以，我强烈建议手动添加“英语”语言输入法，正常代码时切换到纯英文输入法（win+空格），在需要频繁中文注释或者在字符串里写中文时才用中文输入法的英文模式。

这样也可以解决某些游戏需要用到shift键但同样快捷键冲突的问题。具体操作可以自己百度，也可以看我写的这篇有点复杂的文章：[Windows 切换显示语言与添加纯英文输入法](https://zhuanlan.zhihu.com/p/62890493)。

### 某些可能出现的错误

为了阅读的连贯性，这一部分移到了“A. 一些其它可能出现的错误”。遇到问题优先查看那里是否已经提了。

## 4. 其他设置

我的一些其他的设置，用在全局settings.json里，根据自己的情况调整，不需要全部照着我的写。**写完一个以后要打逗号**；最外面的那个大括号我没加，就别弄丢了**。**

现在的VSC用的是可视化的设置界面，其实原本是手动编辑且出现两列设置的。点击右上角那个花括号就能手动编辑。

```json
"editor.fontFamily": "等距更纱黑体 SC", // 控制编辑器字体
"editor.fontSize": 16, // 同上
"editor.fontLigatures": true, // 连体字，效果不太好形容，见 https://typeof.net/Iosevka 最后一部分
"editor.minimap.enabled": false, // 我个人不用minimap，就是右边那个东西
"editor.dragAndDrop": false, // 选中文字后，可以拖动它们调整位置。我是不需要
"editor.cursorSmoothCaretAnimation": true, // 移动光标时变得平滑
"editor.smoothScrolling": true, // 滚动平滑，不过效果很微弱
 
"files.trimTrailingWhitespace": true, // 保存时，删除每一行末尾的空格
"files.insertFinalNewline": true, // 保存后文件最末尾加一整行空行，Linux下的习惯
"files.autoGuessEncoding": false, // 启用后，会在打开文件时尝试猜测字符集编码。我关闭的理由见6，默认也是禁用的

"workbench.colorTheme": "One Dark Pro", // 主题
"workbench.colorCustomizations": {
      "activityBar.foreground": "#39C5BB" // 自定义颜色；想定义其它位置参见官方文档
},
"workbench.settings.useSplitJSON": true, // 恢复手动编辑时的两列设置
"window.zoomLevel": 0.2, // 整体放大

"git.enabled": false, // 如果你不用git，可以考虑关闭它
"git.ignoreMissingGitWarning": true, // 同上

"[c]": {
    // "files.encoding": "gbk" // 这样的格式可以对指定后缀的文件应用设置，如果你实在想用gbk，就这样设置吧。cpp同理。
},
```

更纱黑体是楼下B神做的字体，特点是标点好看（误）：[be5invis/Sarasa-Gothic](https://link.zhihu.com/?target=https%3A//github.com/be5invis/Sarasa-Gothic)

Consolas虽然是Windows自带字体中还算行的，但它只有英文字体；微软雅黑虽然是非衬线字体，但它不是等距的，这一点非常不适合编程，等线也不等距；中易宋体……告辞。不下新的字体，其他两大系统我不清楚，Windows下简直没有编程可用的字体。Consolas加雅黑嘛，也还行吧，不过能用更好的干嘛不用呢。

## 6. 关于中文和乱码

VS Code输出中文会出现乱码，很多人都遇到过。这是因为源代码默认是UTF-8编码，cmd/PowerShell是GBK编码。直接编译，会把“你好”输出成“浣犲ソ”。Linux就没有这个问题。

一种解决方法是用gcc，编译时用*-fexec-charset=GBK*这个参数（目前的配置是有的），生成的程序就是GBK编码的，源文件仍是UTF8*。*而clang的execution-charset supports only UTF-8，所以用clang就无解。

另一种方法是用宽字符输出，有点复杂，见：[C语言与中文的一些测试 (Win, UTF8源码)](https://zhuanlan.zhihu.com/p/71778196) 。此文也提到了chcp 65001的事。

直接修改非Unicode程序的语言为UTF8(beta)会导致所有用GBK的程序乱码，这是不可接受的。

当然，如果你不打算坚持用UTF8作为源代码的编码，那直接用GBK编码也行。

如果是**打开已有的以GBK编码的文件**，VS Code默认会以UTF-8编码打开（除非你设置了猜测编码），这样编辑器内的中文就会乱码，此时要点右下角的GBK，选“通过编码重新打开”，选UTF-8即可。那为什么不打开自动猜测编码呢？可以参见我的这个回答：[VS Code 中文注释显示乱码怎么办？](https://www.zhihu.com/question/34415763/answer/596058039)。如果你不担心，那就开吧。

如果把代码文件发给其他用Windows的人，最好转成GBK，否则别人用记事本打开有可能会乱码（1803后的记事本改善了一些，联通已经不会乱码了）。

对于调试，无论怎么做，gdb都**无法调试路径中存在中文的程序**。这个貌似是gdb的bug，但是优先级极低：[[gdb\] cannot not open source file with Chinese/Unicode characters in path when debugging · Issue #602 · microsoft/vscode-cpptools](https://link.zhihu.com/?target=https%3A//github.com/microsoft/vscode-cpptools/issues/602)

总之，对于Windows，这些问题没什么好办法，因为本文用的这一套就是从Linux搬过来的。用Linux应该就没有这些问题了。

## 7. 找不到头文件的错误

![img](https://pic4.zhimg.com/50/v2-877058be4208e6b3648a1da6cec6205e_hd.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-877058be4208e6b3648a1da6cec6205e_720w.jpg?source=1940ef5c)

- gcc不在Path里。回去看上面的验证那一步
- 手动配置了c_cpp_properties.json且包含的路径不正确。如果没有创建此文件就不用管
- 重启试试

如果你保证这几点都符合要求，那我也没什么好办法……要不就换其它答主的教程吧。注意这句话是终极Fallback，如果你确信你没有操作错误，那就不用问我了，我是无法解决的。

另一种找不到头文件的错误：

![img](https://pic4.zhimg.com/50/v2-a7e1578ac1d50bcba9ccc3986ae607ad_hd.jpg?source=1940ef5c)![img](https://pic4.zhimg.com/80/v2-a7e1578ac1d50bcba9ccc3986ae607ad_720w.jpg?source=1940ef5c)

这种情况是因为clang的默认target为msvc，需要加`--target=x86_64-w64-mingw`这个参数才行。

这个默认target是写死在源代码里的，我找了一圈没找到正常修改办法。下载clang的源代码，自己改掉，再编译clang本身，也许可以解决。或者装Windows SDK而不使用mingw，这样就符合默认target了。

当然这个时候最简单的办法就是用gcc编译。

## 12. 在Win下使用clang

其实这部分本来是本文的主打部分的，但是确实会引入太多概念，而且效果也不是那么好（因为没有libc++），现在全都放在这里变成可选内容。理论上在WSL里用更好，又但也许这样会从一个坑跳到另一个坑，我没试过。本部分仅留作踩坑经验。

- Q：为什么要装Clang？
  A：错误提示更友好。以及：[Clang 比 GCC 好在哪里？](https://www.zhihu.com/question/20235742) 
- Q：Clang怎么读？
  A：正确答案是/ˈklæŋ/，即c发"可"的音；不过实际还是以双方都理解为基础，比如平常把SQL说成circle也是能理解的。
- Q：为什么既要装Clang又要装MinGW？
  A：因为Win下的Clang没有libc++。你也可以选择装VS用Windows SDK，就不需要MinGW了，这个更官方一些，但体积较大。
- Q：MSVC integration install failed / unable to find a Visual Studio installation...
  A：就是上一条的原因，Clang默认用的是MSVC的后端。但本部分用的是MinGW，所以就不用管这个提示。要不就装Windows SDK

**环境**

- [LLVM Download Page](https://link.zhihu.com/?target=https%3A//releases.llvm.org/download.html)：在此页面下载Clang。选 Pre-Built Binaries 中的 Windows (64-bit)，不需要下.sig文件
- vscode-clangd：提供Intellisense和Lint功能；仓库及用法见：[clangd/clangd](https://link.zhihu.com/?target=https%3A//github.com/clangd/clangd) 
- C/C++ Clang Command Adapter：本文曾用过，vscode-clangd出现问题时可以考虑换成这个试试；配置有一些不同，需要改clang.cflags；如果没出问题就别装了
- Clang-Format：只有想自定义代码风格时才装，比如大括号是否换行。需要另外学习如何使用
- CodeLLDB：lldb的vscode扩展，需要Python环境；我没用过

**配置**

- 编译命令加一句`--target=x86_64-w64-mingw`。clang的默认target为msvc，不加就会找不到头文件
- `C_Cpp.errorSquiggles`、`C_Cpp.autocomplete`、`C_Cpp.suggestSnippets`都关掉，否则会跟clangd报的重复

**[compile_flags.txt](https://link.zhihu.com/?target=https%3A//clangd.github.io/)**

其实就是设定那些编译选项，基本上用-Wall和--target=x86_64-w64-mingw就行。clangd只会使用离要评估的文件最近的一个compile_flags.txt。因为需要保证有--target，最好创建一个放到工作区磁盘的根目录用作fallback。

但比较坑的是，C和C++都会使用.h作为头文件，如果不加任何std，.c和.cpp能正确lint，但是.h会使用C的模式。对于fallback来说感觉没什么好办法。还是那句话，要不就装Windows SDK。

## 13. 我编写代码的体验

体积上，本体+编译器+扩展，如果只是用来写C，硬盘占用并不算小，上1G了。内存占用还是比较少的（0.5g左右）；曾经出过吃大量内存的bug，当然现在早就修好了。

VSC的第一优势也许是好看？虽然不是专门为C/C++设计的，但它应该是现在最现代化的纯文本编辑器了。而且光Lint这一点就比wintc、cfree、dev c++强了很多了，更别提dev c++自己的Debug功能就有bug。

其它IDE，CodeBlocks还活着，虽然历史包袱非常明显。Clion界面美观，功能也挺强，不过只有英文，刚上手用起来可能有点困难；学生可以免费申请key，否则收费。如果想用Windows SDK，下个Visual Studio (Installer)，Community版勾上C++桌面开发就是，这样就符合Clang的默认Target了，但我觉得还不如直接用VS。其它答主对一些C的IDE的评价可以看这个回答：[毫无编程基础的小白准备学习C语言，用VC6还是VS2015？](https://www.zhihu.com/question/40929777)。

我还有一点想对学生党说：能自己百度到这篇文章，努力去看懂、动手配置，已经比贴吧无数伸手党和等着老师在qq群里发IDE的人强了很多了。如果有能力，还是建议你们读读VSC的文档：[Documentation for Visual Studio Code](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/docs)，并不复杂，体验一下英语的实际应用也不错哦。

## A. 一些其它可能出现的错误

- 如果你只写了个hello world，不加任何断点，**按f5以后黑框框一闪而过/闪退是正常现象**。想让程序暂停运行可以在末尾加上一个或两个`getchar();`，不明白为什么有时要用两个？去问你们C语言老师；或用`system("pause")`，或加断点，或者launch.json里用内置终端(externalConsole false)。如果你硬要用外置终端且要什么都不做，就想运行后暂停在那里，那么VSC办不到，至少我的配置办不到，我也不想研究，因为我用内置终端。
- preLaunchTask“Compile”已终止，退出代码为 1：编译有error并且你用的是F5运行的就会有这个提示；如果你点仍然调试，就会调试上一次编译成功的文件。其实所有的编译失败都会触发这个错误，出错的返回值是1难道不是常识？所以仅仅告诉我出现了这个提示**根本没用**，它的意思就是出错了，没有人能看出原因，**原因在“终端”面板里**。如果Hello World能正常调试运行，但某个其它代码出现这个错误，很可能是**你自己代码本身有错误**。
- 终端将被任务重用，按任意键关闭：听过“按任意键继续”吗？这句话就是这个意思。这句话比上面那个退出代码为1还要没用，它根本就不包含任何有效信息，**无论成功还是出错都会显示它**，它就是一个说明性的文字。
- 无法打开...，找不到文件(file:///build/glibc-OTsEL5/glibc-2.27/...)：我在Linux下遇到了这个问题，看起来应该是你试图step in一个库函数，但是没有源代码。解决办法是下一个glibc放到指定位置。或者参见这个：[Disable "Unable to open file" during debug · Issue #811 · Microsoft/vscode-cpptools](https://link.zhihu.com/?target=https%3A//github.com/Microsoft/vscode-cpptools/issues/811)。
- undefined reference to xxx ... linker command failed：调用了未声明的函数。可能是函数名打错了，或者没有include头文件。总之是你自己的代码有错误。
- ld: cannot open output file ... permission denied：原程序仍在运行（比如死循环），无法被覆盖所以生成失败。任务管理器结束那个进程即可。
- MinGW下，监视（Watch）窗口里用strcmp，会导致gdb崩溃退出，原因不明。linux下正常。
- 重命名文件后，原来已有的Lint还会在问题栏里；修改了文件后断点可能会失效。以及还存在一些其他的像这样的小bug，一般关掉VSC再开就行。
- 此配置无法使用Bash for Windows或WSL，因为bash中的反斜杠会被识别为换行。cpptools现为launch.json提供了一个*Bash on Windows Launch*的snippets。现在又出了一个Remote WSL。但这些我都没有试过如何使用。
- 如果你要进行调试，不要开优化。gcc用-Og还可以保留一些调试信息，但clang用了以后就不能用gdb调试了。即使如此我还是在某一次写代码的时候遇到了无法跳入函数的问题，而VS可以跳入。
- vscode-clangd第一次无法正确检测到printf和scanf还有realloc，但是代码中用过一次以后就好了。我也不知道为什么。
- 此时不应有 &：终端改为用PowerShell或者code runner的executorMap用我注释掉的那两条命令。具体看上面settings.json的说明。
- crt0_c.c:(.text.startup+0x2e): undefined reference to `WinMain'：没有main函数，或者把main写成了mian。
- 在Win下用clang+mingw，#include <bits/stdc++.h>会报'float.h' file not found，改成g++后就好了。我觉得这应该是库的bug，反正我是不知道怎么解决。或者别用C++17试试

## B. 如何添加环境变量

图形化的方式：右键“此电脑”，选属性；或者按win+PauseBreak。选左边的高级系统设置，高级，环境变量。选上面那几个条目中的Path，编辑，新建。然后把含有目标exe的文件夹路径填进去。例如gcc在`C:\mingw\bin\gcc`，就填`C:\mingw\bin`，Win大小写不敏感。 

命令行的方式：打开cmd或者PS，`setx /m path "%path%;C:\mingw\bin\"` 。此命令无需管理员权限，且不会随着终端退出而退出（就是和上面图形化的效果一样）。

如果还不知道怎么修改，可以自己百度或者b站搜“环境变量”看视频。大多不是C的但是区别不大，小心**别错删**了就是。

------

有问题可以留言讨论，不过最好**详细一点描述。**而且我再说一次，**不要只告诉我“preLaunchTask已终止，代码为1”这一句话。这句话没用。**

原创，非商业转载请注明出处即可。