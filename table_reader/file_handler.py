from reader.image_process_tools import *
from reader.cells_extractor import CellExtractor
from reader.reader import Reader
import numpy as np
import pdf2image
import base64
import cv2


class FileHandler:
    def __init__(self, **kwargs):
        self._cell_extractor = CellExtractor()
        self._reader = Reader(**kwargs)

    def _list_with_numpy_to_native(self,
                                   list_with_numpy: np.array):
        new_col_list = []
        for col in list_with_numpy:
            new_col_list.append([])
            for bbox in col:
                x, y, w, h = bbox
                new_col_list[-1].append((x.item(), y.item(), w.item(), h.item()))
        return new_col_list

    def _draw_cells(self,
                    img: np.array,
                    columns_list: list):

        for col in columns_list:
            for x, y, w, h in col:
                img = cv2.rectangle(img,
                                    (x, y), (x+w, y+h),
                                    (255, 0, 0), 2)
        return img

    def _extract_cells(self,
                       file: np.array):
        """
        :param file: image like np.array
        :return: list like [col1, col2, ...] where col_i is list with coordinates of cells and image like base64 string
        """
        file = align_image(file)
        columns_list = self._cell_extractor.extract_cells(file)
        columns_list = self._list_with_numpy_to_native(columns_list)
        image_with_drawed_cells = image_encoder(self._draw_cells(file, columns_list))
        return columns_list, image_with_drawed_cells

    def extract_cells_from_img(self,
                               file: str):
        """
        :param file: image in base64 string
        :return: tuple with list of coordinates cells and list of image like base64 string
        """
        file = image_decoder(file)
        cells, drawed_page = self._extract_cells(file)
        return [cells], [drawed_page]

    def extract_cells_from_pdf(self,
                               file: str):
        """
        :param file: pdf in base64 string
        :return: list with lists coordinates of cells and list with images in base64 strings
        """
        file = base64.b64decode(file)
        file = pdf2image.convert_from_bytes(file)

        cells_list = []
        pages = []
        for page in file:
            cells, drawed_page = self._extract_cells(np.array(page))
            cells_list.append(cells)
            pages.append(drawed_page)
        return cells_list, pages

    def read_from_img(self,
                      file: str):
        """
        :param file: image in base64 string
        :return: dict like {col_name1: [value1, value2, ...], ...}
        """
        return self._reader.read(file)

    def read_from_pdf(self,
                      file: str):
        """
        :param file: pdf in base64 string
        :return: list of dicts like [{col_name: [value1, ...], ...}, ...]
        """
        file = base64.b64decode(file)
        file = pdf2image.convert_from_bytes(file)

        res = []
        for page in file:
            res.append(self._reader.read(np.array(page)))
        return res
