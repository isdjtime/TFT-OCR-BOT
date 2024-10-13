"""
英雄阵容编辑器
"""
import locale
import os
from math import cos, sin

from PyQt5.QtGui import QPainter, QPixmap, QColor, QDrag, QPolygonF, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QWidget, QVBoxLayout, QScrollArea, \
    QHBoxLayout, QGridLayout, QSizePolicy, QStackedLayout, QLineEdit, QComboBox
import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtCore import Qt, QMimeData, pyqtSlot, QByteArray, QBuffer
from pyqt5_plugins.examplebutton import QtWidgets

import game_assets
from PyQt5.QtCore import QPointF

locale.setlocale(locale.LC_COLLATE, 'zh_CN.UTF-8')


class HeroEditor(QWidget):
    """主窗口 继承QWidget类"""

    def __init__(self, *args, **kwargs):
        """初始化"""
        super().__init__(*args, **kwargs)
        self.w = 0
        self.h = 0
        self.initUI()

    def initUI(self):
        """初始化UI界面"""
        self.w = 900
        self.h = 700
        self.setObjectName('英雄阵容编辑器')  # 设置主窗口对象的名称
        self.setWindowTitle('英雄阵容编辑器')  # 设置主窗口显示的标题
        self.resize(self.w, self.h)  # 设置主用户窗口尺寸
        self.setStyleSheet("background-color: rgb(122,115,116);")
        # TODO 左边 棋盘列表
        cell = CellShow(self)
        cell.setGeometry(10, 10, 600, 300)  # 设置 CellShow 实例的位置和大小
        # TODO 右边 符文选中
        rune = RuneShow(self)
        rune.setGeometry(610, 10, 280, 320)
        rune.setStyleSheet("background-color: rgb(144,255,144);")
        # TODO 菜市场
        main = MainShow(self)
        main.setGeometry(0, 330, 916, 380)

        # main.setStyleSheet("background-color: rgb(0,0,0);")


