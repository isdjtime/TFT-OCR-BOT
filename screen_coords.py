"""
包含机器人使用的静态屏幕坐标
Screen coords for 1920x1080 screens
(x, y, x+w, y+h) for Vec4 locations, (x, y) for Vec2 locations
"""

from vec4 import Vec4, GameWindow
from vec2 import Vec2

#备战期位置
BENCH_HEALTH_POS: list[Vec4] = [
    Vec4(GameWindow(369, 650, 472, 757)),
    Vec4(GameWindow(485, 650, 588, 757)),
    Vec4(GameWindow(601, 650, 704, 757)),
    Vec4(GameWindow(728, 650, 831, 757)),
    Vec4(GameWindow(844, 650, 947, 757)),
    Vec4(GameWindow(960, 650, 1063, 757)),
    Vec4(GameWindow(1076, 650, 1179, 757)),
    Vec4(GameWindow(1192, 650, 1295, 757)),
    Vec4(GameWindow(1308, 650, 1411, 757)),
]
#装备栏
ITEM_POS: list[list] = [
    [Vec2(273, 753), Vec4(GameWindow(373, 794, 611, 824))],
    [Vec2(348, 737), Vec4(GameWindow(451, 778, 689, 808))],
    [Vec2(289, 692), Vec4(GameWindow(391, 734, 629, 764))],
    [Vec2(356, 676), Vec4(GameWindow(458, 717, 696, 747))],
    [Vec2(307, 631), Vec4(GameWindow(410, 674, 648, 704))],
    [Vec2(323, 586), Vec4(GameWindow(422, 628, 658, 658))],
    [Vec2(407, 679), Vec4(GameWindow(507, 721, 745, 751))],
    [Vec2(379, 632), Vec4(GameWindow(482, 674, 721, 704))],
    [Vec2(396, 582), Vec4(GameWindow(497, 625, 735, 655))],
    [Vec2(457, 628), Vec4(GameWindow(559, 670, 797, 701))],
]
#一轮POS
ROUND_POS: Vec4 = Vec4(GameWindow(753, 10, 870, 34))
#第一轮
ROUND_POS_ONE: Vec4 = Vec4(GameWindow(0, 0, 40, 24), use_screen_offset=False)
#第二轮
ROUND_POS_TWO: Vec4 = Vec4(GameWindow(16, 0, 56, 24), use_screen_offset=False)
#第三轮
ROUND_POS_THREE: Vec4 = Vec4(GameWindow(71, 0, 110, 24), use_screen_offset=False)
#圆形相遇图标
ROUND_ENCOUNTER_ICON_POS: list[list[Vec2, Vec4]] = [
    [Vec2(833, 20), Vec4(GameWindow(890, 49, 1218, 75))],
    [Vec2(869, 20), Vec4(GameWindow(926, 49, 1254, 75))],
    [Vec2(905, 20), Vec4(GameWindow(962, 49, 1290, 75))],
    [Vec2(941, 20), Vec4(GameWindow(998, 49, 1326, 75))],
    [Vec2(977, 20), Vec4(GameWindow(1034, 49, 1362, 75))],
    [Vec2(1013, 20), Vec4(GameWindow(1070, 49, 1398, 75))],
    [Vec2(1049, 20), Vec4(GameWindow(1106, 49, 1434, 75))],
    [Vec2(1085, 20), Vec4(GameWindow(1142, 49, 1470, 75))],
]
#商店
SHOP_POS: Vec4 = Vec4(GameWindow(481, 1039, 1476, 1070))

# 英雄商店截图位置 0-4
CHAMP_NAME_POS: list[Vec4] = [
    Vec4(GameWindow(3, 5, 120, 24), use_screen_offset=False),
    Vec4(GameWindow(204, 5, 320, 24), use_screen_offset=False),
    Vec4(GameWindow(407, 5, 522, 24), use_screen_offset=False),
    Vec4(GameWindow(608, 5, 712, 24), use_screen_offset=False),
    Vec4(GameWindow(808, 5, 912, 24), use_screen_offset=False),
]

