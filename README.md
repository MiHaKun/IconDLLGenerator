# Icon Library DLL Generator

这是一个用于生成包含图标资源的 Windows DLL 的工具。该工具可以将图标文件编译到 DLL 中，方便在其他应用程序中使用。好比，`Total Commander`

## 环境要求

- Visual Studio 2022
- Python 3.x
- Pillow 库 (用于图标处理)

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. **准备编译环境**

   - 启动 `x86 Native Tools Command Prompt for VS 2022`
   - 或者运行以下命令设置编译环境：
     ```batch
     cmd /k "C:\Program Files\Microsoft Visual Studio\2022\Professional\VC\Auxiliary\Build\vcvars32.bat"
     ```

2. **准备图标文件**

   - 将需要打包的图标文件 (.png/jpg/icon 格式) 放入项目目录中的 input_pic
   - 图标文件必须是正方形的
   - 输出最大尺寸为 256x256 像素的 icon。这是 icon 本身的限制。

3. **生成 DLL**

   - 运行 build.bat 脚本：
     ```batch
     build.bat
     ```
   - 脚本会自动：
     - 将 PNG 文件转换为 ICO 格式
     - 生成资源文件
     - 编译生成 64 位 DLL

4. **输出文件**
   - 生成的 DLL 文件位于 `output` 目录中
   - 中间文件位于 `obj` 目录中

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
- 图标文件必须是正方形的，且尺寸不超过 256x256，其他格式尺寸随意，会自动缩小到最大尺寸（但是也需要是正方形的）
- 编译过程会自动清理中间文件
- 如果编译失败，请检查环境变量和依赖是否正确安装

## 技术细节

- 使用 交叉编译器生成 64 位 DLL
- 自动将图片转换为适当尺寸的 ICO 文件
- 支持的 ICO 尺寸：16x16, 32x32, 64x64, 128x128, 256x256

## 关于
- 本产品基于Apache协议开源。
- 作者 米哈( @MrMiHa )是一个苦逼程序员，不是煤场奴工，有问题别太理直气壮的跑来下命令。
- 讨论群组是 : https://t.me/DeveloperTeamGroup 欢迎加入后玩耍
- 随意Fork，记得保留关于的内容。
- 【恰饭】服务器推荐RackNerd的。实际上，我也确实用这个。够便宜。这款就够：2核3G--年32刀
