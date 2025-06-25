from Triangle import Triangle as tr
from Square import Square as sq
from Circle import Circle as cr
from Hexagon import Hexagon as hx
from Rectangle import Rectangle as re

class Genertor_Shape:
    @staticmethod
    def Generate_Square():
        length = int(input("Enter an length of Square"))
        width = int(input("Enter an width of Square"))
        return sq(length, width)
    @staticmethod
    def Generate_Rectangle():
        length = int(input("Enter an length of Rectangle"))
        width = int(input("Enter an width of Rectangle"))
        return re(length, width)
    @staticmethod
    def Generate_Circle():
        radius = int(input("Enter an radius of Circle"))
        return cr(radius)
    @staticmethod
    def Generate_Hexagon():
        side = int(input("Enter an side of Hexagon"))
        return hx(side)
    @staticmethod
    def Generate_Triangle():
        length = int(input("Enter an length of Triagle"))
        width = int(input("Enter an width of Triagle"))
        return tr(length, width)
