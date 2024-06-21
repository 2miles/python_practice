import os
import sys

def main():
    abspath = os.path.abspath(__file__)
    realpath = os.path.realpath(__file__)
    basename = os.path.basename(__file__)
    dirname = os.path.dirname(__file__)
    i_dont_know = os.path.dirname(os.path.abspath(__file__))
    append = sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    sys_path = sys.path

    print(f"os.path.abspath(__file__)                  : {abspath}")
    print(f"os.path.realpath(__file__)                 : {realpath}")

    print(f"os.path.realpath(__file__)                 : {realpath}")

    print(f"__file__                                   : {__file__}")

    print(f"os.path.basename(__file__)                 : {basename}")

    print(f"os.path.dirname(__file__)                  : {dirname}")
    print(f"os.path.dirname(os.path.abspath(__file__)) : {i_dont_know}")
    print(f"sys.path.append(os.path.dirname(os.path.abspath(__file__))) : {append}")
    print(f"sys.path: {sys_path}")
    

if __name__ == "__main__":
    main()


