"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
Items will be placed on the top champion first, and prioritize building items on the left.
"""

COMP = {
    "\u5fb7\u83b1\u5384\u65af": {
        "board_position": 21,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u76d6\u4f26": {
        "board_position": 22,
        "items": ["\u65e5\u708e\u6597\u7bf7"],
        "level": 2,
        "final_comp": True
    },
    "\u5200\u75a4": {
        "board_position": 23,
        "items": ["\u72c2\u5f92\u94e0\u7532", "\u77f3\u50cf\u9b3c\u77f3\u677f\u7532", "\u6551\u8d4e","\u5de8\u9f99\u4e4b\u722a","\u6cf0\u5766\u7684\u575a\u51b3"],
        "level": 3,
        "final_comp": True
    },
    "\u963f\u6728\u6728": {
        "board_position": 24,
        "items": [],
        "level": 3,
        "final_comp": True
    },
    "\u8303\u5fb7\u5c14": {
        "board_position": 25,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u5f17\u62c9\u57fa\u7c73\u5c14": {
        "board_position": 27,
        "items": [],
        "level": 2,
        "final_comp": True
    },
    "\u514b\u683c\u83ab": {
        "board_position": 0,
        "items": ["\u9b3c\u7d22\u7684\u72c2\u66b4\u4e4b\u5203", "\u6d77\u514b\u65af\u79d1\u6280\u67aa\u5203", "\u5927\u5929\u4f7f\u4e4b\u6756"],
        "level": 3,
        "final_comp": True
    },
    "\u6cfd\u4e3d": {
        "board_position": 6,
        "items": ["\u65e0\u5c3d\u4e4b\u5203", "\u65af\u5854\u7f07\u514b\u7535\u5203", "\u9b3c\u7d22\u7684\u72c2\u66b4\u4e4b\u5203"],
        "level": 2,
        "final_comp": True
    },
    "\u5fb7\u83b1\u6587": {
        "board_position": 2,
        "items": ["\u9b3c\u7d22\u7684\u72c2\u66b4\u4e4b\u5203"],
        "level": 2,
        "final_comp": False
    }
}

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
# The ones on the top will be prioritized for selection.
# For those augments names with suffixes like I, II, III, such as 'Cybernetic Uplink II',
# You only need to add 'Cybernetic Uplink' in the list to cover all three levels.

# 某些增强没有逻辑，这意味着如果它们包含在这里，机器人将不知道要做什么
# (任何改变游戏玩法或添加到板凳上的内容)。
# 顶部的将被优先选择。
# 对于那些后缀为I、II、III的扩展名，例如“Cybernetic Uplink II”，
# 你只需要在列表中添加“Cybernetic Uplink”就可以覆盖所有三个级别。

# 强化白名单
AUGMENTS: list[str] = [
    "飓风呼啸",
    "幸运手套",
    "玻璃大炮",
    "巨大伙伴",
    "健康就是财富",
    "又一个异常突变",

]

# 异常突变白名单
ABRUPT_ANOMALY: list[str] = [
    "千刀斩",
    "火球",
    "连杀",

]

# 强化黑名单
AVOID_AUGMENTS: list[str] = [
    "我希望这个管用",
    "战地医生",
    "刀锋之舞",
    "炼金术士",
    "震惊巨魔",
    "超级巨星",
    "后援",
    "铁匠训练",
    "腐蚀",
    "假人化",
    "以眼还眼",
    "威力提升",
    "辅助挖矿",
    "巨型泰坦",
    "变形重组器",
    "后期专家",
    "潘朵拉的备战席",
    "联合抵抗",
    "不拘一格",
    "基础装备自助餐",
    "救援已在路上",
    "延迟开始",
    "重启任务",
    "休眠锻炉",
    "皮城学院之徽",
    "学术研究",
    "伏击专家之徽",
    "战利品爆炸",
    "炮手之徽",
    "火箭收藏",
    "海克斯机械之徽",
    "碎裂水晶",
    "格斗家之徽",
    "强力重击",
    "黑色玫瑰之徽",
    "禁忌魔法",
    "残暴复仇",
    "炼金男爵之徽",
    "底城争夺战",
    "征服者之徽",
    "诺克萨斯断头台",
    "统领之徽",
    "统领全场",
    "执法官之徽",
    "执法",
    "物竞天择",
    "野火帮之徽",
    "游击作战",
    "迅击战士之徽",
    "蓝发小队之徽",
    "肾上腺爆发",
    "极客之徽",
    "极客宝藏之顶",
    "哨兵之徽",
    "护盾猛击",
    "狙神之徽",
    "狙神之巢",
    "法师之徽",
    "奥术之惩",
    "先知之徽",
    "虚空召唤者",
    "血色契约",
    "监察之徽",
    "魔像化",
    "假人金币",
    "月光",
    "一对4",
    "塔防游戏",
    "卓尔不群",
    "闪若金鳞",
    "漫游训练师",
    "替罪羊",
    "辅助宝库",
    "便携锻炉",
    "皮城学院之冕",
    "伏击专家之冕",
    "炮手之冕",
    "海克斯机械之冕",
    "格斗家之冕",
    "炼金男爵之冕",
    "征服者之冕",
    "统领之冕",
    "执法官之冕",
    "野火帮之冕",
    "搏击手之冕",
    "迅击战士之冕",
    "蓝发小队之冕",
    "极客之冕",
    "哨兵之冕",
    "狙神之冕",
    "法师之冕",
    "先知之冕",
    "监察之冕",
    "近距离作战",
    "最终润色",
    "连串打击",
    "光明重构器",
    "狂暴到底",
    "不计代价",
    "暗巷交易",
    "遥遥领先",
    "我成C位了",
    "金鳞精粹",
    "假装摸鱼",
    "厄运保护",
    "克隆设施",

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


def get_key(comps, index: int) -> str:
    """
     @param comps:预设阵容列表
     @param index:查询英雄棋盘位置
     @return: 英雄名称
    """
    return next((k for k, v in comps.items() if any(goal == index for goal in v.values())), None)


if __name__ == '__main__':
    res = get_key(COMP, 0)
    print(res)
