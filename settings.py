"""
    程序参数设置
"""

"""系统设置"""
GAME_HWND_NAME = 'League of Legends (TM) Client'  # 检测游戏加载窗口名
USE_GPU = False  # 英伟达显卡设置 True AMD或其他显卡设置 False
UI_FONT = 'Microsoft YaHei'  # 设置屏幕标记字体 -->  'STCaiyun','Microsoft YaHei'

"""OCR引擎设置"""
DET_DB_SCORE_MODE = 'fast'  # fast是根据polygon的外接矩形边框内的所有像素计算平均得分，slow是根据原始polygon内的所有像素计算平均得分，计算速度相对较慢一些，但是更加准确一些。
USE_MP = True  # 是否开启多进程预测 True False
TOTAL_PROCESS_NUM = 4  # 开启的进程数，USE_MP为True时生效

"""游戏挂机设置"""
QUEUE_ID = 1090  # 1090匹配 1100排位
FORFEIT = False  # 是否主动投降
FORFEIT_TIME = 600  # 多久投降 单位 秒 目前10分钟投降

"""游戏运营设置"""
MIN_GOLD = 6  # 最小预留金币 开启梭哈后生效
MAX_GOLD = 56  # 最大多少金币 50吃利息 默认预留56金币
HEALTH = 40  # 低于生命值开启梭哈模式
STORE_COUNT = 8  # 梭哈一波 每次连续刷新多少次商店
RANDOM_ITEM = True  # 梭哈模式 是否随机给装备
MAX_ITEM = 9  # 当有 n 个装备后就随机给 装备栏最多10件
RANDOM_MAX_ITEM = True  # 当有 n 个装备后就随机给 开关
UPGRADE_LEVEL = [8,9,10]  # 指定等级回合不购买经验
BUY_EXP_REFRESH_STORE = True  # 购买经验循环是否刷新商店
