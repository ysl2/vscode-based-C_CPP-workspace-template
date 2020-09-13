import os
import sys
import shutil

buildType = sys.argv[1]
projName = sys.argv[2]

def clean():
    print(">>>>>>>>>>>>>>>>>>>> Begin cleaning >>>>>>>>>>>>>>>>>>>>")

    # 删除build目录
    shutil.rmtree(os.getcwd() + "\\build")

    # 删除debug exe
    debugExePath = "bin/debug/" + projName + ".exe"
    if os.path.exists(debugExePath):
        os.remove(debugExePath)

    # 删除release exe
    releaseExePath = "bin/release/" + projName + ".exe"
    if os.path.exists(releaseExePath):
        os.remove(releaseExePath)

    # 创建build目录
    os.mkdir("build")

    print("\n<<<<<<<<<<<<<<<<<<<< End cleaning <<<<<<<<<<<<<<<<<<<<")

def compile():
    print(">>>>>>>>>>>>>>>>>>>> Begin compiling >>>>>>>>>>>>>>>>>>>>")
    print("Build Type is " + buildType)

    # 判断debug还是release
    buildTypeString = "-DBUILD_TYPE=debug"
    if buildType == "release":
        # release之前执行clean()
        # clean()
        buildTypeString = "-DBUILD_TYPE=release"

    # 获取工程名称
    projNameString = "-DPROJ_NAME=" + projName

    # 切换工作区到build目录下
    print("\nchange work dir to build\n")
    os.chdir("build")

    # cmake
    print("Begin camke...")
    cmd = 'cmake .. -G "MinGW Makefiles" '
    cmd += buildTypeString + " "
    cmd += projNameString + " "
    os.system(cmd)

    # make
    print("\nBegin make...")
    os.system("mingw32-make")

    print("\n<<<<<<<<<<<<<<<<<<<< End compiling <<<<<<<<<<<<<<<<<<<<")

# 如果不存在build目录，则创建
if not os.path.exists("build"):
    os.mkdir("build")

# 判断是编译还是clean
if buildType == "clean":
    # 执行清理
    clean()
else:
    # 执行编译
    compile()
