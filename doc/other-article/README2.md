## 配置clang

作者：Violinwang
链接：https://zhuanlan.zhihu.com/p/84258079
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



Visual Studio Code是Microsoft推出的一款可高度定制的代码编辑器，具有无与伦比的颜值和强大的可扩展性。但是对于C语言初学者来说，VSCode不是“开箱即用”的，并且全英文的界面也不是那么友好，这导致Dev-C++甚至VC++6.0在今天仍然有不小的市场。本文将带各位自己搭建一个C语言开发环境，告别祖传Dev-C++。

## 第一步：安装MinGW

MinGW是GNU为windows环境提供的编译工具链，其安装方法网上有一大堆，这里简要提一下。

首先下载MinGW安装器：[下载链接](https://link.zhihu.com/?target=http%3A//rec.ustc.edu.cn/share/aa13f7a0-e01e-11e9-bc25-6f5bd9874ea7)

安装以后，运行安装器，标记mingw32-base-bin和mingw32-gcc-g++-bin两项为安装，在左上角的Installation菜单中提交更改。安装过程需要从境外网站下载文件，所以可能比较慢。

然后添加系统环境变量。首先找到你的MinGW安装位置（默认是C:\MinGW\）下的bin文件夹，确认一下这个文件夹下有gcc.exe与gdb.exe两个文件，然后复制这个文件夹的路径（默认是C:\MinGW\bin）。在此电脑上单击右键，属性，高级系统设置（或Cortana搜索高级系统设置），点最下面的环境变量。

![img](https://pic2.zhimg.com/v2-b4e166406dd3098553b5d4d44f7fef3e_b.jpg)

然后在下面系统变量处找到path变量，点击下面的编辑

![img](https://pic3.zhimg.com/v2-49f0cb6acbd6a9b7858798eb0fccc7f1_b.jpg)

在最后添加一个英文的分号;然后粘贴上我们刚刚复制的路径

![img](https://pic1.zhimg.com/v2-90c755390e4eb01ec9065aa240c2184a_b.jpg)

完成以后一路确定回到桌面

为了检查我们的环境变量是否添加成功，按下window徽标键+R，输入cmd回车，在命令窗口中输入gcc回车，如果出现如下情况说明成功

![img](https://pic3.zhimg.com/v2-08863838a995456f70ef923741efb920_b.png)

## 第二步：安装clang（可选，建议有经验的同学使用）

虽然我们已经有了gcc了，但是为了更好的体验，建议大家安装clang。clang提供的更加友好的报错信息以及静态代码检查功能都是很有必要的。

从此处下载clang的安装包：[下载链接](https://link.zhihu.com/?target=http%3A//rec.ustc.edu.cn/share/a5874eb0-e031-11e9-835c-576db553715d)

安装过程中，注意此处最好选择让安装程序帮我们添加环境变量

![img](https://picb.zhimg.com/v2-83adce7ca5eab00eeae7dc860e4214ca_b.jpg)

安装好后，进行下一步

## 第三步：安装与配置vscode（1）

首先从官网下载vscode的安装包：[下载链接](https://link.zhihu.com/?target=https%3A//code.visualstudio.com/)

安装完成后，启动vscode，打开左侧插件栏

![img](https://pic3.zhimg.com/v2-aa5f962b2ad95eeb05d091a02b41075e_b.jpg)

我们首先要安装的是C/C++扩展（上图中第二个，如果没有可以搜索），它提供了基础的C/C++支持，单击install即可安装。

接下来安装Code Runner扩展，它提供了一个快捷的方式，让你无需复杂的配置就可以快速运行C程序。

如果你上面安装了clang，那么需要一些额外的配置才能让它发挥作用，否则起作用的是默认的gcc编译器。如果你没有安装clang，可以直接跳到第四步。

下面点击Code Runner扩展的齿轮图标，选择Configure Extension Settings，打开Code Runner的配置界面，找到下图中的一项，点击下面的Edit in settings.json

![img](https://pic4.zhimg.com/v2-bd7fd1d1553945c6b683747eff9112fe_b.jpg)

然后在打开的文件中输入如下内容

```json
{
    "code-runner.saveFileBeforeRun": true,
    "code-runner.executorMap": {
        "c": "cd $dir && clang $fileName -o $fileNameWithoutExt.exe --target=i686-pc-mingw32 -lm && $dir$fileNameWithoutExt.exe"
    },
    "code-runner.runInTerminal": true
}
```

保存，关闭此文件，code runner的配置就完成了。可以进行如下测试：新建一个文件（比如test.c)，输入如下内容：

```c
#include <stdio.h>
int main(void) {
    printf("Hello World!\n");
    return 0;
}
```

然后点击右上角的三角形图标运行，如果下面的终端窗口中出现Hello World!字样，说明code runner配置成功了。

## 第四步：配置vscode（2）

这一步是配置C/C++编译和调试环境。如果你不需要用到调试器，可以不进行这一步，只用code runner运行即可。

首先要注意的一点是，如果要对一个程序进行调试，vscode要求必须建立workspace。并且，每个workspace的配置文件是独立的。首先，在某个位置建立一个空文件夹（路径中不得有中文。推荐放在根目录下，比如D:\VSCodeProjects\myWorkspace\），然后打开vscode，在File菜单中点击Add Folder to Workspace，选中刚刚新建的文件夹。完成以后应该是这个样子（记得点击左侧边栏第一个按钮切换到资源管理板块）：

![img](https://pic4.zhimg.com/v2-1dff3ef294d51e0775828241b0229d3b_b.jpg)

然后在myWorkspace上右键，New File，输入文件名（比如main.c），回车。

接下来在这个文件中输入你的程序代码。

下面配置build task。如果你没有安装clang，那么比较简单，在菜单栏中点击Terminal->Configure Tasks，出现的复选框中选择第二项C/C++: gcc.exe build active file即可。

![img](https://picb.zhimg.com/v2-71420e0f5598694392dc7ce166b2877f_b.jpg)

如果你安装了clang，那么选择第一项，然后在打开的tasks.json文件中输入如下内容（原有内容删掉）

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "shell",
            "label": "clang.exe build active file",
            "command": "C:\\Program Files\\LLVM\\bin\\clang.exe",
            "args": [
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "--target=i686-pc-mingw32",
                "-lm"
            ],
            "options": {
                "cwd": "C:\\Program Files\\LLVM\\bin"
            },
            "problemMatcher": [
                "$gcc"
            ],
            "group": "build"
        }
    ]
}
```

注意上面的command和cwd路径要根据你安装clang时选择的路径去填写。

保存tasks.json，关闭该文件。

接下来配置调试器。点击菜单栏Debug->Open Configurations，在出现的复选框中选择第一项C++ (GDB/LLDB)

![img](https://pic1.zhimg.com/v2-1ad27155eae7d29a5cad39cb5a8a4d4e_b.jpg)

接下来会出现这个

![img](https://picb.zhimg.com/v2-d93441ba011ad0c0a28087387b707f89_b.jpg)

如果你没有安装clang，点击第二项gcc.exe build and debug active file即可。

如果你安装了clang，点击第二项gcc.exe build and debug active file，在出现的launch.json文件中输入如下内容（原有内容删掉）：

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "clang.exe build and debug active file",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "C:\\MinGW\\bin\\gdb.exe",
            "setupCommands": [
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "clang.exe build active file"
        }
    ]
}
```

（这里不是选择第一项，原因是我们只安装了clang编译器而没有安装配套的调试器lldb，所以还是要借用gcc配套的调试器gdb来调试。感兴趣的读者可以研究一下怎样用lldb来取代gdb）

保存，关闭launch.json。

**注意：刚刚配置的tasks.json和launch.json文件只对当前workspace有效，所以如果以后你换了另外一个文件夹当作workspace，需要重新设置。**

下面来测试一下我们的调试功能是否正常：在main.c文件中输入以下内容：

```c
#include <stdio.h>
int main(void)
{
    int a, sum = 0;
    for (a = 1; a <= 100; a++)
    {
        sum += a;
    }
    printf("%d\n", sum);
    return 0;
}
```

保存，在sum+=a一行左侧点击鼠标添加断点，然后点击Debug->Start Debugging（或按F5）

![img](https://pic3.zhimg.com/v2-56ad19abf8786d23f6657b6f7c81beb5_b.jpg)鼠标点击红点处即可添加/移除断点

如果出现如下的情况，恭喜你，你的调试器配置完成了！

![img](https://pic3.zhimg.com/v2-878bef9011a19d73c2ab6afaeb0e9301_b.jpg)注意左侧的变量观察窗口，点击上面出现的几个按钮观察程序执行情况

注1：如果你收到一个提示，让你安装.NET Framework 4.6.2，可以从此处下载安装：[下载链接](https://link.zhihu.com/?target=https%3A//support.microsoft.com/zh-cn/help/3151800/the-net-framework-4-6-2-offline-installer-for-windows)

注2：如果你的调试器总是提示你找不到某个文件，看看你的文件路径里有没有中文。

## 第五步：安装其他实用插件（可选）

第一个建议安装的插件是C/C++ Clang Command Adapter。它可以提供代码的静态检查(lint)功能，让你在写代码的时候立刻发现错误。不过，它运行的基础是clang——也就是说，如果你之前没有安装clang的话，就享受不到它带来的好处啦！

![img](https://pic4.zhimg.com/v2-2be3a47500bb2500ffea3041a8403a73_b.jpg)当你漏了一个分号时，lint工具提醒你

![img](https://picb.zhimg.com/v2-a2b42990d1270690cbda6bd21c4f0c2a_b.png)当你在printf函数中使用了错误的转换说明符时，lint工具提醒你（这种错误编译器是检查不出来的哦，最多给一个警告）

另一个建议安装的插件是One Dark Pro。这是一个主题插件（或许是vscode最流行的主题），提供了更漂亮的代码高亮。当然，如果你不喜欢这个配色，可以不装。毕竟即使是默认主题也比Dev-C++好看太多了。

![img](https://pic3.zhimg.com/v2-28136ac78db7c86052e89b3980f89203_b.jpg)原生主题

![img](https://pic2.zhimg.com/v2-035720d2c646735f109b9ddb3f327b01_b.jpg)One Dark Pro主题

以上就是全部内容啦，如果你还有其他问题，欢迎私信我哦～

------

## 更新记录

- 10月22日更新：添加了-lm编译选项和code runner配置文件中的.exe扩展名，添加了faq。
- 11月27日更新：launch.json中externalConsole改为true，方便在调试过程中输入输出数据。

## FAQ

1. 编译时提示clang不是有效的命令或应用程序：检查是否正确配置clang的环境变量，配置文件中的clang路径是否正确
2. 提示找不到stdio.h：检查target是否正确配置。如果不是使用本文提供的mingw，target有可能不同，可以试试--target=x86_64-pc-mingw32
3. 编译没有问题，但是写代码的时候stdio.h等库下面被clang command adapter标了红线：打开clang command adapter的配置页面，在c和cxx的编译参数里都添加上target配置，具体的target参见本文其他内容。如果还是不行，那就禁用这个插件吧。
4. 引入math.h时提示找不到math.h库中的函数（例如提示sqrt函数未定义云云）：在编译选项中添加-lm，现在本文中的代码已经默认添加了这个编译选项。