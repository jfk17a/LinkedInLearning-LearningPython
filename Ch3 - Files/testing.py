import os
from os import path
import shutil

def main():
    src = path.realpath("deps")
    print(src)
    # for dir, root, file in os.walk(src):
    #     for fl in file:
    #         name = dir + "\\" + fl
    #         print(path.getsize(name))

if __name__ == "__main__":
    main()