#新赛季的魔杖BUFF购买位置
WAND_POS: Vec4 = Vec4(GameWindow(1292, 1043, 1440, 1068))
WAND_LOC: Vec2 = Vec2(1400, 1024)

#面板名称loc
PANEL_NAME_LOC: Vec4 = Vec4(GameWindow(1707, 320, 1821, 342))

#钱包位置
GOLD_POS: Vec4 = Vec4(GameWindow(870, 883, 920, 909))

#铁砧
ANVIL_MSG_POS: Vec4 = Vec4(GameWindow(818, 838, 932, 859))
#现在退出
EXIT_NOW_POS: Vec4 = Vec4(GameWindow(910, 560, 1029, 583))

#每回合符文Title位置
AUGMENT_POS: list[Vec4] = [
    Vec4(GameWindow(420, 532, 687, 570)),
    Vec4(GameWindow(825, 532, 1095, 570)),
    Vec4(GameWindow(1233, 532, 1500, 570)),
]
#增强地方
AUGMENT_LOC: list[Vec2] = [Vec2(549, 445), Vec2(955, 445), Vec2(1365, 445)]
#增加卷
AUGMENT_ROLL: list[Vec2] = [Vec2(549, 875), Vec2(960, 875), Vec2(1363, 875)]
#胜利POS
VICTORY_POS: Vec4 = Vec4(GameWindow(906, 560, 1030, 587))
#买的地方
BUY_LOC: list[Vec2] = [
    Vec2(575, 992),
    Vec2(775, 992),
    Vec2(975, 992),
    Vec2(1175, 992),
    Vec2(1375, 992),
]
#物品领取箱
ITEM_PICKUP_LOC: list[Vec2] = [
    Vec2(1440, 611),
    Vec2(406, 544),
    Vec2(1440, 486),
    Vec2(469, 440),
    Vec2(1380, 381),
    Vec2(644, 323),
    Vec2(1297, 262),
    Vec2(590, 215),
]
#板凳LOC
BENCH_LOC: list[Vec2] = [
    Vec2(425, 777),
    Vec2(542, 777),
    Vec2(658, 777),
    Vec2(778, 777),
    Vec2(892, 777),
    Vec2(1010, 777),
    Vec2(1128, 777),
    Vec2(1244, 777),
    Vec2(1359, 777),
]

# 这个列表从左下(0)到右上(27) 棋盘位置
BOARD_LOC: list[Vec2] = [
    Vec2(581, 651),
    Vec2(707, 651),
    Vec2(839, 651),
    Vec2(966, 651),
    Vec2(1091, 651),
    Vec2(1222, 651),
    Vec2(1349, 651),
    Vec2(532, 571),
    Vec2(660, 571),
    Vec2(776, 571),
    Vec2(903, 571),
    Vec2(1022, 571),
    Vec2(1147, 571),
    Vec2(1275, 571),
    Vec2(609, 494),
    Vec2(723, 494),
    Vec2(841, 494),
    Vec2(962, 494),
    Vec2(1082, 494),
    Vec2(1198, 494),
    Vec2(1318, 494),
    Vec2(557, 423),
    Vec2(673, 423),
    Vec2(791, 423),
    Vec2(907, 423),
    Vec2(1019, 423),
    Vec2(1138, 423),
    Vec2(1251, 423),
]
#旋转木马LOC
CAROUSEL_LOC: Vec2 = Vec2(964, 620)
#立即退出loc
EXIT_NOW_LOC: Vec2 = Vec2(963, 575)
#购买xp loc
BUY_XP_LOC: Vec2 = Vec2(364, 964)
#刷新LOC
REFRESH_LOC: Vec2 = Vec2(364, 1039)
#默认的代码行
DEFAULT_LOC: Vec2 = Vec2(60, 222)
#健康的地方
HEALTH_LOC: Vec2 = Vec2(1897, 126)
#投降LOC
SURRENDER_LOC: Vec2 = Vec2(771, 843)
#交出两枚loc
SURRENDER_TWO_LOC: Vec2 = Vec2(832, 489)
