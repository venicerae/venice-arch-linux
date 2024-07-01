import os
import re


def search_files(pattern, path='.'):
    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # 跳过二进制文件（这里简单地基于文件名，可以改进）
            if file_path.endswith(('.bin', '.o', '.obj', '.a', '.dll', '.exe', '.so')):
                continue

                # 尝试打开并搜索文件
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    line_number = 1
                    for line in lines:
                        if pattern in line:
                            print(f"{file_path}:{line_number}: {line.strip()}")
                        line_number += 1
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")

            # 主程序入口


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python ag.py PATTERN [PATH]")
        print("If no PATH is provided, search in current directory.")
        sys.exit(1)

    pattern = sys.argv[1]
    path = '.' if len(sys.argv) < 3 else sys.argv[2]

    search_files(pattern, path)