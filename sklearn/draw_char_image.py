import os
import cv2
from xml.etree.ElementTree import ElementTree

match_names = ['2', '5', '3', '8', '6', '9']
voc_paths = [r'D:\share\202200517\bof\0517']
learn_parent_path = r'D:\share\202200517\sklearn'

class VocBox:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def read_box(obj):
    box = obj.find('bndbox')
    x1 = int(box.find('xmin').text)
    y1 = int(box.find('ymin').text)
    x2 = int(box.find('xmax').text)
    y2 = int(box.find('ymax').text)
    return VocBox(x1, y1, x2, y2)


class VocTree:
    def __init__(self):
        self.xml_file = ''
        self.tree = ElementTree()
        self.capture_file = ''


class DrawCharImage:
    def __init__(self):
        self._path = ''
        self._voc_tree = VocTree()
        self._no = 0

    def get_xml_path(self, file=''):
        if file == '':
            return os.path.join(self._path, 'xml')
        return os.path.join(self._path, 'xml', file)

    def get_image_path(self, file):
        if file == '':
            return os.path.join(self._path, 'img')
        return os.path.join(self._path, 'img', file)

    def run(self):
        for path in voc_paths:
            self._path = path
            self.read_xml()

    def read_xml(self):
        xml_files = os.listdir(self.get_xml_path())
        voc_tree = self._voc_tree
        for xml_file in xml_files:
            voc_tree.xml_file = xml_file
            self.draw_jpg()

    def draw_jpg(self):
        voc_tree = self._voc_tree
        xml_full = self.get_xml_path(voc_tree.xml_file)
        voc_tree.tree = ElementTree(file=xml_full)
        root = voc_tree.tree.getroot()
        voc_tree.capture_file = root.find('filename').text
        for obj in root.findall('object'):
            name = obj.find('name').text
            if name in match_names:
                parent = os.path.join(learn_parent_path, name)
                if not os.path.exists(parent):
                    os.mkdir(parent)
                box = read_box(obj)
                image = cv2.imread(self.get_image_path(voc_tree.capture_file))
                clip = image[box.y1:box.y2, box.x1:box.x2]
                self._no += 1
                write_file = os.path.join(parent, str(self._no) + '.jpg')
                print(write_file, name, xml_full)
                cv2.imwrite(write_file, clip)


if __name__ == "__main__":
    drawer = DrawCharImage()
    drawer.run()
