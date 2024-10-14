"""
机器人执行从哪里开始并包含让机器人无限运行的游戏循环
"""

import multiprocessing

import settings
from ui import UI
import auto_queue
from game import Game


def game_loop(ui_queue: multiprocessing.Queue) -> None:
    """通过在循环中调用queue和game start，让程序无限期地运行"""
    while True:
        auto_queue.queue()
        Game(ui_queue)


if __name__ == "__main__":

    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))

    print("TFT OCR BOT | https://github.com/NatureTao/TFT-OCR-BOT")
    print("关闭此窗口,以结束运行程序!")
    print("加载配置文件 setting.py")
    if settings.QUEUE_ID == 1100:
        game_mode = "排位"
    else:
        game_mode = "匹配"
    print("匹配模式:", game_mode)
    game_thread.start()
    overlay.ui_loop()
