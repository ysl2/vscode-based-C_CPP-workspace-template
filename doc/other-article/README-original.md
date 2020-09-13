# VSCode-CPP-Template
VSCode开发C++项目的通用工程模板，方便快捷的实现编译、调试功能  
使用GCC编译器  
使用CMake配置编译

该模板适用于使用VSCode开发C++跨平台项目  
如果项目只是基于Windows平台，那么建议使用Visual Studio

## 配置
### 软件安装
* MinGW-W64  
    在Windows系统中使用GCC作为编译器，因此需要MinGW-W64

* CMake
    使用CMake生成MakeFile，并执行编译

* Python
    编写build.py来配置并执行cmake命令

### VSCode插件安装
* C/C++  
  配置文件为.vscode目录下的tasks.json, launch.json和setting.json  
* Include Autocomplete  
   配置文件为.vscode/c_cpp_properties.json  
* CMake  
  该插件只用于为编写CMakeList.txt提供便利，包括高亮显示、函数提示等  
  我们并不适使用该插件来执行cmake命令

### 路径配置
* 配置环境变量，将MinGW-W64/bin添加到Path中
* c_cpp_properties.json中的 compilerPath 配置为g++.exe的绝对路径
* launch.json中的 miDebuggerPath 配置为g++.exe的绝对路径

## 使用
### 开始新项目
复制Template目录，并将Template目录名修改为工程名称即可

### 编译、调试和运行
* Ctrl + Shift + R 选择task执行  
    tasks.json中共配置了5个task，分别为：  
    * build(debug):   
      编译debug版本，编译的可执行文件在bin/debug目录下   
    * build(release):  
      编译debug版本，编译的可执行文件在bin/release目录下   
    * run(debug):  
      执行bin/debug目录的可执行文件  
    * run(release):  
      执行bin/relase目录的可执行文件
    * clean  
      清理编译结果：删除build目录下的所有内容，已经bin/debug，bin/release下的可执行文件

* F5调试  
    在调试前，会自动执行build(debug)的task，生成最新的debug版本

### 关于build.py文件
目前网上找到的介绍，都是在tasks.json中直接配置编译指令  
如果项目只有几个文件，那么这种方式很方便  

但是对于几十几百个文件的工程，这种方式就力不从心  
编译过程中的各种设置，以及头文件搜索路径、第三方库、第三方库搜索路径  
这些信息如果全部在tasks.json中填写，一则导致tasks.json文件太大不方便，二是无法执行各种复杂的逻辑判断，毕竟tasks.json只是一个json文件

因此，我们添加了一个build.py脚本来执行这些配置和逻辑判断，而在tasks.json中只是简单的调用该脚本
在build.py中，我们会执行cmake和make命令来完成编译

### 关于.vscode目录
该目录下是VSCode的配置文件，有的是VSCode本身使用，有的是插件使用，共有四个文件  

* c_cpp_properties.json  
  该配置文件用于设置代码显示的语法检查、代码跳转  
  例如: 在main.cpp中 
  ```
  #include "include1.h" 
  ```
  编辑器会提示无法找到include1.h文件，我们需要在该配置文件的includePath字段中填写include1.h所在的路径  
  我们在工程中为了方便，使用 ${workspaceFolder}/src/** 来包含src下的所有子目录

  注意：这里配置的头文件搜索路径，只与代码提示有关，与编译无关  
  编译时的头文件搜索路径在CMakeList.txt中配置

  同理
  ```
  "compilerPath": "C:/MinGW/bin/g++.exe",
  "cStandard": "c11",
  "cppStandard": "c++11"
  ```
  文件中配置的编译器信息也只用于语法检查、代码提示等功能，与编译无关
  编译时的相关设置在CMakeList.txt中配置
  
* launch.json  
  该配置文件为VSCode使用，用于配置调试相关的信息，其中最主要的字段是：
  ```
  "program": "${workspaceFolder}/bin/debug/${workspaceRootFolderName}.exe",
  "miDebuggerPath":"c:/MinGW/bin/gdb.exe",     
  ```
  分别指定调试的exe文件和调试器

* settings.json  
  一般配置信息，无须赘述

* tasks.json  
  该配置文件为VSCode使用，我们配置了5个task，参考上面的"编译、调试和运行"