
@echo off
chcp 65001
REM 确保在obj和output目录中操作


python generate_rc.py

REM 切换到obj目录
cd obj

REM 使用RC编译器编译资源文件
rc.exe /v resources.rc

REM 编译DLL
cl.exe /LD ..\icon_library.cpp resources.res /Fe:..\output_dll\icon_library.dll

REM 返回原目录
cd ..




REM 清理中间文件
del /Q obj\*.obj obj\*.exp obj\*.lib

echo 编译完成，DLL已生成在output目录中 