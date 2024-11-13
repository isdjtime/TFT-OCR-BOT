"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
Items will be placed on the top champion first, and prioritize building items on the left.
"""

COMP = {
    "\u963f\u5361\u4e3d": {
        "board_position": 22,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u5361\u8428\u4e01": {
        "board_position": 21,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "\u8d6b\u5361\u91cc\u59c6": {
        "board_position": 27,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "\u8d3e\u514b\u65af": {
        "board_position": 26,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "\u827e\u5e0c": {
        "board_position": 1,
        "items": [],
        "level": 2,
        "final_comp": False
    },
    "\u83f2\u5965\u5a1c": {
        "board_position": 23,
        "items": ["\u996e\u8840\u5251", "\u6cf0\u5766\u7684\u575a\u51b3", "\u65af\u7279\u62c9\u514b\u7684\u6311\u6218\u62a4\u624b"],
        "level": 3,
        "final_comp": True
    },
    "\u5361\u7279\u7433\u5a1c": {
        "board_position": 24,
        "items": ["\u6b63\u4e49\u4e4b\u624b", "\u79bb\u5b50\u706b\u82b1", "\u82b1\u4ed9\u738b\u5195"],
        "level": 3,
        "final_comp": True
    },
    "\u6d1b": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u5c3c\u83c8": {
        "board_position": 15,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u683c\u6e29": {
        "board_position": 17,
        "items": ["\u73e0\u5149\u62a4\u624b", "\u6b63\u4e49\u4e4b\u624b", "\u84dd\u9738\u7b26"],
        "level": 3,
        "final_comp": True
    },
    "\u5df4\u5fb7": {
        "board_position": 0,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u83ab\u7518\u5a1c": {
        "board_position": 16,
        "items": ["\u72c2\u66b4\u6218\u58eb\u7eb9\u7ae0", "\u996e\u8840\u5251"],
        "level": 3,
        "final_comp": True
    },
    "\u7c73\u5229\u6b27": {
        "board_position": 6,
        "items": [],
        "level": 3,
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
    "狂暴战士之徽",
    "狂暴战士之冕",
    "潘朵拉的装备",
    "四费增援",
    "投资",
    "漫游训练师",
    "吾剑听命于您",
    "同排活力",
    "双排",
    "激昂墓志铭",
    "飞升",
    "天生二星",



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
    "降档",
    "抛硬币",
    "休战",
    "贪婪困境",



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
    "变形重组器",
    "运力不足",
    "精致古董",
    "金制拆卸器",
    "节外生枝",
    "开摆",
    "重启任务",
    "开摆",
    "不是今天",
    "主打一个陪伴",
    "碰撞测试假人",
    "双喜临门",
    "替罪羊",
    "辅助宝库",
    "法师之徽",
    "命运之子之徽",

    "花仙子之徽",
    "咖啡甜心之徽",
    "次元术士之徽",
    "时间学派之徽",

    "堡垒卫士之徽",
    "学者之徽",
    "术师之徽",
    "重装战士之徽",
    "复苏者之徽",
    "魔战士之徽",
]


def champions_to_buy() -> dict:
    """返回需要购买英雄的数量 以达到目标星级"""
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
