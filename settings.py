"""

"""

"""系统设置"""
GAME_HWND_NAME = 'League of Legends (TM) Client'  # 检测游戏加载窗口名
USE_GPU = False  # 英伟达显卡设置 True AMD或其他显卡设置 False
UI_FONT = '也字工厂招牌体'  # 设置屏幕标记字体  'STCaiyun' ->华文彩云  'Microsoft YaHei' ->微软雅黑
DET_DB_SCORE_MODE = 'slow'  # fast是根据polygon的外接矩形边框内的所有像素计算平均得分，slow是根据原始polygon内的所有像素计算平均得分，计算速度相对较慢一些，但是更加准确一些。
USE_MP = False  # 是否开启多进程预测 True False
TOTAL_PROCESS_NUM = 6  # 开启的进程数，USE_MP为True时生效

"""游戏设置"""
QUEUE_ID = 1090  # 1090匹配 1100排位
FORFEIT = False  # 是否主动投降
FORFEIT_TIME = 600  # 多久投降单位 秒 目前10分钟投降
MIN_GOLD = 6  # 最小预留金币
MAX_GOLD = 50  # 最大多少金币
HEALTH = 40  # 低于生命值开启梭哈
