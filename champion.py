"""
包含与机器人使用的单个棋盘槽相关的所有信息
"""


class Champion:
    """英雄类，包含关于棋盘或备战区上的单个单位的信息"""

    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    def __init__(self, name: str, coords: tuple, build, slot: int, size: int, final_comp: bool,
                 trait1: str,
                 trait2: str,
                 trait3: str) -> None:
        self.name: str = name
        self.coords: tuple = coords
        self.build = build
        self.index: int = slot
        self.size: int = size
        self.completed_items: list = []
        self.current_building: list = []
        self.final_comp: bool = final_comp

        # 英雄羁绊
        self.traits = [trait1, trait2, trait3]

    def does_need_items(self) -> bool:
        """返回 英雄 实例是否需要装备"""
        return len(self.completed_items) != 3 or len(self.build) + len(self.current_building) == 0

    def does_need_trait(self) -> bool:
        """返回 英雄 实例是否可以装备纹章"""
        return len(self.completed_items) != 3 and len(self.build) + len(self.current_building) <= 2

    def hero_type(self) -> bool:
        """获取英雄类型 前排返回False  后排返回True """
        return 0 <= self.index <= 13

    def check_trait(self, item: str) -> bool:
        """根据通过的物品检查冠军是否有特定的特质。"""
        # 移除物品名称中的“徽章”
        trait_to_check = item.replace("纹章", "")
        # 检查这个特质是否存在于冠军的特质中
        return trait_to_check not in self.traits and "纹章" in item


if __name__ == '__main__':
    cm = Champion("阿木木", None, None, None, None, None, "监察", None, None)
    print(cm.check_trait("锁子甲"))
    print(cm.check_trait("监察纹章"))
