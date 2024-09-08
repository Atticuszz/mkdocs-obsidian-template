import re
from pathlib import Path


# BUG
def convert_obsidian_callouts(cwd: str="../docs") -> None:
    """Convert callouts in cwd.

    Args:
        cwd (str, optional): _description_. Defaults to "../docs".

    """
    root =  Path(__file__).parents[1]/'docs'
    if not root.exists():
        raise FileExistsError
    for file_path in root.rglob("*.md"):
        with file_path.open(encoding="utf-8") as file:
            content = file.read()

        pattern = r"^(>\s*\[!(\w+)\]\s*)(.*?)$((?:\n>\s*.*$)*)"

        def replace_format(match):
            callout_type = match.group(2)
            title = match.group(3).strip()
            content = match.group(4)


            if content:
                # replace  '> ' with tab
                content = re.sub(r"^>\s?", "\t", content, flags=re.MULTILINE).rstrip()

            # new format
            new_format = f"!!! {callout_type}"
            if title:
                new_format += f" {title}"
            if content:
                new_format += f"{content}"

            return new_format


        new_content = re.sub(pattern, replace_format, content, flags=re.MULTILINE)


        with file_path.open("w", encoding="utf-8") as file:
            file.write(new_content)



convert_obsidian_callouts()
