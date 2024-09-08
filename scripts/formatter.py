import re
from pathlib import Path

# BUG
def convert_obsidian_callouts(cwd: str="../docs"):
    '''
    root: cwd: str
    '''
    root =  Path(cwd)
    assert not root.exists()
    for file_path in root.rglob("*.md"):
    # 读取文件内容
        with file_path.open(encoding="utf-8") as file:
            content = file.read()

        # 定义正则表达式模式
        pattern = r"^(>\s*\[!(\w+)\]\s*)(.*?)$((?:\n>\s*.*$)*)"

        def replace_format(match):
            callout_type = match.group(2)
            title = match.group(3).strip()
            content = match.group(4)

            # 处理内容
            if content:
                content = content.replace("\n>", "\n").strip()

            # 构建新的格式
            new_format = f"!!! {callout_type}"
            if title:
                new_format += f" {title}"
            if content:
                new_format += f"\n{content}"

            return new_format

        # 使用正则表达式替换内容
        new_content = re.sub(pattern, replace_format, content, flags=re.MULTILINE)

        # 将修改后的内容写回文件
        with file_path.open("w", encoding="utf-8") as file:
            file.write(new_content)

        print(f"File {file_path} has been updated.")


# 使用示例
convert_obsidian_callouts()
