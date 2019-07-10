from xml.dom.minidom import parse, parseString
from PyQt5.QtCore import QObject, pyqtSignal

class Parser(QObject):
    parse_res = pyqtSignal()

    def parse_book(self, path):
        dom = parse(path)
        dom.normalize()
        node1=dom.getElementsByTagName("p")
        book_text = ''
        for i in range(len(node1)):
            for j in node1[i].childNodes:
                print(j.nodeValue)
                if not j.nodeValue:
                    continue
                else:
                    book_text += j.nodeValue
        emit parse_res(book_text)


p = Parser()
path = 'aaa.fb2'
p.parse_book(path)
