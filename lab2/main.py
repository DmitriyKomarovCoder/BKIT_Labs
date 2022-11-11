from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import os

def main():
    r = Rectangle("синего", 6, 6)
    c = Circle("зеленого", 6)
    s = Square("красного", 6)

    os.system('cowsay ' + str(r))
    os.system('cowsay ' + str(c))
    os.system('cowsay ' + str(s))
if name == "main":
    main()