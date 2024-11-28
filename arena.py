"""
处理游戏内部的棋盘/备战区状态
机器人用于决策的其他变量
"""
import threading
from time import sleep

from PIL import ImageGrab

import game_assets
import mk_functions
import screen_coords
import settings
from champion import Champion
import comps
import ocr
import game_functions
import arena_functions
from vec4 import Vec4


class Arena:
    """
       Arena类，处理游戏逻辑，如棋盘和备战区状态
    """

    # pylint: disable=too-many-instance-attributes,too-many-public-methods
    def __init__(self, message_queue) -> None:
        self.message_queue = message_queue
        self.board_size = 0
        self.bench: list[None] = [None] * 9  # 备战区
        self.anvil_free: list[bool] = [False] * 9
        self.board: list = []
        self.board_unknown: list = []
        self.unknown_slots: list = comps.get_unknown_slots()
        self.champs_to_buy: dict = comps.champions_to_buy()
        self.board_names: list = []
        self.items: list = []
        self.final_comp = False
        self.level = 0
        self.augment_roll = True
        self.spam_roll = False
        self.HP: list = [None]

    def fix_bench_state(self) -> None:
        """遍历备战区并修复未知的槽位"""
        bench_occupied: list = arena_functions.bench_occupied_check()
        for index, slot in enumerate(self.bench):
            if slot is None and bench_occupied[index]:
                mk_functions.right_click(screen_coords.BENCH_LOC[index].get_coords())
                champ_name: str = arena_functions.valid_champ(
                    ocr.get_text(
                        screenxy=screen_coords.PANEL_NAME_LOC.get_coords(),
                        scale=3
                    )
                )
                if self.champs_to_buy.get(champ_name, 0) > 0:
                    print(
                        f"  备战区[{champ_name}]存在升星队列中"
                    )
                    self.bench[index] = Champion(
                        name=champ_name,
                        coords=screen_coords.BENCH_LOC[index].get_coords(),
                        build=comps.COMP[champ_name]["items"].copy(),
                        slot=index,
                        size=game_assets.CHAMPIONS[champ_name]["Board Size"],
                        final_comp=comps.COMP[champ_name]["final_comp"],

                    )
                    self.champs_to_buy[champ_name] -= 1

                else:
                    print(
                        f" 备战区[{champ_name}]不在升星队列中"
                    )
                    self.bench[index] = "?"
                continue
            if isinstance(slot, str) and not bench_occupied[index]:
                self.bench[index] = None
                continue
            if isinstance(slot, Champion) and not bench_occupied[index]:
                self.bench[index] = None

    def bought_champion(self, name: str, slot: int) -> None:
        """
            购买英雄 并创建英雄实例
        """
        # print(f"bought_champion [name]==>{name} ")

        self.bench[slot] = Champion(
            name=name,
            coords=screen_coords.BENCH_LOC[slot].get_coords(),
            build=comps.COMP[name]["items"].copy(),
            slot=slot,
            size=game_assets.CHAMPIONS[name]["Board Size"],
            final_comp=comps.COMP[name]["final_comp"],

        )

        mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
        sleep(0.5)
        self.fix_bench_state()

    def have_champion(self) -> Champion | None:
        """检测备战区是否存在英雄"""
        return next(
            (
                champion
                for champion in self.bench
                if isinstance(champion, Champion)
                   and champion.name not in self.board_names
            ),
            None,
        )

    def move_known(self, champion: Champion) -> None:
        """将英雄移动到棋盘上"""
        print(f"  移动[{champion.name}]到棋盘")

        destination: tuple = screen_coords.BOARD_LOC[
            comps.COMP[champion.name]["board_position"]
        ].get_coords()

        mk_functions.left_click(champion.coords)
        sleep(0.1)
        mk_functions.left_click(destination)
        champion.coords = destination
        self.board.append(champion)
        self.board_names.append(champion.name)
        self.bench[champion.index] = None
        champion.index = comps.COMP[champion.name]["board_position"]
        self.board_size += champion.size

    def move_unknown(self) -> None:
        """将未识别的英雄移动到棋盘上"""
        for index, champion in enumerate(self.bench):
            if isinstance(champion, str):
                print(f"  移动 {champion} 到棋盘")
                # print(f"move_unknown Debug =>{index,champion,isinstance(champion, str)}")
                mk_functions.left_click(screen_coords.BENCH_LOC[index].get_coords())
                sleep(0.1)
                mk_functions.left_click(
                    screen_coords.BOARD_LOC[
                        self.unknown_slots[len(self.board_unknown)]
                    ].get_coords()
                )
                self.bench[index] = None
                self.board_unknown.append(champion)
                self.board_size += 1
                return

    def sell_bench(self) -> None:
        """出售备战区所有英雄"""
        for index, _ in enumerate(self.bench):
            mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
            self.bench[index] = None

    def unknown_in_bench(self) -> bool:
        """出售备战区所有英雄"""
        return any(isinstance(slot, str) for slot in self.bench)

    def move_champions(self) -> None:
        """将英雄移动到棋盘上"""
        self.level: int = arena_functions.get_level()
        while self.level > self.board_size:
            champion: Champion | None = self.have_champion()
            if champion is not None:
                self.move_known(champion)
            elif self.unknown_in_bench():
                self.move_unknown()
            else:
                bought_unknown = False
                shop: list = arena_functions.get_shop()
                count = 0  # 循环计数
                for champion in shop:
                    count += 1

                    gold: int = arena_functions.get_gold()
                    # 购买未知英雄
                    # champion[1] 是英雄名字 champion[0] 是英雄下标
                    # TODO 代码优化
                    common = list()  # 获取预设阵容的羁绊信息
                    for name in self.board_names:
                        common.append(game_assets.CHAMPIONS[name]["Trait1"])
                        common.append(game_assets.CHAMPIONS[name]["Trait2"])
                        common.append(game_assets.CHAMPIONS[name]["Trait3"])
                    common = set(list(filter(None, common)))

                    hero = list()
                    if champion[1].__len__() != 0:
                        hero.append(game_assets.CHAMPIONS[champion[1]]["Trait1"])
                        hero.append(game_assets.CHAMPIONS[champion[1]]["Trait2"])
                        hero.append(game_assets.CHAMPIONS[champion[1]]["Trait3"])
                        hero = list(filter(None, hero))

                    character = False
                    none = True
                    priority = 0
                    for group in hero:
                        if group in common:
                            priority += 1
                        if priority >= 2:
                            character = True
                            none = False
                            break

                            # 如果真的没有相同羁绊的奕子就随机买
                    if none and self.level > self.board_size or count == shop.__len__():
                        character = True

                    valid_champ: bool = (
                            champion[1] in game_assets.CHAMPIONS
                            and game_assets.champion_gold_cost(champion[1]) <= gold
                            and game_assets.champion_board_size(champion[1]) == 1
                            and self.champs_to_buy.get(champion[1], -1) < 0
                            and champion[1] not in self.board_unknown
                            and character
                    )

                    if valid_champ:
                        none_slot: int = arena_functions.empty_slot()
                        mk_functions.left_click(
                            screen_coords.BUY_LOC[champion[0]].get_coords()
                        )
                        sleep(0.2)
                        self.bench[none_slot] = f"{champion[1]}"
                        self.move_unknown()
                        bought_unknown = True
                        break

                if not bought_unknown:
                    print("  需清空备战区初始化")
                    self.sell_bench()
                    return

    def replace_unknown(self) -> None:
        """替换掉未识别的英雄"""
        champion: Champion | None = self.have_champion()
        if len(self.board_unknown) > 0 and champion is not None:
            mk_functions.press_e(
                screen_coords.BOARD_LOC[
                    self.unknown_slots[len(self.board_unknown) - 1]
                ].get_coords()
            )
            self.board_unknown.pop()
            self.board_size -= 1
            self.move_known(champion)

    def bench_cleanup(self) -> None:
        """出售未识别的英雄"""
        self.anvil_free: list[bool] = [False] * 9
        for index, champion in enumerate(self.bench):
            if champion == "?" or isinstance(champion, str):
                print("  出售英雄")
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                self.bench[index] = None
                self.anvil_free[index] = True
            elif isinstance(champion, Champion):
                if (
                        self.champs_to_buy.get(champion.name, -1) < 0
                        and champion.name in self.board_names
                ):
                    print("  出售英雄")
                    mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
                    self.bench[index] = None
                    self.anvil_free[index] = True

    def clear_anvil(self) -> None:
        """消耗掉 备战区的武器库 (铁砧)"""
        isAnvil = False
        for index, champion in enumerate(self.bench):
            if champion is None and not self.anvil_free[index]:
                mk_functions.press_e(screen_coords.BENCH_LOC[index].get_coords())
        sleep(0.5)
        anvil_msg: str = ocr.get_text(
            screenxy=screen_coords.ANVIL_MSG_POS.get_coords(),
            scale=3
        )
        if anvil_msg == "选择一件":
            items: list = self.get_anvil_items()
            arbitrarily = True
            isAnvil = True
            # 遍历预设英雄列表
            for champ_name in comps.COMP:
                # 遍历预设英雄装备
                for c_item in comps.COMP[champ_name]["items"]:
                    # 铁砧武器库装备
                    for item in items:
                        # 普通
                        if items.__len__() == 4:
                            if item in game_assets.FULL_ITEMS[c_item] and arbitrarily:
                                mk_functions.left_click(
                                    screen_coords.ORDINARY_ANVIL_LOC[items.index(item)].get_coords())
                                print(f" 选择[{item}]")
                                arbitrarily = False
                                break
                        # 高级
                        elif items.__len__() == 5:
                            if item in c_item and arbitrarily:
                                mk_functions.left_click(
                                    screen_coords.DIVINE_ANVIL_LOC[items.index(item)].get_coords())
                                print(f" 选择[{item}]")
                                arbitrarily = False
                                break
            if arbitrarily:
                # 快速处理铁砧
                print(f" 快速选择")
                mk_functions.left_click(screen_coords.BUY_LOC[2].get_coords())
            if isAnvil:
                sleep(1)

    def get_anvil_items(self) -> list:
        """返回铁砧上的物品"""
        screen_capture = ImageGrab.grab(bbox=screen_coords.ANVIL_ITEMS_POS.get_coords())
        items: list = []
        thread_list: list = []
        for index, pos in enumerate(screen_coords.ORDINARY_ANVIL_ITEM_POS):
            thread = threading.Thread(
                target=self.get_anvil_item, args=(screen_capture, pos, index, items)
            )
            thread_list.append(thread)
        for index, pos in enumerate(screen_coords.DIVINE_ANVIL_ITEM_POS):
            thread = threading.Thread(
                target=self.get_anvil_item, args=(screen_capture, pos, index, items)
            )
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            sleep(0.05)
        for thread in thread_list:
            thread.join()
        return sorted(items)

    def get_anvil_item(self, screen_capture: ImageGrab.Image, pos: Vec4, index: int, items: list):
        """遍历识别每个铁砧物品"""
        item: str = screen_capture.crop(pos.get_coords())
        item: str = ocr.get_text_from_image(image=item)
        item = arena_functions.valid_item(item)
        if item is not None:
            items.append((index, item))

    def place_items(self) -> None:
        """
            尝试遍历我的装备 并合成给英雄单位
        """
        self.items = arena_functions.get_items()
        print(f"  装备: {list(filter((None).__ne__, self.items))}")
        for index, _ in enumerate(self.items):
            if self.items[index] is not None:
                self.add_item_to_champs(index)

    def add_item_to_champs(self, item_index: int) -> None:
        """遍历棋盘中的英雄并检查英雄是否需要该装备"""
        # self.board 每个 item.completed_items 是已经完成的装备
        # self.board 每个 item.current_building[0] 正在构建的装备 item.current_building[1]还缺少的装备
        for champ_name in comps.COMP:
            for champ in self.board:
                if champ_name == champ.name:
                    if champ.does_need_items() and self.items[item_index] is not None:
                        self.add_item_to_champ(item_index, champ)

                        #  决赛未成形装备全上
                        if self.HP:
                            if (self.HP[0][1] <= settings.HEALTH and settings.RANDOM_ITEM) or (list(filter(None,
                                                                                                           self.items)).__len__() >= settings.MAX_ITEM and settings.RANDOM_MAX_ITEM):
                                self.any_item_to_champ(item_index, champ)
                            break

    def any_item_to_champ(self, item_index: int, champ: Champion) -> None:
        """决赛装备随便上了"""
        item = self.items[item_index]
        flag = False
        coords1 = None
        if champ.hero_type():
            if item in game_assets.REAR_ITEMS:
                coords1 = screen_coords.ITEM_POS[item_index][0].get_coords()
                flag = True
        else:
            if item in game_assets.FRONTLINE_ITEMS:
                coords1 = screen_coords.ITEM_POS[item_index][0].get_coords()
                flag = True

        if flag:
            mk_functions.left_click_drag(coords1, champ.coords)
            print(f"  [随机] 装备 {item} 给 {champ.name}")
            champ.completed_items.append(item)
            index = self.items.index(item)
            while index < len(self.items) - 1:
                self.items[index] = self.items[index + 1]
                index += 1
            self.items[index] = None

    def add_item_to_champ(self, item_index: int, champ: Champion) -> None:
        """获取物品的index和champ并装备该装备"""
        item = self.items[item_index]
        similar_item = game_assets.SACRED_MATCHED_GROUP.get(item)
        # 普通成装
        if item in champ.build:
            mk_functions.left_click_drag(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)
            print(f"  成装 {item} 给 {champ.name}")
            champ.completed_items.append(item)
            champ.build.remove(item)
            index = self.items.index(item)
            while index < len(self.items) - 1:
                self.items[index] = self.items[index + 1]
                index += 1
            self.items[index] = None
            return

        # 光明成装
        if similar_item in champ.build:
            mk_functions.left_click_drag(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)
            print(f"  光明成装 {item} 给 {champ.name}")
            champ.completed_items.append(similar_item)
            champ.build.remove(similar_item)
            index = self.items.index(item)
            while index < len(self.items) - 1:
                self.items[index] = self.items[index + 1]
                index += 1
            self.items[index] = None
            return

        if item in game_assets.FULL_ITEMS:
            if item in champ.build:
                mk_functions.left_click_drag(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)
                print(f"  装备 {item} 给 {champ.name}")
                champ.completed_items.append(item)
                champ.build.remove(item)
                index = self.items.index(item)
                while index < len(self.items) - 1:
                    self.items[index] = self.items[index + 1]
                    index += 1
                self.items[index] = None

        elif len(champ.current_building) == 0:
            item_to_move: None = None
            for build_item in champ.build:
                build_item_components: list = list(game_assets.FULL_ITEMS[build_item])
                if item in build_item_components:
                    item_to_move: None = item
                    build_item_components.remove(item_to_move)
                    champ.current_building.append(
                        (build_item, build_item_components[0])
                    )
                    champ.build.remove(build_item)
            if item_to_move is not None:

                mk_functions.left_click_drag(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)

                print(f"  装备 {item} 给 {champ.name}")
                # self.items[self.items.index(item)] = None
                index = self.items.index(item)
                while index < len(self.items) - 1:
                    self.items[index] = self.items[index + 1]
                    index += 1
                self.items[index] = None
        else:
            for builditem in champ.current_building:
                if item == builditem[1]:

                    mk_functions.left_click_drag(screen_coords.ITEM_POS[item_index][0].get_coords(), champ.coords)

                    champ.completed_items.append(builditem[0])
                    champ.current_building.clear()
                    # self.items[self.items.index(item)] = None
                    index = self.items.index(item)
                    while index < len(self.items) - 1:
                        self.items[index] = self.items[index + 1]
                        index += 1
                    self.items[index] = None

                    print(f"  装备 {item} 给 {champ.name}")
                    print(f"  合成 {builditem[0]}")
                    return

    def fix_unknown(self) -> None:
        """检查参数1中传递的项是否有效"""
        sleep(0.5)
        mk_functions.press_e(
            screen_coords.BOARD_LOC[self.unknown_slots[0]].get_coords()
        )
        self.board_unknown.pop(0)
        self.board_size -= 1

    def remove_champion(self, champion: Champion) -> None:
        """移除棋盘和备战区上的指定英雄"""
        for index, slot in enumerate(self.bench):
            if isinstance(slot, Champion) and slot.name == champion.name:
                mk_functions.press_e(slot.coords)
                self.bench[index] = None

        # Remove all instances of champion in champs_to_buy
        self.champs_to_buy.pop(champion.name)

        mk_functions.press_e(champion.coords)
        self.board_names.remove(champion.name)
        self.board_size -= champion.size
        self.board.remove(champion)

    def final_comp_check(self) -> None:
        """检查棋盘并替换没有进入决赛的英雄"""
        for slot in self.bench:
            if (
                    isinstance(slot, Champion)
                    and slot.final_comp
                    and slot.name not in self.board_names
            ):
                for champion in self.board:
                    if not champion.final_comp and champion.size == slot.size:
                        print(f"  更换 {champion.name} 为 {slot.name}")
                        self.remove_champion(champion)
                        self.move_known(slot)
                        break

    def tacticians_crown_check(self) -> None:
        """检测是否从选秀界面获取一个金铲铲冠冕装备"""
        mk_functions.move_mouse(screen_coords.ITEM_POS[0][0].get_coords())
        sleep(0.2)
        item: str = ocr.get_text(
            screenxy=screen_coords.ITEM_POS[0][1].get_coords(),
            scale=3
        )
        item: str = arena_functions.valid_item(item)
        try:
            if ("金铲铲冠冕" in item) or ("金锅锅冠冕" in item) or ("金锅铲冠冕" in item):
                self.board_size -= 1
            else:
                print(f"{item} 不是冠冕")
        except TypeError:
            print("  [!]装备栏没有装备")

    def spend_gold(self, speedy=False) -> None:

        """每回合都消费金币"""
        first_run = True
        min_gold = 100 if speedy else (settings.MIN_GOLD if self.spam_roll else settings.MAX_GOLD)
        show_store = False
        const = 0
        while first_run or arena_functions.get_gold() >= min_gold:
            refresh = True
            if not first_run:
                if arena_functions.get_level() != 10:
                    if arena_functions.get_level() not in settings.UPGRADE_LEVEL:
                        mk_functions.buy_xp()
                        print("  小于期望等级 -> 购买经验")

                        if settings.BUY_EXP_REFRESH_STORE:
                            mk_functions.reroll()
                            print("  小于期望等级 -> 刷新商店")
                            refresh = False
                            show_store = True

                    elif self.champs_to_buy[comps.get_key(comps.COMP, settings.TARGET_HERO_INDEX_SATISFY_GRADE)] == 0:
                        mk_functions.buy_xp()
                        print("  C位成型 -> 购买经验")
                        if settings.BUY_EXP_REFRESH_STORE:
                            mk_functions.reroll()
                            print("  C位成型 -> 刷新商店")
                            refresh = False
                            show_store = True

                if refresh and arena_functions.get_level() in settings.UPGRADE_LEVEL:
                    mk_functions.reroll()
                    print("  刷新商店")
                    show_store = True

            shop: list = arena_functions.get_shop()

            if show_store or first_run:
                print(f"  商店: {shop}")

            for champion in shop:
                if (
                        self.champs_to_buy.get(champion[1], -1) >= 0
                        and arena_functions.get_gold()
                        - game_assets.CHAMPIONS[champion[1]]["Gold"]
                        >= 0
                ):
                    self.buy_champion(champion, 1)

            first_run = False

            const += 1
            if const >= 10:
                return

    def buy_champion(self, champion, quantity) -> None:

        """从商店购买英雄"""
        none_slot: int = arena_functions.empty_slot()
        if none_slot != -1:
            mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
            print(f"    购买 {champion[1]}")
            self.bought_champion(champion[1], none_slot)
            if champion[1] in self.champs_to_buy:
                self.champs_to_buy[champion[1]] -= quantity
        else:
            # Try to buy champ 3 when bench is full
            print(f"  备战区已满 无法购买: {champion[1]}")
            mk_functions.left_click(screen_coords.BUY_LOC[champion[0]].get_coords())
            game_functions.default_pos()
            sleep(0.5)
            self.fix_bench_state()
            none_slot = arena_functions.empty_slot()
            sleep(0.5)
            if none_slot != -1:
                print(f"    购买 {champion[1]}")
                if champion[1] in self.champs_to_buy:
                    self.champs_to_buy[champion[1]] -= quantity

    def buy_xp_round(self) -> None:
        """当金币等于或超过预定值时购买经验 4"""
        if arena_functions.get_gold() >= 4:
            mk_functions.buy_xp()

    def pick_abnormal(self, gold: int, attempts=settings.MAX_REFRESH_ABNORMAL) -> None:
        """从用户定义的异常突变优先级列表中选择一个"""
        abnormalName: str = arena_functions.get_abnormal()
        for potential in comps.ABRUPT_ANOMALY:
            if potential in abnormalName and gold >= 1:
                print(f"  选择异常突变BUFF {abnormalName}")
                mk_functions.left_click(screen_coords.ABNORMAL_LOC.get_coords())
                return
        if gold >= 2 and attempts >= 0:
            mk_functions.reroll()  # 按下D键刷新BUFF
            self.pick_abnormal(gold - 1, attempts - 1)
        else:
            print(f" [!]尝试刷新次数已用完")
            mk_functions.left_click(screen_coords.ABNORMAL_LOC.get_coords())

    def pick_augment(self) -> None:
        """从用户定义的强化优先级列表中选择一个强化，或者默认为不在避免列表中的强化"""

        while True:
            sleep(1)
            augments: list = []
            for coords in screen_coords.AUGMENT_POS:
                augment: str = ocr.get_text(
                    screenxy=coords.get_coords(), scale=3
                )
                augments.append(augment)
            print(f"  强化符文: {augments}")
            if len(list(filter(None, augments))) == 3 and '' not in augments:
                break

        for potential in comps.AUGMENTS:
            for augment in augments:
                if potential in augment:
                    print(f"  选择强化符文 {augment}")
                    mk_functions.left_click(
                        screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords()
                    )
                    return

        if self.augment_roll:
            print("  刷新强化符文")
            for i in range(0, 3):
                mk_functions.left_click(screen_coords.AUGMENT_ROLL[i].get_coords())
            self.augment_roll = False
            self.pick_augment()
            return

        print(
            "  [!] 未找到预设强化符文,默认选择第一个\n  [!] 您可以设置强化符文黑名单"
        )

        for augment in augments:
            found = False
            for potential in comps.AVOID_AUGMENTS:
                if potential in augment:
                    found = True
                    break
            if not found:
                mk_functions.left_click(
                    screen_coords.AUGMENT_LOC[augments.index(augment)].get_coords()
                )
                return
        mk_functions.left_click(screen_coords.AUGMENT_LOC[0].get_coords())

    def get_label(self) -> None:
        """获取用于在窗口上显示英雄名称UI的标签"""
        labels: list = [
            (f"{slot.name}", slot.coords)
            for slot in self.bench
            if isinstance(slot, Champion)
        ]
        for slot in self.board:
            if isinstance(slot, Champion):
                labels.append((f"{slot.name}", slot.coords))

        labels.extend(
            (slot, screen_coords.BOARD_LOC[self.unknown_slots[index]].get_coords())
            for index, slot in enumerate(self.board_unknown)
        )
        self.message_queue.put(("LABEL", labels))
