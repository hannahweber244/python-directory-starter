import argparse as arg
from .directory_starter import main

if __name__ == "__main__":
    parser = arg.ArgumentParser(description="Process package specific inputs")

    parser.add_argument("--structure-mode", "-mode", default="minimal", type=str)
    parser.add_argument("--mirror-from", "-mirror", default=None, type=str)
    args = parser.parse_args()

    main(args)
