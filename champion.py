"""
包含与机器人使用的单个棋盘槽相关的所有信息
"""


class Champion:
    """英雄类，包含关于棋盘或备战区上的单个单位的信息"""

    # pylint: disable=too-many-instance-attributes,too-few-public-methods,too-many-arguments

    def __init__(self, name: str, coords: tuple, build, slot: int, size: int, final_comp: bool) -> None:
        self.name: str = name
        self.coords: tuple = coords
        self.build = build
        self.index: int = slot
        self.size: int = size
        self.completed_items: list = []
        self.current_building: list = []
        self.final_comp: bool = final_comp

    def does_need_items(self) -> bool:
        """返回 英雄 实例是否需要装备"""
        return len(self.completed_items) != 3 or len(self.build) + len(self.current_building) == 0

    def hero_type(self) -> bool:
        """获取英雄类型 前排返回False  后排返回True """
        return 0 <= self.index <= 13
