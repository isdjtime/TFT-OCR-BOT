"""
    最后更新时间: 2024年11月22日
        英雄和装备数据
"""

# 基本装备
BASIC_ITEM: set[str] = {"暴风之剑", "反曲之弓", "无用大棒", "女神之泪", "锁子甲", "负极斗篷", "巨人腰带", "金铲铲",
                        "拳套", "金锅锅"}
# 合成装备
COMBINED_ITEMS: set[str] = {"死亡之刃",
                            "巨人杀手",
                            "海克斯科技枪刃",
                            "朔极之矛",
                            "饮血剑",
                            "无尽之刃",
                            "鬼索的狂暴之刃",
                            "斯塔堤克电刃",
                            "泰坦的坚决",
                            "卢安娜的飓风",
                            "纳什之牙",
                            "最后的轻语",
                            "灭世者的死亡之帽",
                            "大天使之杖",
                            "离子火花",
                            "莫雷洛秘典",
                            "珠光护手",
                            "蓝霸符",
                            "救赎",
                            "正义之手",
                            "棘刺背心",
                            "石像鬼石板甲",
                            "日炎斗篷",
                            "巨龙之爪",
                            "水银",
                            "狂徒铠甲",
                            "金铲铲冠冕",
                            "窃贼手套",
                            "破防者",
                            "斯特拉克的挑战护手",
                            "冕卫",
                            "适应性头盔",
                            "薄暮法袍",
                            "红霸符",
                            "坚定之心",
                            "夜之锋刃",
                            "圣盾使的誓约",

                            "征服者纹章",
                            "炮手纹章",
                            "蓝发小队纹章",
                            "迅击战士纹章",
                            "黑色玫瑰纹章",
                            "法师纹章",
                            "家人纹章",
                            "先知纹章",
                            "执法官纹章",
                            "哨兵纹章",
                            "海克斯机械纹章",
                            "搏击手纹章",
                            "试验品纹章",
                            "格斗家纹章",
                            "野火帮纹章",
                            "伏击专家纹章",

                            "金锅铲冠冕",
                            "金锅锅冠冕",
                            }

# 辅助装备
SUPPORT_ITEM: set[str] = {"军团圣盾",
                          "女妖面纱",
                          "余烬之冠",
                          "殉道美德",
                          "能量圣杯",
                          "钢铁烈阳之匣",
                          "无用大宝石",
                          "黑曜石切割者",
                          "兰顿之兆",
                          "静止法衣",
                          "基克的先驱",
                          "灵风",
                          "兹若特传送门",
                          "辅助手套",
                          "永恒烈焰",
                          "骑士之誓",
                          "月石再生器",
                          "恶意",
                          "不稳定的财宝箱",
                          }

# 不可合成的
NON_CRAFTABLE_ITEMS: set[str] = {"次级英雄复制器", "英雄复制器", "大亨之铠", "投机者之刃", "坚定投资器", "装备拆卸器",
                                 "装备重铸器",
                                 "炼金男爵纹章", "皮城学院纹章", "极客纹章", "狙神纹章", "监察纹章", "统领纹章",
                                 "失稳炼金罐",
                                 "行刑官链锯刃",
                                 "裂肉者",
                                 "皮城海克斯护甲",
                                 "毒素倾泻",
                                 "烈性病毒",
                                 "完美行刑官链锯刃",
                                 "完美裂肉者",
                                 "完美失稳炼金罐",
                                 "完美皮城海克斯护甲",
                                 "完美毒素倾泻",
                                 "完美烈性病毒",
                                 "行刑官链锯刃 II",
                                 "裂肉者 II",
                                 "失稳炼金罐 II",
                                 "皮城海克斯护甲 II",
                                 "毒素倾泻 II",
                                 "烈性病毒 II",
                                 "微光绽放",
                                 "微光绽放 II",
                                 "完美微光绽放",
                                 "电震军刀",
                                 "电震军刀 II",
                                 "完美电震军刀",
                                 "回收护手",
                                 "回收左轮枪",
                                 "回收装置",
                                 "高维传家宝",
                                 "便携异常点"
                                 "杰作升级"
                                 }
