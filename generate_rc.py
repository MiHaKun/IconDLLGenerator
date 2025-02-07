import os
import sys
import shutil
import random
import string
from PIL import Image


def ensure_dir(dir_path):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"创建目录: {dir_path}")


def generate_random_filename():
    """生成8位随机字符串作为文件名"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(8))


def convert_to_ico(input_path, output_path):
    """将图片转换为ICO文件，选择最合适的尺寸"""
    try:
        # 打开图片
        img = Image.open(input_path)

        # 确保图片是正方形的
        if img.width != img.height:
            print(f"警告: {input_path} 不是正方形图片，将被跳过")
            return False

        # 定义支持的ICO尺寸
        ico_sizes = [16, 32, 64, 128, 256]

        # 获取原图尺寸
        original_size = img.width  # 因为是正方形，width 和 height 相同

        # 选择最合适的尺寸（不大于原图的最大尺寸）
        target_size = max(size for size in ico_sizes if size <= original_size)

        # 转换为RGBA模式
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # 调整图片尺寸
        resized_img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)

        # 创建一个临时文件来保存调整后的PNG
        temp_png = output_path + ".temp.png"
        resized_img.save(temp_png, format="PNG")

        # 重新打开调整后的PNG并保存为ICO
        with Image.open(temp_png) as img_for_ico:
            img_for_ico.save(
                output_path, format="ICO", sizes=[(target_size, target_size)]
            )

        # 删除临时文件
        os.remove(temp_png)

        print(
            f"转换成功: {input_path} -> {output_path} (尺寸: {target_size}x{target_size})"
        )
        return True
    except Exception as e:
        print(f"转换失败 {input_path}: {str(e)}")
        return False


def clean_directory(dir_path):
    """清空目录内容"""
    if os.path.exists(dir_path):
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"清理文件失败 {file_path}: {str(e)}")


def generate_rc_file():
    # 定义所需的目录
    input_dir = "input_pic"
    icons_dir = "icons"
    obj_dir = "obj"
    output_dir = "output_dll"

    # 确保所需目录都存在
    for dir_path in [input_dir, icons_dir, obj_dir, output_dir]:
        ensure_dir(dir_path)

    # 清空icons目录
    clean_directory(icons_dir)

    # 处理输入文件
    icon_files = []
    supported_formats = {".png", ".jpg", ".jpeg", ".ico"}

    for filename in os.listdir(input_dir):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in supported_formats:
            input_path = os.path.join(input_dir, filename)
            new_filename = generate_random_filename()

            if file_ext == ".ico":
                # 如果是ico文件，直接复制到icons目录
                new_path = os.path.join(icons_dir, new_filename + ".ico")
                shutil.copy2(input_path, new_path)
                icon_files.append(os.path.basename(new_path))
                print(f"复制ICO文件: {input_path} -> {new_path}")
            else:
                # 转换其他格式为ico
                new_path = os.path.join(icons_dir, new_filename + ".ico")
                if convert_to_ico(input_path, new_path):
                    icon_files.append(os.path.basename(new_path))

    if not icon_files:
        print(f"错误: 在input_pic目录中没有找到可用的图片文件")
        return

    rc_content = []
    # 添加RC文件头
    rc_content.append("#include <windows.h>\n")

    # 生成资源定义
    for idx, filename in enumerate(icon_files):
        resource_id = idx + 1
        rc_content.append(f'{resource_id} ICON "..\\\\icons\\\\{filename}"')

    # 写入.rc文件到obj目录
    rc_file_path = os.path.join(obj_dir, "resources.rc")
    with open(rc_file_path, "w", encoding="utf-8") as rc_file:
        rc_file.write("\n".join(rc_content))

    print(f"成功生成resources.rc文件，包含 {len(icon_files)} 个图标资源")


if __name__ == "__main__":
    generate_rc_file()
