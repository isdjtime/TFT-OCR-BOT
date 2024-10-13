"""
Game类用于检索相关数据的函数
"""

from time import sleep
from PIL import ImageGrab
import screen_coords
import ocr
import game_assets
import mk_functions


def get_round() -> list[str, int]:
    """Gets the current game round"""
    screen_capture = ImageGrab.grab(bbox=screen_coords.ROUND_POS.get_coords())
    round_three = screen_capture.crop(screen_coords.ROUND_POS_THREE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_three)
    if game_round in game_assets.ROUNDS:
        return [game_round, 3]

    round_two = screen_capture.crop(screen_coords.ROUND_POS_TWO.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_two)
    if game_round in game_assets.ROUNDS:
        return [game_round, 2]

    round_one = screen_capture.crop(screen_coords.ROUND_POS_ONE.get_coords())
    game_round: str = ocr.get_text_from_image(image=round_one)
    if game_round in game_assets.ROUNDS:
        return [game_round, 1]
    return ["999-999", 0]


def check_encounter_round() -> list[str]:
    """通过检查回合文本获取游戏回合列表"""
    round_list: list = []
    for positions in screen_coords.ROUND_ENCOUNTER_ICON_POS:
        mk_functions.move_mouse(positions[0].get_coords())
        round_message: str = ocr.get_text(
            screenxy=positions[1].get_coords(),
            scale=3
        )
        if any(keyword in round_message for keyword in ["选秀"]):
            round_list.append("carousel")
        elif any(keyword in round_message for keyword in ["奇遇出现了！"]):
            round_list.append("encounter")
        elif any(
                keyword in round_message for keyword in ["对抗：石甲虫", "对抗：暗影狼", "对抗：锋喙鸟", "对抗：远古巨龙"]):
            round_list.append("pve")
        else:
            round_list.append("pvp")
    mk_functions.move_mouse(screen_coords.DEFAULT_LOC.get_coords())
    return round_list


def pickup_items() -> None:  # Refacor this function to make it more clear whats happening
    """在PVP回合后从棋盘上捡起物品"""
    for index, coords in enumerate(screen_coords.ITEM_PICKUP_LOC):
        mk_functions.right_click(coords.get_coords())
        if index == 7:  # Don't need to sleep on final click
            return
        if index == 0:
            sleep(1.2)
        if index % 2 == 0:
            sleep(2)
        else:
            sleep(1.2)


def get_champ_carousel(tft_round: str) -> None:
    """从选秀界面拿取英雄"""
    while tft_round == get_round()[0]:
        mk_functions.right_click(screen_coords.CAROUSEL_LOC.get_coords())
        sleep(0.7)
    sleep(3)


def check_alive() -> bool:  # Refactor this function to use API
    """Checks the screen to see if player is still alive"""
    if ocr.get_text(screenxy=screen_coords.EXIT_NOW_POS.get_coords(), scale=3) == '现在退出':
        return False
    return (
            ocr.get_text(
                screenxy=screen_coords.VICTORY_POS.get_coords(),
                scale=3
            )
            != '继续观看'
    )


def exit_game() -> None:
    """Exits the game"""
    mk_functions.left_click(screen_coords.EXIT_NOW_LOC.get_coords())


def default_pos() -> None:
    """将鼠标移动到默认位置，以确保没有数据被OCR阻止"""
    mk_functions.left_click(screen_coords.DEFAULT_LOC.get_coords())


def forfeit() -> None:
    """输掉比赛"""
    mk_functions.press_esc()
    mk_functions.left_click(screen_coords.SURRENDER_LOC.get_coords())
    sleep(0.1)
    mk_functions.left_click(screen_coords.SURRENDER_TWO_LOC.get_coords())
    sleep(1)