# 奥恩装备
ORNN_ITEMS: set[str] = {"生命盔甲",
                        "死亡之蔑",
                        "魔蕴",
                        "三相之力",
                        "永恒凛冬",
                        "金币收集者",
                        "中娅悖论",
                        "碎舰者",
                        "诡术师之镜",
                        "狙击手的专注",
                        "冥火之拥",
                        "铁匠手套",
                        "钻石之手",
                        "飞升护符",
                        "黑暗吸血鬼节杖",
                        "鱼骨头",
                        "迷离风衣",
                        "视界专注",
                        "连指手套",
                        "无终恨意",
                        "疾射火炮",
                        "激发之匣",
                        "卢登的激荡",
                        "密银黎明",
                        "暗行者之爪",
                        "幽魂弯刀",
                        "枯萎珠宝",
                        "智慧末刃",
                        "禁忌雕像",
                        "巫妖之祸",
                        "光盾徽章",
                        "探索者的护臂",
                        }

# 光明装备
SACRED_ITEMS: set[str] = {
    "意志破坏者",
    "余烬之冠",
    "巨像的传承",
    "壁垒的誓言",
    "光辉之刃",
    "恶魔杀手",
    "海克斯科技生命之刃",
    "希拉娜之矛",
    "黎明锋刃",
    "福佑饮血剑",
    "斯特拉克的究极盾牌",
    "天顶锋刃",
    "鬼索的清算",
    "斯塔缇克狂热",
    "泰坦的誓言",
    "卢安娜的风暴",
    "男爵赠礼",
    "永恒轻语",
    "灭世者的飞升之帽",
    "阿福天使之杖",
    "皇家冕盾",
    "神圣离子火花",
    "莫雷洛圣典",
    "圣洁珠光护手",
    "圣蓝祝福",
    "千变者贾修",
    "赦除",
    "绝对正义之拳",
    "瑰刺背心",
    "天神石板甲",
    "日光斗篷",
    "巨龙意志",
    "星体结界",
    "至速水银",
    "狂徒之傲",
    "光明窃贼手套",
}

SACRED_MATCHED_GROUP = {
    "意志破坏者": "破防者",
    "余烬之冠": "红霸符",
    "巨像的传承": "坚定之心",
    "壁垒的誓言": "圣盾使的誓约",
    "光辉之刃": "死亡之刃",
    "恶魔杀手": "巨人杀手",
    "海克斯科技生命之刃": "海克斯科技枪刃",
    "希拉娜之矛": "朔极之矛",
    "黎明锋刃": "夜之锋刃",
    "福佑饮血剑": "饮血剑",
    "斯特拉克的究极盾牌": "斯特拉克的挑战护手",
    "天顶锋刃": "无尽之刃",
    "鬼索的清算": "鬼索的狂暴之刃",
    "斯塔缇克狂热": "斯塔缇克电刃",
    "泰坦的誓言": "泰坦的坚决",
    "卢安娜的风暴": "卢安娜的飓风",
    "男爵赠礼": "纳什之牙",
    "永恒轻语": "最后的轻语",
    "灭世者的飞升之帽": "灭世者的死亡之帽",
    "阿福天使之杖": "大天使之杖",
    "皇家冕盾": "冕卫",
    "神圣离子火花": "离子火花",
    "莫雷洛圣典": "莫雷洛秘典",
    "圣洁珠光护手": "珠光护手",
    "圣蓝祝福": "蓝霸符",
    "千变者贾修": "适应性头盔",
    "赦除": "救赎",
    "绝对正义之拳": "正义之手",
    "瑰刺背心": "棘刺背心",
    "天神石板甲": "石像鬼石板甲",
    "日光斗篷": "日炎斗篷",
    "巨龙意志": "巨龙之爪",
    "星体结界": "薄暮法袍",
    "至速水银": "水银",
    "狂徒之傲": "狂徒铠甲",
    "光明窃贼手套": "窃贼手套"
}

# 前排预设装备名单
FRONTLINE_ITEMS: set[str] = {
    "锁子甲",
    "负极斗篷",
    "巨人腰带",
    "军团圣盾",
    "女妖面纱",
    "殉道美德",
    "钢铁烈阳之匣",
    "无用大宝石",
    "兰顿之兆",
    "兹若特传送门",
    "永恒烈焰",
    "骑士之誓",
    "不稳定的财宝箱",
    "大亨之铠",
    "生命盔甲",
    "永恒凛冬",
    "碎舰者",
    "诡术师之镜",
    "密银黎明",
    "暗行者之爪",
    "幽魂弯刀",
    "禁忌雕像",
    "光盾徽章",
    "探索者的护臂",
    "破防者"

}

