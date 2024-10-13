"""
一键安装环境
"""

import os

current_directory = os.getcwd()
REQUIREMENTS = 'requirements.txt'


if os.path.exists(os.path.join(current_directory,REQUIREMENTS)):
    print("\033[92m 找到requirements.txt文件，正在安装依赖......\033[0m")
    os.system('pip install -r requirements.txt')
else:
    print("\033[31m 在当前目录找不到requirements.txt文件 \033[0m")



input("请按 Enter(回车) 退出")