class CellPlace(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # 允许接受拖放事件
        self.group = QVBoxLayout()  # 创建一个垂直布局
        """设置一些基本属性"""
        self.setProperty("level",2) #英雄等级 1-3 默认2
        self.setProperty("final_comp", True)  # 最终英雄
        self.setProperty("items", ["","",""])  # 装备

        # text = QLabel()
        # text.setText("文本")
        # self.group.addWidget(text)

        self.setLayout(self.group)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText() and event.mimeData().hasImage():
            # print("拖动到棋盘了")
            event.accept()

    def dropEvent(self, event):
        print("============")
        print("站位",self.property("board_position"))
        print("等级",self.property("level"))
        print("成型英雄",self.property("final_comp"))
        print("装备",self.property("items"))
        print("============")
        if event.mimeData().hasText() and event.mimeData().hasImage():
            hero_name = event.mimeData().text()
            hero_img = QPixmap()
            hero_img.convertFromImage(event.mimeData().imageData())

            # 图片
            hero_img_label = QLabel(self)
            hero_img_label.setPixmap(hero_img)
            hero_img_label.setFixedSize(45, 45)  # 设置大小
            hero_img_label.setScaledContents(True)
            # 文本
            hero_name_label = QLabel(hero_name, self)
            self.group.deleteLater()  # 清空已有布局
            # self.deleteLater()


            self.setStyleSheet("background-color:rgb(237, 86, 106);border:1px solid rgb(234, 234, 239);")

            self.group.addWidget(hero_img_label)
            self.group.addWidget(hero_name_label)

            event.acceptProposedAction()


class CellShow(QWidget):
    """棋盘列表"""

    def __init__(self, parent=None):
        """初始化"""
        super().__init__(parent)
        self.w = 0
        self.h = 0
        self.cell_count = 0
        self.column = 0
        self.row = 0
        self.initUI()

    def initUI(self):
        """初始化UI控件"""
        self.w = 550
        self.h = 250
        self.cell_count = 28
        self.column = 7
        self.row = 4
        self.resize(self.w, self.h)  # 设置棋盘大小

        # 设置一个格子的宽度
        cell_w = int(self.w / self.column)
        cell_h = int(self.h / self.row)
        for i in range(0, self.cell_count):

            # 英雄格子
            w = CellPlace(self)

            w.resize(cell_w, cell_h)

            # 调整格子位置以符合TFT模式布局

            if (i // self.column) % 2 == 1:
                cell_x = int((i % self.column + 0.5) * cell_w)
            else:
                cell_x = int(i % self.column * cell_w)
            cell_y = int(i // self.column * cell_h)

            num = (i + 21) if i <= 6 else ((i + 7) if i <= 13 else ((i - 7) if i <= 20 else (i - 21)))
            spacing = 15 - (num // 7) * 5
            w.move(cell_x, cell_y + spacing)

            w.setProperty("board_position",num) #设置位置属性
            # w.setText(str(num))  # 展示位置编号
            w.setStyleSheet("background-color:rgb(237, 86, 106);border:1px solid rgb(234, 234, 239);")
            w.show()


class RuneShow(QLabel):
    """强化符文选中列表"""

    def __init__(self, parent=None):
        """初始化"""
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        pass


class MoveHero(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


    def mousePressEvent(self, event):
        # if event.button() == Qt.LeftButton:
        #     self.startDrag()
        if event.button() == Qt.LeftButton:
            self.dragStartPosition = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            dragDistance = (event.pos() - self.dragStartPosition).manhattanLength()
            if dragDistance > 50:  # 设置拖动阈值为 50 像素
                self.startDrag()
                self.dragStartPosition = event.pos()
    def startDrag(self):
        print("拖动")
        image_label = self.findChild(QLabel, "hero_img")  # 获取图片控件
        image_name_label = self.findChild(QLabel, "hero_name")  # 获取文本控件

        drag = QDrag(self)
        mime_data = QMimeData()  # 创建QMimeData对象

        mime_data.setText(image_name_label.text())
        mime_data.setImageData(image_label.pixmap().toImage())

        drag.setMimeData(mime_data)  # 设置拖放数据
        drag.setPixmap(self.grab())  # 设置拖动时显示的图标
        drag.setHotSpot(self.rect().center())  # 设置拖动时鼠标点击位置为热点
        drag.exec_(Qt.MoveAction)  # 开始拖动操作


class Hero(QWidget):
    """英雄信息类"""

    def __init__(self, *args, **kwargs):
        """初始化"""
        super().__init__(*args, **kwargs)
        self.added_ids = set()
        self.added_jobs = set()
        self.hero_id = None
        self.hero_job = None
        self.gold_sort = False
        self.image_folder = "images/英雄"
        self.w = 0
        self.h = 0
        self.initUI()

    def initUI(self):
        self.w = 880
        self.h = 300
        self.resize(self.w, self.h)
        """垂直布局 用于划分上下两个功能板块  功能列表  英雄渲染"""
        main_layout = QVBoxLayout()

        hero_vlayout = QHBoxLayout()  # 水平布局 整合功能列表

        # TODO 查询
        self.hero_search = QLineEdit()
        self.hero_search.textChanged.connect(self.hero_search_result)
        self.hero_search.setPlaceholderText("搜索英雄")
        hero_vlayout.addWidget(self.hero_search)

        # TODO 根据 字段 排序
        sort1 = QPushButton()
        sort1.setText("A-Z")
        sort1.clicked.connect(self.sort_a_to_z)
        sort2 = QPushButton()
        sort2.setText("费用")
        sort2.clicked.connect(self.by_gold_sort)

        hero_vlayout.addWidget(sort1)
        hero_vlayout.addWidget(sort2)

        # TODO 特质
        self.hero_id = QComboBox()
        self.hero_id.addItem("特质")
        self.hero_id.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.hero_id.model().item(0).setEnabled(False)

        hero_vlayout.addWidget(self.hero_id)
        # TODO 职业
        self.hero_job = QComboBox()
        self.hero_job.addItem("职业")
        self.hero_job.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.hero_job.model().item(0).setEnabled(False)
        self.hero_id.currentIndexChanged.connect(self.update_hero_search_result)  # 连接槽
        self.hero_job.currentIndexChanged.connect(self.update_hero_search_result)
        hero_vlayout.addWidget(self.hero_job)
        # TODO 清空查询字段
        empty = QPushButton()
        empty.setText("清空")
        empty.clicked.connect(self.empty_checked_item)

        hero_vlayout.addStretch()  # 弹簧
        hero_vlayout.addWidget(empty)
        main_layout.addLayout(hero_vlayout)

        # TODO 渲染可选英雄列表

        hero_list_hlayout = QHBoxLayout()  # 水平布局

        # 创建一个滚动布局 用于渲染超出范围的内容
        hero_list = QScrollArea()

        # 创建一个 QWidget 作为滚动布局的内容小部件
        hero_list_widget = QWidget()

        # 创建一个 网格布局 用于存放每个英雄的item
        self.grid_layout = QGridLayout(hero_list_widget)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # 设置对其方式

        # 遍历文件夹中的图片
        image_files = os.listdir(self.image_folder)
        row = 0
        column = 0
        for image_file in image_files:
            # 利用QWidget把两个QLabel合成一个整体
            hero_item = MoveHero()

            hero_group = QVBoxLayout()  # 创建一个垂直布局用于设置排版
            # 创建一个 QLabel 来显示英雄图片
            image_label = QLabel()
            image_label.setFixedSize(45, 45)  # 设置大小
            image_label.setScaledContents(True)
            image_label.setPixmap(QPixmap(os.path.join(self.image_folder, image_file)))

            self.image_name = image_file.rsplit(".", 1)[0]  # 取文件名
            """通过读取配置信息设置对应的英雄费用颜色边框"""
            gold = game_assets.CHAMPIONS[self.image_name]["Gold"]
            if gold == 1:
                image_label.setStyleSheet("border: 2px solid #999;")
            elif gold == 2:
                image_label.setStyleSheet("border: 2px solid #5fcc29;")
            elif gold == 3:
                image_label.setStyleSheet("border: 2px solid #297acc;")
            elif gold == 4:
                image_label.setStyleSheet("border: 2px solid #cc29cc;")
            elif gold == 5:
                image_label.setStyleSheet("border: 2px solid #cca329;")
            # 使用 setProperty 给每个英雄添加一个 gold 属性
            hero_item.setProperty("gold", gold)
            # 添加特质
            hero_id_trait1 = game_assets.CHAMPIONS[self.image_name]["Trait1"]
            hero_item.setProperty("hero_id", hero_id_trait1)
            self.add_id(hero_id_trait1)

            # 添加职业
            hero_job_trait1 = game_assets.CHAMPIONS[self.image_name]["Trait2"]
            hero_job_trait2 = game_assets.CHAMPIONS[self.image_name]["Trait3"]
            hero_job_trait3 = game_assets.CHAMPIONS[self.image_name]["Trait4"]
            hero_item.setProperty("hero_job1", hero_job_trait1)
            hero_item.setProperty("hero_job2", hero_job_trait2)
            hero_item.setProperty("hero_job3", hero_job_trait3)

            if "" != hero_job_trait1:
                self.add_job(hero_job_trait1)
            if "" != hero_job_trait2:
                self.add_job(hero_job_trait2)
            if "" != hero_job_trait3:
                self.add_job(hero_job_trait3)

            hero_group.addWidget(image_label)  # 添加到垂直布局中

            # 创建一个 QLabel 来显示英雄名
            image_name_label = QLabel()
            image_name_label.setWordWrap(True)
            image_name_label.setText(self.image_name)
            image_name_label.setAlignment(Qt.AlignCenter)
            image_name_label.setStyleSheet("font-size: 12px")
            image_label.setObjectName("hero_img")  ####
            image_name_label.setObjectName("hero_name")  ####
            hero_group.addWidget(image_name_label)  # 添加到垂直布局中

            hero_item.setLayout(hero_group)  # 把排版好的添加成一个item
            # hero_item.setObjectName("hero_name")  # 设置对象名称 排序用
            hero_item.setStyleSheet("background-color:rgba(255, 255, 255,0);")
            # TODO 拖动事件

            self.grid_layout.addWidget(hero_item, row, column)  # 添加到网格布局中
            # 每行显示12个超过换行
            column += 1
            if column >= 12:
                row += 1
                column = 0

        # 将 QWidget 设置为 QScrollArea 的内容小部件
        hero_list.setWidget(hero_list_widget)

        # 整合到一起
        hero_list_hlayout.addWidget(hero_list)
        main_layout.addLayout(hero_list_hlayout)

        # 将上下两个添加好的功能区块显示
        self.setLayout(main_layout)

    # 模糊搜索
    def hero_search_result(self, hero_name):
        # 清空原有的 hero_item
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # 如果搜索框中有内容
        if hero_name:
            row = 0
            column = 0
            # 遍历英雄列表，查找匹配的英雄
            for image_file in os.listdir(self.image_folder):
                image_name = image_file.rsplit(".", 1)[0]
                if hero_name.lower() in image_name.lower():  # 不区分大小写进行模糊匹配
                    # 创建一个 QWidget 把两个QLabel 合成一个整体
                    hero_item = QWidget()
                    hero_group = QVBoxLayout()

                    # 创建一个 QLabel 来显示英雄图片
                    image_label = QLabel()
                    image_label.setFixedSize(45, 45)
                    image_label.setScaledContents(True)
                    image_label.setPixmap(QPixmap(os.path.join(self.image_folder, image_file)))

                    image_name = image_file.rsplit(".", 1)[0]
                    gold = game_assets.CHAMPIONS[image_name]["Gold"]
                    if gold == 1:
                        image_label.setStyleSheet("border: 2px solid #999;")
                    elif gold == 2:
                        image_label.setStyleSheet("border: 2px solid #5fcc29;")
                    elif gold == 3:
                        image_label.setStyleSheet("border: 2px solid #297acc;")
                    elif gold == 4:
                        image_label.setStyleSheet("border: 2px solid #cc29cc;")
                    elif gold == 5:
                        image_label.setStyleSheet("border: 2px solid #cca329;")
                    # 使用 setProperty 方法添加 gold 属性
                    hero_item.setProperty("gold", gold)
                    hero_group.addWidget(image_label)

                    # 创建一个 QLabel 来显示英雄名
                    image_name_label = QLabel()
                    image_name_label.setWordWrap(True)
                    image_name_label.setText(image_name)
                    image_name_label.setAlignment(Qt.AlignCenter)
                    image_name_label.setStyleSheet("font-size: 12px")

                    hero_group.addWidget(image_name_label)

                    hero_item.setLayout(hero_group)
                    hero_item.setObjectName(image_name)  # 设置对象名称 排序用

                    self.grid_layout.addWidget(hero_item, row, column)
                    column += 1
                    if column >= 12:
                        row += 1
                        column = 0
        else:  # 如果搜索框为空
            # 重新加载所有英雄项
            row = 0
            column = 0
            for image_file in os.listdir(self.image_folder):
                image_name = image_file.rsplit(".", 1)[0]

                # 创建英雄项
                hero_item = QWidget()
                hero_group = QVBoxLayout()

                # 创建英雄图片和名称
                image_label = QLabel()
                image_label.setFixedSize(45, 45)
                image_label.setScaledContents(True)
                image_label.setPixmap(QPixmap(os.path.join(self.image_folder, image_file)))

                image_name_label = QLabel()
                image_name_label.setWordWrap(True)
                image_name_label.setText(image_name)
                image_name_label.setAlignment(Qt.AlignCenter)
                image_name_label.setStyleSheet("font-size: 12px")

                # 英雄颜色
                gold = game_assets.CHAMPIONS[image_name]["Gold"]
                if gold == 1:
                    image_label.setStyleSheet("border: 2px solid #999;")
                elif gold == 2:
                    image_label.setStyleSheet("border: 2px solid #5fcc29;")
                elif gold == 3:
                    image_label.setStyleSheet("border: 2px solid #297acc;")
                elif gold == 4:
                    image_label.setStyleSheet("border: 2px solid #cc29cc;")
                elif gold == 5:
                    image_label.setStyleSheet("border: 2px solid #cca329;")
                # 使用 setProperty 方法添加 gold 属性
                hero_item.setProperty("gold", gold)
                hero_group.addWidget(image_label)
                hero_group.addWidget(image_name_label)

                hero_item.setLayout(hero_group)
                hero_item.setObjectName(image_name)

                # 将英雄项添加到布局中
                self.grid_layout.addWidget(hero_item, row, column)
                column += 1
                if column >= 12:
                    row += 1
                    column = 0

        # 刷新布局
        self.grid_layout.update()

    def empty_checked_item(self):
        print("清空")

        self.hero_search.clear()
        self.hero_id.setCurrentIndex(0)
        self.hero_job.setCurrentIndex(0)
        # 史
        row = 0
        column = 0
        for image_file in os.listdir(self.image_folder):
            image_name = image_file.rsplit(".", 1)[0]

            # 创建英雄项
            hero_item = QWidget()
            hero_group = QVBoxLayout()

            # 创建英雄图片和名称
            image_label = QLabel()
            image_label.setFixedSize(45, 45)
            image_label.setScaledContents(True)
            image_label.setPixmap(QPixmap(os.path.join(self.image_folder, image_file)))

            image_name_label = QLabel()
            image_name_label.setWordWrap(True)
            image_name_label.setText(image_name)
            image_name_label.setAlignment(Qt.AlignCenter)
            image_name_label.setStyleSheet("font-size: 12px")

            # 英雄颜色
            gold = game_assets.CHAMPIONS[image_name]["Gold"]
            if gold == 1:
                image_label.setStyleSheet("border: 2px solid #999;")
            elif gold == 2:
                image_label.setStyleSheet("border: 2px solid #5fcc29;")
            elif gold == 3:
                image_label.setStyleSheet("border: 2px solid #297acc;")
            elif gold == 4:
                image_label.setStyleSheet("border: 2px solid #cc29cc;")
            elif gold == 5:
                image_label.setStyleSheet("border: 2px solid #cca329;")
            # 使用 setProperty 方法添加 gold 属性
            hero_item.setProperty("gold", gold)
            hero_group.addWidget(image_label)
            hero_group.addWidget(image_name_label)

            hero_item.setLayout(hero_group)
            hero_item.setObjectName(image_name)

            # 将英雄项添加到布局中
            self.grid_layout.addWidget(hero_item, row, column)
            column += 1
            if column >= 12:
                row += 1
                column = 0
        # 刷新布局
        self.grid_layout.update()

    def sort_a_to_z(self):

        # 获取英雄列表的子部件数量
        hero_count = self.grid_layout.count()

        # 创建一个列表来存储英雄列表的子部件
        hero_items = []

        # 获取英雄列表的所有子部件
        for i in range(hero_count):
            hero_item = self.grid_layout.itemAt(i).widget()
            hero_items.append(hero_item)

        # 对英雄列表进行排序，使用自定义的中文排序函数
        sorted_heroes = sorted(hero_items, key=lambda x: locale.strxfrm(x.objectName()))

        # 清空布局
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        # 重新设置英雄列表的布局顺序
        for i, hero_item in enumerate(sorted_heroes):
            self.grid_layout.addWidget(hero_item, i // 12, i % 12)

    # 排序
    def by_gold_sort(self):
        self.gold_sort = not self.gold_sort
        if self.gold_sort:
            self.sort_by_gold_asc()
        else:
            self.sort_by_gold_desc()

    def sort_by_gold_asc(self):

        # 获取英雄列表的子部件数量
        hero_count = self.grid_layout.count()

        # 创建一个列表来存储英雄列表的子部件
        hero_items = []

        # 获取英雄列表的所有子部件
        for i in range(hero_count):
            hero_item = self.grid_layout.itemAt(i).widget()
            hero_items.append(hero_item)

        # 对英雄列表按照 gold 属性从小到大排序
        sorted_heroes = sorted(hero_items, key=lambda x: x.property("gold"))

        # 清空布局
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        # 重新设置英雄列表的布局顺序
        for i, hero_item in enumerate(sorted_heroes):
            self.grid_layout.addWidget(hero_item, i // 12, i % 12)

    def sort_by_gold_desc(self):

        # 获取英雄列表的子部件数量
        hero_count = self.grid_layout.count()

        # 创建一个列表来存储英雄列表的子部件
        hero_items = []

        # 获取英雄列表的所有子部件
        for i in range(hero_count):
            hero_item = self.grid_layout.itemAt(i).widget()
            hero_items.append(hero_item)

        # 对英雄列表按照 gold 属性从大到小排序
        sorted_heroes = sorted(hero_items, key=lambda x: x.property("gold"), reverse=True)

        # 清空布局
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        # 重新设置英雄列表的布局顺序
        for i, hero_item in enumerate(sorted_heroes):
            self.grid_layout.addWidget(hero_item, i // 12, i % 12)

    def add_job(self, job):
        isTrue = False
        for key, value in game_assets.CHAMPIONS.items():
            hero_id = value["Trait1"]
            if job not in hero_id:
                isTrue = True
            else:
                isTrue = False
                return

        if isTrue:
            if job not in self.added_jobs:
                self.hero_job.addItem(job)
                self.added_jobs.add(job)

    def add_id(self, hero_id):
        if hero_id not in self.added_ids:
            self.hero_id.addItem(hero_id)
            self.added_ids.add(hero_id)

    def update_hero_search_result(self):
        isTrue = False
        # 获取当前选中的内容
        selected_hero_id = self.hero_id.currentText()
        selected_hero_job = self.hero_job.currentText()

        # 清空原有的 hero_item
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if selected_hero_id != "特质":
            print(selected_hero_id)
            isTrue = True

        if selected_hero_job != "职业":
            print(selected_hero_job)
            isTrue = True

        if isTrue:
            image_files = os.listdir(self.image_folder)

            row = 0
            column = 0
            for image_file in image_files:
                # 创建一个 QWidget 把两个QLabel 合成一个整体
                hero_item = QWidget()
                hero_group = QVBoxLayout()

                # 创建一个 QLabel 来显示英雄图片
                image_label = QLabel()
                image_label.setFixedSize(45, 45)
                image_label.setScaledContents(True)
                image_label.setPixmap(QPixmap(os.path.join(self.image_folder, image_file)))

                self.image_name = image_file.rsplit(".", 1)[0]
                gold = game_assets.CHAMPIONS[self.image_name]["Gold"]
                if gold == 1:
                    image_label.setStyleSheet("border: 2px solid #999;")
                elif gold == 2:
                    image_label.setStyleSheet("border: 2px solid #5fcc29;")
                elif gold == 3:
                    image_label.setStyleSheet("border: 2px solid #297acc;")
                elif gold == 4:
                    image_label.setStyleSheet("border: 2px solid #cc29cc;")
                elif gold == 5:
                    image_label.setStyleSheet("border: 2px solid #cca329;")
                # 使用 setProperty 方法添加 gold 属性
                hero_item.setProperty("gold", gold)
                # 添加特质
                hero_id_trait1 = game_assets.CHAMPIONS[self.image_name]["Trait1"]
                hero_item.setProperty("hero_id", hero_id_trait1)
                self.add_id(hero_id_trait1)

                # 添加职业
                hero_job_trait1 = game_assets.CHAMPIONS[self.image_name]["Trait2"]
                hero_job_trait2 = game_assets.CHAMPIONS[self.image_name]["Trait3"]
                hero_job_trait3 = game_assets.CHAMPIONS[self.image_name]["Trait4"]
                hero_item.setProperty("hero_job1", hero_job_trait1)
                hero_item.setProperty("hero_job2", hero_job_trait2)
                hero_item.setProperty("hero_job3", hero_job_trait3)

                if "" != hero_job_trait1:
                    self.add_job(hero_job_trait1)
                if "" != hero_job_trait2:
                    self.add_job(hero_job_trait2)
                if "" != hero_job_trait3:
                    self.add_job(hero_job_trait3)

                hero_group.addWidget(image_label)

                # 创建一个 QLabel 来显示英雄名
                image_name_label = QLabel()
                image_name_label.setWordWrap(True)
                image_name_label.setText(self.image_name)
                image_name_label.setAlignment(Qt.AlignCenter)
                image_name_label.setStyleSheet("font-size: 12px")

                hero_group.addWidget(image_name_label)

                hero_item.setLayout(hero_group)

                hero_item.setObjectName(self.image_name)  # 设置对象名称 排序用

                if selected_hero_id == hero_id_trait1 and (
                        selected_hero_job == hero_job_trait1 or selected_hero_job == hero_job_trait2 or selected_hero_job == hero_job_trait3):
                    self.grid_layout.addWidget(hero_item, row, column)
                    column += 1
                    if column >= 12:
                        row += 1
                        column = 0
                else:

                    if selected_hero_id == hero_id_trait1 and selected_hero_job == "职业":

                        self.grid_layout.addWidget(hero_item, row, column)
                        column += 1
                        if column >= 12:
                            row += 1
                            column = 0
                    if (
                            selected_hero_job == hero_job_trait1 or selected_hero_job == hero_job_trait2 or selected_hero_job == hero_job_trait3) and selected_hero_id == "特质":
                        print("职业条件成立", selected_hero_job)
                        self.grid_layout.addWidget(hero_item, row, column)
                        column += 1
                        if column >= 12:
                            row += 1
                            column = 0


class Weapon(QLabel):
    """装备"""
    pass


class Rune(QLabel):
    """强化符文"""
    pass


class MainShow(QWidget):
    def __init__(self, parent=None):
        """初始化"""
        super().__init__(parent)
        self.w = 0
        self.h = 0
        self.stackedLayout = None
        self.initUI()

    def initUI(self):
        self.w = 880
        self.h = 360
        self.stackedLayout = QStackedLayout()  # 堆叠布局

        # self.setGeometry(10, 393, 880, 300)

        # 切换页面按钮
        button1 = QPushButton("英雄")
        button2 = QPushButton("装备")
        button3 = QPushButton("符文")

        # TODO 英雄列表
        hero = Hero(self)

        # =========================

        # TODO 装备列表
        label2 = QLabel("装备")
        label2.setStyleSheet("background-color:green;")
        # TODO 符文列表
        label3 = QLabel("符文")
        label3.setStyleSheet("background-color:yellow;")

        # self.stackedLayout.addWidget(label1)
        self.stackedLayout.insertWidget(0, hero)  # 设置索引 添加到堆叠布局中
        # self.stackedLayout.addWidget(label2)
        self.stackedLayout.insertWidget(1, label2)
        # self.stackedLayout.addWidget(label3)
        self.stackedLayout.insertWidget(2, label3)

        button1.clicked.connect(self.hero_page)  # 按钮绑定切换事件
        button2.clicked.connect(self.weapon_page)
        button3.clicked.connect(self.rune_page)

        vlayout = QVBoxLayout(self)  # 水平布局
        hlayout = QHBoxLayout(self)  # 垂直布局
        hlayout.addWidget(button1, Qt.AlignCenter)  # 添加按钮到水平布局中
        hlayout.addWidget(button2, Qt.AlignCenter)
        hlayout.addWidget(button3, Qt.AlignCenter)

        vlayout.addLayout(hlayout)  # 添加 垂直布局容器 到 水平布局容器中
        vlayout.addLayout(self.stackedLayout)

        self.setLayout(vlayout)

    # 通过索引来设置切换界面
    def hero_page(self):
        self.stackedLayout.setCurrentIndex(0)

    def weapon_page(self):
        self.stackedLayout.setCurrentIndex(1)

    def rune_page(self):
        self.stackedLayout.setCurrentIndex(2)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = HeroEditor()
    # window = CellShow()
    window.show()
    sys.exit(app.exec_())
