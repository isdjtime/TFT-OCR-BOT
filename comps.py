"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
Items will be placed on the top champion first, and prioritize building items on the left.
"""

COMP = {
    "\u65af\u83ab\u5fb7": {
        "board_position": 0,
        "items": ["\u65e0\u5c3d\u4e4b\u5203", "\u82f1\u96c4\u590d\u5236\u5668", "\u9b3c\u7d22\u7684\u72c2\u66b4\u4e4b\u5203", "\u5de8\u4eba\u6740\u624b"],
        "level": 3,
        "final_comp": True
    },
    "\u97e6\u9c81\u65af": {
        "board_position": 3,
        "items": ["\u82f1\u96c4\u590d\u5236\u5668","\u7a83\u8d3c\u624b\u5957"],
        "level": 3,
        "final_comp": True
    },
    "\u8bfa\u59c6\u5e0c": {
        "board_position": 6,
        "items": ["\u6714\u6781\u4e4b\u77db", "\u65e0\u5c3d\u4e4b\u5203", "\u6700\u540e\u7684\u8f7b\u8bed"],
        "level": 3,
        "final_comp": True
    },
    "\u65af\u7ef4\u56e0": {
        "board_position": 16,
        "items": ["\u9b54\u795e\u4f7f\u8005\u7eb9\u7ae0"],
        "level": 2,
        "final_comp": True
    },
    "\u4f0a\u8389\u4e1d": {
        "board_position": 18,
        "items": ["\u730e\u624b\u7eb9\u7ae0"],
        "level": 3,
        "final_comp": True
    },
    "\u59ae\u853b": {
        "board_position": 23,
        "items": ["\u7a83\u8d3c\u624b\u5957"],
        "level": 2,
        "final_comp": True
    },
    "\u5185\u745f\u65af": {
        "board_position": 25,
        "items": ["\u9501\u5b50\u7532", "\u88c5\u5907\u62c6\u5378\u5668", "\u9501\u5b50\u7532"],
        "level": 3,
        "final_comp": True
    },
    "\u5e0c\u74e6\u5a1c": {
        "board_position": 26,
        "items": ["\u77f3\u50cf\u9b3c\u77f3\u677f\u7532", "\u6b21\u7ea7\u82f1\u96c4\u590d\u5236\u5668", "\u82f1\u96c4\u590d\u5236\u5668", "\u6551\u8d4e", "\u5195\u536b"],
        "level": 3,
        "final_comp": True
    },
    "\u8d1d\u857e\u4e9a": {
        "board_position": 24,
        "items": ["\u996e\u8840\u5251", "\u82f1\u96c4\u590d\u5236\u5668", "\u65af\u7279\u62c9\u514b\u7684\u6311\u6218\u62a4\u624b", "\u6cf0\u5766\u7684\u575a\u51b3", "\u4e00\u4e2a\u8f7b\u98df\u70b9\u5fc3"],
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
    "潘朵拉的装备",
    "升星冒险",
    "换形师之徽",
    "C位的觉悟",
    "飞升",
    "天生二星",
    "永恒成长",
    "龙族专精",
    "殉道者",



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
    "狂暴战士之徽",
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
