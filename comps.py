"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
Items will be placed on the top champion first, and prioritize building items on the left.
"""

COMP = {
    "\u8d6b\u5361\u91cc\u59c6": {
        "board_position": 21,
        "items": ["\u5c0f\u871c\u8702\u7eb9\u7ae0"],
        "level": 2,
        "final_comp": True
    },
    "\u5854\u59c6": {
        "board_position": 22,
        "items": ["\u5723\u76fe\u4f7f\u7684\u8a93\u7ea6", "\u82f1\u96c4\u590d\u5236\u5668", "\u547d\u8fd0\u4e4b\u5b50\u7b26\u5370"],
        "level": 2,
        "final_comp": True
    },
    "\u5e03\u91cc\u8328": {
        "board_position": 26,
        "items": ["\u5195\u536b", "\u72c2\u5f92\u94e0\u7532", "\u79bb\u5b50\u706b\u82b1"],
        "level": 3,
        "final_comp": True
    },
    "\u52aa\u52aa": {
        "board_position": 27,
        "items": ["\u7a83\u8d3c\u624b\u5957", "\u6b21\u7ea7\u82f1\u96c4\u590d\u5236\u5668"],
        "level": 3,
        "final_comp": True
    },
    "\u963f\u72f8": {
        "board_position": 0,
        "items": ["\u6b21\u7ea7\u82f1\u96c4\u590d\u5236\u5668", "\u5c0f\u871c\u8702\u7eb9\u7ae0"],
        "level": 2,
        "final_comp": True
    },
    "\u6cfd\u62c9\u65af": {
        "board_position": 2,
        "items": ["\u5c0f\u871c\u8702\u7eb9\u7ae0"],
        "level": 3,
        "final_comp": True
    },
    "\u5409\u683c\u65af": {
        "board_position": 4,
        "items": ["\u84dd\u9738\u7b26", "\u706d\u4e16\u8005\u7684\u6b7b\u4ea1\u4e4b\u5e3d", "\u7eb3\u4ec0\u4e4b\u7259"],
        "level": 3,
        "final_comp": True
    },
    "\u514b\u683c\u83ab": {
        "board_position": 5,
        "items": ["\u6714\u6781\u4e4b\u77db", "\u7ea2\u9738\u7b26", "\u6b21\u7ea7\u82f1\u96c4\u590d\u5236\u5668"],
        "level": 3,
        "final_comp": True
    },
    "\u7ef4\u8fe6": {
        "board_position": 6,
        "items": [],
        "level": 2,
        "final_comp": True
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
# The ones on the top will be prioritized for selection.
# For those augments names with suffixes like I, II, III, such as 'Cybernetic Uplink II',
# You only need to add 'Cybernetic Uplink' in the list to cover all three levels.

#某些增强没有逻辑，这意味着如果它们包含在这里，机器人将不知道要做什么
#(任何改变游戏玩法或添加到板凳上的内容)。
#顶部的将被优先选择。
#对于那些后缀为I、II、III的扩展名，例如“Cybernetic Uplink II”，
#你只需要在列表中添加“Cybernetic Uplink”就可以覆盖所有三个级别。

# 强化白名单
AUGMENTS: list[str] = [
    "潘朵拉的装备",
    "潘朵拉的备战席",
    "白银门票",
    "团队建设",
    "D个痛快",
    "辅助魔像",
    "新人入队",
    "咒刃",
    "魔杖",
    "棱彩门票",
    "便携锻炉",
    "大百宝袋",
    "小蜜蜂之冕",
    "英勇福袋",
    "小蜜蜂之徽",
    "电震攻击",
    "最佳蜜友",
]

# 魔杖BUFF白名单
WANDS: list[str] = [
    "低阶胜负手",
    "升档",
    "连上加连",
    "免费刷新术",
    "掷骰子",
    "快速悬赏",
    "伯爵",
    "巨大化",

    "召唤假人",
    "盾墙",
    "召唤苍蓝雕纹魔像",
    "功能性拉满",
    "终极飞升",
    "人寿保险",
    "装甲之灵",
    "秘术之灵",
    "神器化",
    "余震",
    "海克斯爆炸",
    "日炎巫术",
    "约德尔之灵",
    "法术反制",
    "收割者",

    "死亡",
    "审判",

    "好好学习",
    "魔镜",
    "拷贝猫",
    "低阶祈愿术",
    "愈心美食",
    "刻苦训练",
    "战斗专精",
    "粘腻手指",
    "高阶祈愿术",
    "月光仪式",

    "丰功伟绩",



]

# 强化黑名单
AVOID_AUGMENTS: list[str] = [
    ""
]


def champions_to_buy() -> dict:
    """Creates a list of champions to buy during the game"""
    champs_to_buy: dict = {}
    for champion, champion_data in COMP.items():
        if champion_data["level"] == 1:
            champs_to_buy[champion] = 1
        elif champion_data["level"] == 2:
            champs_to_buy[champion] = 3
        elif champion_data["level"] == 3:
            champs_to_buy[champion] = 9
        else:
            raise ValueError("Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """创建棋盘上没有冠军的位置列表"""
    container: list = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