# 后排预设装备名单
REAR_ITEMS: set[str] = {
    "暴风之剑",
    "反曲之弓",
    "无用大棒",
    "女神之泪",
    "拳套",
    "余烬之冠",
    "能量圣杯",
    "黑曜石切割者",
    "静止法衣",
    "基克的先驱",
    "灵风",
    "辅助手套",
    "月石再生器",
    "恶意",
    "投机者之刃",
    "坚定投资器",
    "死亡之蔑",
    "魔蕴",
    "三相之力",
    "金币收集者",
    "中娅悖论",
    "狙击手的专注",
    "冥火之拥",
    "铁匠手套",
    "钻石之手",
    "飞升护符",
    "黑暗吸血鬼节杖",
    "鱼骨头",
    "迷离风衣",
    "视界专注",
    "连指手套",
    "无终恨意",
    "疾射火炮",
    "激发之匣",
    "卢登的激荡",
    "枯萎珠宝",
    "智慧末刃",
    "巫妖之祸",

}

ITEMS: set[str] = BASIC_ITEM.union(COMBINED_ITEMS).union(SUPPORT_ITEM).union(NON_CRAFTABLE_ITEMS).union(
    ORNN_ITEMS).union(SACRED_ITEMS)

# 默认英雄信息 英雄名称:金币:x,占人口容量:x,羁绊1:羁绊信息,羁绊2:羁绊信息,羁绊3:羁绊信息
CHAMPIONS: dict[str, dict[str, int | str]] = {
    "辛吉德": {"Gold": 1, "Board Size": 1, "Trait1": "炼金男爵", "Trait2": "哨兵", "Trait3": ""},
    "阿木木": {"Gold": 1, "Board Size": 1, "Trait1": "海克斯机械", "Trait2": "监察", "Trait3": ""},
    "德莱文": {"Gold": 1, "Board Size": 1, "Trait1": "铁血征服者", "Trait2": "搏击手", "Trait3": ""},
    "特朗德尔": {"Gold": 1, "Board Size": 1, "Trait1": "极客", "Trait2": "格斗家", "Trait3": ""},
    "斯特卜": {"Gold": 1, "Board Size": 1, "Trait1": "执法官", "Trait2": "格斗家", "Trait3": ""},
    "麦迪": {"Gold": 1, "Board Size": 1, "Trait1": "执法官", "Trait2": "狙神", "Trait3": ""},
    "爆爆": {"Gold": 1, "Board Size": 1, "Trait1": "家人", "Trait2": "极客", "Trait3": "伏击专家"},
    "蔚奥莱": {"Gold": 1, "Board Size": 1, "Trait1": "家人", "Trait2": "搏击手", "Trait3": ""},
    "薇古丝": {"Gold": 1, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "先知", "Trait3": ""},
    "德莱厄斯": {"Gold": 1, "Board Size": 1, "Trait1": "铁血征服者", "Trait2": "监察", "Trait3": ""},
    "艾瑞莉娅": {"Gold": 1, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "哨兵", "Trait3": ""},
    "婕拉": {"Gold": 1, "Board Size": 1, "Trait1": "试验品", "Trait2": "法师", "Trait3": ""},
    "拉克丝": {"Gold": 1, "Board Size": 1, "Trait1": "皮城学院", "Trait2": "法师", "Trait3": ""},
    "莫甘娜": {"Gold": 1, "Board Size": 1, "Trait1": "黑色玫瑰", "Trait2": "先知", "Trait3": ""},

    "烈娜塔": {"Gold": 2, "Board Size": 1, "Trait1": "炼金男爵", "Trait2": "先知", "Trait3": ""},
    "卡蜜尔": {"Gold": 2, "Board Size": 1, "Trait1": "执法官", "Trait2": "伏击专家", "Trait3": ""},
    "阿卡丽": {"Gold": 2, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "迅击战士", "Trait3": ""},
    "瑟提": {"Gold": 2, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "格斗家", "Trait3": ""},
    "芮尔": {"Gold": 2, "Board Size": 1, "Trait1": "铁血征服者", "Trait2": "哨兵", "Trait3": "先知"},
    "弗拉基米尔": {"Gold": 2, "Board Size": 1, "Trait1": "黑色玫瑰", "Trait2": "监察", "Trait3": "法师"},
    "吉格斯": {"Gold": 2, "Board Size": 1, "Trait1": "极客", "Trait2": "统领", "Trait3": ""},
    "范德尔": {"Gold": 2, "Board Size": 1, "Trait1": "家人", "Trait2": "监察", "Trait3": ""},
    "泽丽": {"Gold": 2, "Board Size": 1, "Trait1": "野火帮", "Trait2": "狙神", "Trait3": ""},
    "魔腾": {"Gold": 2, "Board Size": 1, "Trait1": "海克斯机械", "Trait2": "迅击战士", "Trait3": ""},
    "蕾欧娜": {"Gold": 2, "Board Size": 1, "Trait1": "皮城学院", "Trait2": "哨兵", "Trait3": ""},
    "崔丝塔娜": {"Gold": 2, "Board Size": 1, "Trait1": "外交官", "Trait2": "炮手", "Trait3": ""},
    "厄加特": {"Gold": 2, "Board Size": 1, "Trait1": "试验品", "Trait2": "搏击手", "Trait3": "炮手"},

    "布里茨": {"Gold": 3, "Board Size": 1, "Trait1": "海克斯机械", "Trait2": "统领", "Trait3": ""},
    "伊泽瑞尔": {"Gold": 3, "Board Size": 1, "Trait1": "皮城学院", "Trait2": "蓝发小队", "Trait3": "炮手"},
    "卡西奥佩娅": {"Gold": 3, "Board Size": 1, "Trait1": "黑色玫瑰", "Trait2": "统领", "Trait3": ""},
    "史密奇": {"Gold": 3, "Board Size": 1, "Trait1": "炼金男爵", "Trait2": "伏击专家", "Trait3": ""},
    "崔妮": {"Gold": 3, "Board Size": 1, "Trait1": "炼金男爵", "Trait2": "格斗家", "Trait3": ""},
    "洛里斯": {"Gold": 3, "Board Size": 1, "Trait1": "执法官", "Trait2": "哨兵", "Trait3": ""},
    "刀疤": {"Gold": 3, "Board Size": 1, "Trait1": "野火帮", "Trait2": "监察", "Trait3": ""},
    "努努和威朗普": {"Gold": 3, "Board Size": 1, "Trait1": "试验品", "Trait2": "格斗家", "Trait3": "先知"},
    "娜美": {"Gold": 3, "Board Size": 1, "Trait1": "外交官", "Trait2": "法师", "Trait3": ""},
    "普朗克": {"Gold": 3, "Board Size": 1, "Trait1": "极客", "Trait2": "双形战士", "Trait3": "搏击手"},
    "克格莫": {"Gold": 3, "Board Size": 1, "Trait1": "海克斯机械", "Trait2": "狙神", "Trait3": ""},
    "崔斯特": {"Gold": 3, "Board Size": 1, "Trait1": "执法官", "Trait2": "迅击战士", "Trait3": ""},
    "斯维因": {"Gold": 3, "Board Size": 1, "Trait1": "铁血征服者", "Trait2": "双形战士", "Trait3": "法师"},

    "希尔科": {"Gold": 4, "Board Size": 1, "Trait1": "炼金男爵", "Trait2": "统领", "Trait3": ""},
    "蔚": {"Gold": 4, "Board Size": 1, "Trait1": "执法官", "Trait2": "搏击手", "Trait3": ""},
    "艾克": {"Gold": 4, "Board Size": 1, "Trait1": "野火帮", "Trait2": "极客", "Trait3": "伏击专家"},
    "蒙多医生": {"Gold": 4, "Board Size": 1, "Trait1": "试验品", "Trait2": "统领", "Trait3": ""},
    "图奇": {"Gold": 4, "Board Size": 1, "Trait1": "试验品", "Trait2": "狙神", "Trait3": ""},
    "俄洛伊": {"Gold": 4, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "哨兵", "Trait3": ""},
    "伊莉丝": {"Gold": 4, "Board Size": 1, "Trait1": "黑色玫瑰", "Trait2": "双形战士", "Trait3": "格斗家"},
    "黑默丁格": {"Gold": 4, "Board Size": 1, "Trait1": "皮城学院", "Trait2": "先知", "Trait3": ""},
    "库奇": {"Gold": 4, "Board Size": 1, "Trait1": "极客", "Trait2": "炮手", "Trait3": ""},
    "盖伦": {"Gold": 4, "Board Size": 1, "Trait1": "外交官", "Trait2": "监察", "Trait3": ""},
    "安蓓萨": {"Gold": 4, "Board Size": 1, "Trait1": "外交官", "Trait2": "铁血征服者", "Trait3": "迅击战士"},
    "佐伊": {"Gold": 4, "Board Size": 1, "Trait1": "", "Trait2": "", "Trait3": ""},

    "凯特琳": {"Gold": 5, "Board Size": 1, "Trait1": "执法官", "Trait2": "狙神", "Trait3": ""},
    "玛尔扎哈": {"Gold": 5, "Board Size": 1, "Trait1": "海克斯机械", "Trait2": "先知", "Trait3": ""},
    "乐芙兰": {"Gold": 5, "Board Size": 1, "Trait1": "黑色玫瑰", "Trait2": "法师", "Trait3": ""},
    "杰斯": {"Gold": 5, "Board Size": 1, "Trait1": "皮城学院", "Trait2": "双形战士", "Trait3": ""},
    "兰博": {"Gold": 5, "Board Size": 1, "Trait1": "机械公敌", "Trait2": "极客", "Trait3": "哨兵"},
    "塞薇卡": {"Gold": 5, "Board Size": 1, "Trait1": "百变铁手", "Trait2": "炼金男爵", "Trait3": "搏击手"},
    "金克丝": {"Gold": 5, "Board Size": 1, "Trait1": "蓝发小队", "Trait2": "伏击专家", "Trait3": ""},
    "莫德凯撒": {"Gold": 5, "Board Size": 1, "Trait1": "铁血征服者", "Trait2": "统领", "Trait3": ""},
}

