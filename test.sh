#!/bin/bash
file="target.txt"

# 备份原文件
cp "$file" "${file}.bak"

# 处理逻辑：非空行且不以!结尾的行末尾添加!
sed -i -e '/^[[:space:]]*$/d' -e 's/[[:space:]]*$//' -e '/^$/d' -e 's/[^!]$/&!/' "$file"

echo "处理完成。原文件已备份为 ${file}.bak"