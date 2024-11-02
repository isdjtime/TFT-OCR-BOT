"""
机器人执行从哪里开始并包含让机器人无限运行的游戏循环
"""

import multiprocessing
import time

import settings
from ui import UI
import auto_queue
from game import Game

def show_inform() -> None:
    print("TFT OCR BOT | https://github.com/NatureTao/TFT-OCR-BOT")
    print("关闭此窗口,以结束运行程序!")
    print("加载配置文件 setting.py")
    if settings.QUEUE_ID == 1100:
        game_mode = "排位赛"
    elif settings.QUEUE_ID == 1090:
        game_mode = "匹配赛"
    else:
        game_mode = f"[注意]当前选择房间ID不是下棋模式|当前ID =>{settings.QUEUE_ID}"
    print("当前挂机模式:", game_mode)

def game_loop(ui_queue: multiprocessing.Queue) -> None:
    """通过在循环中调用queue和game start，让程序无限期地运行"""
    while True:
        try:
            auto_queue.queue()
        except ConnectionError:
            print("本地服务器连接异常 正常重新连接")
            time.sleep(1)
            continue
        Game(ui_queue)


if __name__ == "__main__":

    message_queue = multiprocessing.Queue()
    overlay: UI = UI(message_queue)
    game_thread = multiprocessing.Process(target=game_loop, args=(message_queue,))

    show_inform()

    game_thread.start()
    overlay.ui_loop()
