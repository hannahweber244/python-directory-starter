import os

from .structure import StructureBuilder


def main(args):
    """main function to initialize directory structure"""
    mode = args.structure_mode
    mirror_directory = args.mirror_from

    if mirror_directory is not None:
        mode = None

    builder = StructureBuilder()

    if mode == "minimal":
        builder.directory_list = ["src", "data", "reports", "notebooks"]
        builder.file_list = [
            "README.md",
            ".gitignore",
            "requirements.txt",
            "LICENSE",
            "src/__init__.py",
            ".env"
        ]

    elif mode == "medium":
        builder.directory_list = [
            "src",
            "data",
            "tests",
            "reports",
            "docs",
            "references",
            "notebooks",
        ]
        builder.file_list = [
            "README.md",
            ".gitignore",
            "main.py",
            "requirements.txt",
            "LICENSE",
            "src/__init__.py",
            ".env",
        ]

    elif mode == "packaging":
        builder.directory_list = ["src/PACKAGE-DIR", "docs", "tests"]
        builder.file_list = [
            "LICENSE",
            "setup.py",
            "setup.cfg",
            "README.md",
            "pyproject.toml",
            "MANIFEST.in",
            "requirements.txt",
            ".gitignore",
            "src/PACKAGE-DIR/__init__.py",
            "src/PACKAGE-DIR/__main__.py",
        ]
    elif mode == "large":
        builder.directory_list = [
            "data/external",
            "data/interim",
            "data/processed",
            "data/raw",
            "docs",
            "models",
            "notebooks",
            "references",
            "reports/figures",
            "src/data",
            "src/features",
            "src/models",
            "src/visualization",
            "tests",
        ]
        builder.file_list = [
            "README.md",
            "setup.py",
            "main.py",
            "requirements.txt",
            "LICENSE",
            ".env",
            ".gitignore",
        ]
    elif os.path.exists(mirror_directory):
        mirror_directories, mirror_files = builder.mirror_project_structure(
            mirror_directory
        )
        builder.directory_list = mirror_directories
        builder.file_list = mirror_files
    else:
        raise ValueError(
            "Unknown mode specification, try 'minimal', 'medium', 'large' or 'packaging' or pass a valid directory path to read a structure from"
        )
    # initialize directory structure
    builder.initialize_structure()
