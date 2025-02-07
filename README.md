# Icon Library DLL Generator

这是一个用于生成包含图标资源的 Windows DLL 的工具。  
This is a tool for generating a Windows DLL that contains icon resources.

该工具可以将图标文件编译到 DLL 中，方便在其他应用程序中使用。  
This tool can compile icon files into a DLL for easy use in other applications.

好比，`Total Commander`  
Similar to `Total Commander`.

## 环境要求

- Visual Studio 2022  
  Visual Studio 2022
- Python 3.x  
  Python 3.x
- Pillow 库 (用于图标处理)  
  Pillow library (for icon processing)

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. **准备编译环境**  
   **Prepare the compilation environment**

   - 启动 `x86 Native Tools Command Prompt for VS 2022`  
     Start `x86 Native Tools Command Prompt for VS 2022`
   - 或者运行以下命令设置编译环境：  
     Or run the following command to set up the compilation environment:
     ```batch
     cmd /k "C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvars32.bat"
     ```

2. **准备图标文件**  
   **Prepare the icon files**

   - 将需要打包的图标文件 (.png/jpg/icon 格式) 放入项目目录中的 input_pic  
     Place the icon files to be packed (.png/jpg/icon format) into the `input_pic` directory in the project.
   - 图标文件必须是正方形的  
     The icon files must be square.
   - 输出最大尺寸为 256x256 像素的 icon。这是 icon 本身的限制。  
     The output maximum size for the icon is 256x256 pixels, which is a limitation of the icon itself.

3. **生成 DLL**  
   **Generate the DLL**

   - 运行 build.bat 脚本：  
     Run the `build.bat` script:
     ```batch
     build.bat
     ```
   - 脚本会自动：  
     The script will automatically:
     - 将 PNG 文件转换为 ICO 格式  
       Convert PNG files to ICO format.
     - 生成资源文件  
       Generate resource files.
     - 编译生成 64 位 DLL  
       Compile and generate a 64-bit DLL.

4. **输出文件**  
   **Output files**
   - 生成的 DLL 文件位于 `output` 目录中  
     The generated DLL file is located in the `output` directory.
   - 中间文件位于 `obj` 目录中  
     Intermediate files are located in the `obj` directory.

## 目录结构

```project/
├── build.bat              # 编译脚本  
├── generate_rc.py         # 资源生成脚本  
├── icon_library.cpp       # DLL 源代码  
├── requirements.txt       # Python 依赖  
├── obj/                   # 编译中间文件  
├── input_pic/             # 输入图标文件  
├── icons/                 # 生成图标中间文件  
└── output/                # 输出目录  
```

## 注意事项

- 确保使用正确的 Visual Studio 命令提示符环境  
  Ensure you are using the correct Visual Studio command prompt environment.
- 图标文件必须是正方形的，且尺寸不超过 256x256，其他格式尺寸随意，会自动缩小到最大尺寸（但是也需要是正方形的）  
  Icon files must be square and no larger than 256x256; other formats can be of any size but will be automatically resized to the maximum size (still needs to be square).
- 编译过程会自动清理中间文件  
  The compilation process will automatically clean up intermediate files.
- 如果编译失败，请检查环境变量和依赖是否正确安装  
  If the compilation fails, please check that the environment variables and dependencies are correctly installed.

## 技术细节

- 使用交叉编译器生成 64 位 DLL  
  Uses a cross-compiler to generate a 64-bit DLL.
- 自动将图片转换为适当尺寸的 ICO 文件  
  Automatically converts images to the appropriate
- 支持的 ICO 尺寸：16x16, 32x32, 64x64, 128x128, 256x256
  Supported ICO sizes: 16x16, 32x32, 64x64, 128x128, 256x256


# 关于

- 本产品基于Apache协议开源。
- 作者 米哈( [@MrMiHa](https://t.me/MrMiHa) )是一个苦逼程序员，不是煤场奴工，有问题别太理直气壮的跑来下命令。
- 讨论群组是 : https://t.me/DeveloperTeamGroup 欢迎加入后玩耍
- 随意Fork，记得保留`关于`的内容。
- 【恰饭服务器推荐】这款：[2核3G--年32刀](https://my.racknerd.com/aff.php?aff=11705&pid=905) 
