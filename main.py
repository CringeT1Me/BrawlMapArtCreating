from PIL import Image, ImageEnhance, ImageDraw
from GetColor import GetColor
import io
import sys
from PySide6 import QtWidgets, QtGui

from gui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, mapmaker):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.mapmaker = mapmaker
        self.dialog_save = QtWidgets.QFileDialog(self)
        self.dialog_open = QtWidgets.QFileDialog(self)
        self.dialog_open.selectNameFilter('Images (*.png *.jpg)')
        self.dialog_open.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        self.ui.btn_new_image.clicked.connect(self.create_new_image)
        self.ui.btn_save_image.clicked.connect(self.save_image)
        self.ui.checkBox_grid.clicked.connect(self.set_image)
        self.ui.checkBox_map_cells.clicked.connect(self.set_image)

    def get_image(self):
        if self.ui.checkBox_grid.isChecked() and self.ui.checkBox_map_cells.isChecked():
            img = self.mapmaker.get_result_image_with_grid_and_cells()
        elif self.ui.checkBox_grid.isChecked():
            img = self.mapmaker.get_result_image_with_grid()
        elif self.ui.checkBox_map_cells.isChecked():
            img = self.mapmaker.get_result_image_with_cells()
        else:
            img = self.mapmaker.get_result_image()
        return img

    def create_new_image(self):
        fname = self.dialog_open.getOpenFileName(self, 'Open file', '/', 'Images (*.png *.jpg)')
        self.mapmaker.set_source_image(fname[0])
        self.set_image()

    def set_image(self, ):
        img = self.get_image()
        bytes_img = io.BytesIO()
        img.save(bytes_img, format='PNG')
        q_img = QtGui.QImage()
        q_img.loadFromData(bytes_img.getvalue())
        self.ui.ImageBoard.setPixmap(QtGui.QPixmap.fromImage(q_img))

    def save_image(self):
        fpath = self.dialog_save.getSaveFileName(self, 'Save file', '/', 'PNG (*.png);; JPG (*.jpg)')
        img = self.get_image()
        if fpath[1].find('JPG', 0, 3) != -1:
            img = img.convert('RGB')
        img.save(fpath[0])


class MakeAMap:
    def __init__(self, get_color):
        self.getColor = get_color
        self.assets_size = 40
        self.source_image = None
        self.result_image = Image.open('assets\\map.png').convert('RGBA')
        self.result_image_map_cells = Image.open('assets\\map.png').convert('RGBA')
        self.result_image_grid = None
        self.result_image_grid_map_cells = None
        self.draw_grid()

    def make_map(self):
        self.result_image = Image.open('assets\\map.png').convert('RGBA')
        self.result_image_map_cells = Image.open('assets\\map.png').convert('RGBA')
        map_of_assets = [[0] * 60 for _ in range(60)]
        map_of_assets_with_cells = [[0] * 60 for _ in range(60)]
        pixels = self.source_image.load()
        images = [[0] * 60 for _ in range(60)]
        for x in range(60):
            for y in range(60):
                rgb = pixels[x, y]
                map_of_assets[x][y] = self.getColor.get_color(rgb)
                map_of_assets_with_cells[x][y] = self.getColor.get_color_map_cells(rgb)
                if not (map_of_assets_with_cells[x][y] == 'brown_map_cell_dark' and (x - y) % 2 == 0) and not (
                        map_of_assets_with_cells[x][y] == 'brown_map_cell_light' and (x - y) % 2 != 0):
                    images[x][y] = Image.open('assets\\showdown\\' + str(map_of_assets[x][y]) + '.png').resize(
                        (40, 40)).convert('RGBA')
                    self.result_image_map_cells.paste(images[x][y], (x * 40, y * 40), mask=images[x][y])
                images[x][y] = Image.open('assets\\showdown\\' + str(map_of_assets[x][y]) + '.png').resize(
                    (40, 40)).convert('RGBA')
                self.result_image.paste(images[x][y], (x * 40, y * 40), mask=images[x][y])
        self.draw_grid()

    def get_result_image_with_grid(self):
        return self.result_image_grid

    def get_result_image_with_grid_and_cells(self):
        return self.result_image_grid_map_cells

    def get_result_image_with_cells(self):
        return self.result_image_map_cells

    def get_result_image(self):
        return self.result_image

    def draw_grid(self):
        self.result_image_grid = self.result_image.copy()
        self.result_image_grid_map_cells = self.result_image_map_cells.copy()
        drawer = ImageDraw.Draw(self.result_image_grid)
        drawer_with_cells = ImageDraw.Draw(self.result_image_grid_map_cells)
        for xy in range(40, 2400, 40):
            drawer.line((xy, 0, xy, 2400), (255, 255, 255), 2)
            drawer.line((0, xy, 2400, xy), (255, 255, 255), 2)
            drawer_with_cells.line((xy, 0, xy, 2400), (255, 255, 255), 2)
            drawer_with_cells.line((0, xy, 2400, xy), (255, 255, 255), 2)

    def set_source_image(self, path):
        self.source_image = Image.open(path).convert('RGBA')
        enchancer = ImageEnhance.Contrast(self.source_image)
        self.source_image = enchancer.enhance(2.5)
        self.source_image = self.source_image.resize((60, 60))
        self.make_map()


app = QtWidgets.QApplication(sys.argv)
getColor = GetColor()
mapmaker = MakeAMap(getColor)
window = MainWindow(mapmaker)
window.show()
app.exec()