ROUNDS: set[str] = {"1-1", "1-2", "1-3", "1-4",
                    "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8",
                    "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8",
                    "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7", "4-8",
                    "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7", "5-8",
                    "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7", "6-8",
                    "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7", "7-8"}

SECOND_ROUND: set[str] = {"1-2"}

# 选秀回合
CAROUSEL_ROUND: set[str] = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND: set[str] = {"1-3", "1-4", "2-7", "3-7", "4-6", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND: set[str] = {"2-1", "2-2", "2-3", "2-5", "2-6",
                       "3-1", "3-2", "3-3", "3-5", "3-6",
                       "4-1", "4-2", "4-3", "4-5",
                       "5-1", "5-2", "5-3", "5-5", "5-6",
                       "6-1", "6-2", "6-3", "6-5", "6-6",
                       "7-1", "7-2", "7-3", "7-5", "7-6"}
# 拾取战利品回合
PICKUP_ROUNDS: set[str] = {"2-1", "3-1", "4-1", "4-3", "5-1", "6-1", "7-1"}

ANVIL_ROUNDS: set[str] = {"2-1", "2-5", "3-1", "3-5", "4-1", "4-5", "5-1", "5-5", "6-1", "6-5", "7-1", "7-5"}

# 强化符文回合
AUGMENT_ROUNDS: set[str] = {"2-1", "3-2", "4-2"}

# 这些回合给装备
ITEM_PLACEMENT_ROUNDS: set[str] = {
    "2-1", "2-5", "2-7",
    "3-3", "3-5", "3-7",
    "4-2", "4-3", "4-4", "4-7",
    "5-1", "5-2", "5-3", "5-4", "5-5", "5-7",
    "6-1", "6-2", "6-3", "6-5", "6-6", "6-7",
    "7-1", "7-2", "7-3", "7-5", "7-6", "7-7"
}
# 刚开始的回合
ENCOUNTER_ROUNDS: set[str] = {"0-0"}

# 自动投降回合
FINAL_COMP_ROUND = "5-5"

# 合成表
FULL_ITEMS = {
    "死亡之刃": ("暴风之剑", "暴风之剑"),
    "巨人杀手": ("暴风之剑", "反曲之弓"),
    "海克斯科技枪刃": ("暴风之剑", "无用大棒"),
    "朔极之矛": ("暴风之剑", "女神之泪"),
    "饮血剑": ("暴风之剑", "负极斗篷"),
    "无尽之刃": ("暴风之剑", "拳套"),
    "斯特拉克的挑战护手": ("暴风之剑", "巨人腰带"),
    "夜之锋刃": ("暴风之剑", "锁子甲"),
    "征服者纹章": ("暴风之剑", "金铲铲"),
    "炮手纹章": ("暴风之剑", "金锅锅"),

    "鬼索的狂暴之刃": ("反曲之弓", "无用大棒"),
    "斯塔缇克电刃": ("反曲之弓", "女神之泪"),
    "泰坦的坚决": ("反曲之弓", "锁子甲"),
    "卢安娜的飓风": ("反曲之弓", "负极斗篷"),
    "纳什之牙": ("反曲之弓", "巨人腰带"),
    "最后的轻语": ("反曲之弓", "拳套"),
    "红霸符": ("反曲之弓", "反曲之弓"),
    "蓝发小队纹章": ("反曲之弓", "金铲铲"),
    "迅击战士纹章": ("反曲之弓", "金锅锅"),

    "灭世者的死亡之帽": ("无用大棒", "无用大棒"),
    "大天使之杖": ("无用大棒", "女神之泪"),
    "离子火花": ("无用大棒", "负极斗篷"),
    "莫雷洛秘典": ("无用大棒", "巨人腰带"),
    "珠光护手": ("无用大棒", "拳套"),
    "冕卫": ("无用大棒", "锁子甲"),
    "黑色玫瑰纹章": ("无用大棒", "金铲铲"),
    "法师纹章": ("无用大棒", "金锅锅"),

    "蓝霸符": ("女神之泪", "女神之泪"),
    "救赎": ("女神之泪", "巨人腰带"),
    "正义之手": ("女神之泪", "拳套"),
    "适应性头盔": ("女神之泪", "负极斗篷"),
    "圣盾使的誓约": ("女神之泪", "锁子甲"),
    "家人纹章": ("女神之泪", "金铲铲"),
    "先知纹章": ("女神之泪", "金锅锅"),

    "棘刺背心": ("锁子甲", "锁子甲"),
    "石像鬼石板甲": ("锁子甲", "负极斗篷"),
    "日炎斗篷": ("锁子甲", "巨人腰带"),
    "坚定之心": ("锁子甲", "拳套"),
    "执法官纹章": ("锁子甲", "金铲铲"),
    "哨兵纹章": ("锁子甲", "金锅锅"),

    "巨龙之爪": ("负极斗篷", "负极斗篷"),
    "水银": ("负极斗篷", "拳套"),
    "海克斯机械纹章": ("负极斗篷", "金铲铲"),
    "搏击手纹章": ("负极斗篷", "金锅锅"),

    "狂徒铠甲": ("巨人腰带", "巨人腰带"),
    "破防者": ("巨人腰带", "拳套"),
    "薄暮法袍": ("巨人腰带", "负极斗篷"),
    "试验品纹章": ("巨人腰带", "金铲铲"),
    "格斗家纹章": ("巨人腰带", "金锅锅"),

    "窃贼手套": ("拳套", "拳套"),
    "野火帮纹章": ("金铲铲", "拳套"),
    "伏击专家纹章": ("金锅锅", "拳套"),
    "金铲铲冠冕": ("金铲铲", "金铲铲"),
    "金锅铲冠冕": ("金铲铲", "金锅锅"),
    "金锅锅冠冕": ("金锅锅", "金锅锅"),

    "次级英雄复制器": ("次级英雄复制器", "次级英雄复制器"),
    "英雄复制器": ("英雄复制器", "英雄复制器"),
}
# 铁砧奇遇
ANVIL_PORTALS: list[str] = [
    "基础装备锻造器",
]
# 假人等奇遇
DUMMY_PORTALS: list[str] = [
    "魔像训练师",
]

def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """根据字符串（英雄名称）返回英雄购买需要的金币"""
    return CHAMPIONS[champion]["Gold"]
