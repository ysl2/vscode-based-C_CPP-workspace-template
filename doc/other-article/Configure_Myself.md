# 我自己的配置过程

[TOC]

---

## 说明

gcc/g++比较容易上手，clang/clang++有一定难度。**二者选择一种即可，并且二者有冲突。**

本仓库有两个分支：仓库中的master分支是用gcc/g++作为编译时期编译器，仓库中的clang分支是用clang/clang++作为编译时期编译器。这两种无论哪种方案，在调试时都是使用gcc/g++作为调试时期编译器。

> 这是我自己给的定义，目的是能够说清楚请注意编译和调试的区别。如果你想直接运行代码，而不调试，就算编译时期。如果你需要调试，就算调试时期。这种定义方法可能并不正确，但是你能明白就好了

## 一、gcc/g++作为编译时期编译器

这种方法只安装mingw就行。但是如果你也安装了LLVM，二者可以不合并，也可以合并，这都无所谓。而对于clang（也就是第二种方案），二者需要进行合并。但是无论是否合并，都必须配置环境变量：

1. 如果没有合并，需要配置mingw的bin到环境变量和LLVM的bin到环境变量（如果你安装了LLVM的话，没安装就只配置mingw的bin）
2. 如果合并了，只需要把LLVM的bin配置到环境变量里面

此时需要安装vscode扩展：ms-vscode.cpptools，code runner

关于四个文件的配置：（使用这四个文件时，一定确保你已经正确配置环境变量）

c_cpp_properties.json可以直接删掉（并且我个人十分建议删掉），但是mingw的环境变量一定要弄好。删掉c_cpp_properties.json之后，vscode会按照默认的方式寻找你的gcc/g++，但是能够找到的前提是你已经正确地配置了mingw的环境变量。

lanunch.json什么都不用改，已经调整到了最佳状态。

settings.json里面需要小改动（这个小改动可选，对程序运行的正确性不会有影响）：关于"files.defaultLanguage": "c++", 字段，如果你想新建文件直接默认用C，就把里面的c++改成c（去掉两个+号即可）。其他地方都不用改。

tasks.json里面，如果你要用c，把"command": "g++"的g++改成gcc（删掉两个c，加两个+号）

## 二、clang/clang++作为编译时期编译器

这种方法需要先安装LLVM，然后安装mingw-w64到LLVM的路径里面。如果你下的mingw是压缩包那种，可以直接解压到LLVM文件夹里面。也就是把mingw合并到LLVM里面

合并完成后，配置LLVM的bin的环境变量，一定注意配置要正确，否则下面的配置肯定全都不好使了。

此时需要安装vscode扩展：ms-vscode.cpptools，code runner，clang command adapter

关于四个文件的配置：

c_cpp_properties.json我没试过是否能删，但是我认为如果可以删掉，优先还是选择删掉比较好。因为删掉就会使用vscode的默认配置，毕竟你自己配置肯定和人家给你配置有一些区别。

launch.json不用改。

settings.json和上面一样，里面需要小改动（这个小改动可选，对程序运行的正确性不会有影响）：关于"files.defaultLanguage": "cpp", 字段，如果你想新建文件直接默认用C，就把里面的c++改成c（去掉两个+号即可）。其他地方都不用改。

> 此处进行说明：我不知道在这个字段里面，用cpp和c++是否有区别，也不知道是否会导致不一样的后果。但是我可以确保：这个字段不会对编译运行和调试产生影响，因此这个字段无伤大雅。

tasks.json里面，如果你要用c，把"command": "clang++"的g++改成gcc（删掉两个c，加两个+号）

## 补充

实际上clang最配套的插件应该是clangd，而不是clang command adapter。但是我用clangd的时候，一直提示找不到头文件，而此时我编译和运行都正常，只是强迫症受不了这种提示信息。这很明显是我的vscode关于头文件的路径没有设置正确，而不凑巧的是我并不知道如何处理这个问题。因此我放弃了clangd而改用clang command adapter。改用clang command adapter后，我不确定智能提示是用的ms-vscode.cpptools的提示，还是用的clang的提示，反正从我个人的感觉，应该是智能提示还是用的cpptools，但是编译和运行时的提示是用的clang，不知道这种想法是否正确。总之，经过了两天的忙活，好歹我也能用上clang了（不完美）。