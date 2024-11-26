"""
机器人执行从哪里开始并包含让机器人无限运行的游戏循环
"""

import multiprocessing
import sys
import time

import settings
from ui import UI
import auto_queue
from game import Game


def show_inform() -> None:
    print("TFT OCR BOT | https://github.com/NatureTao/TFT-OCR-BOT")
    print("关闭此窗口,以结束运行程序!")
    print("加载配置文件 setting.py")
    print("S13:双城之战2")
    if settings.QUEUE_ID == 1100:
        game_mode = "排位赛"
    elif settings.QUEUE_ID == 1090:
        game_mode = "匹配赛"
    else:
        game_mode = f"[注意]当前选择房间ID不是(匹配/排位)云顶模式|当前ID =>{settings.QUEUE_ID}"
    print("当前挂机模式:", game_mode)


def game_loop(ui_queue: multiprocessing.Queue) -> None:
    """通过在循环中调用queue和game start，让程序无限期地运行"""
    while True:
        try:
            auto_queue.queue()
            Game(ui_queue)
        except Exception as e:
            print("[!]本地游戏服务器连接失败,正在重新连接!")
            print(e)
            print(sys.exc_info())
            time.sleep(1)


if __name__ == "__main__":
    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))
    show_inform()
    game_thread.start()
    overlay.ui_loop()
